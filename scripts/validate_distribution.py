#!/usr/bin/env python3
"""Validate the portable skill and plugin distribution without third-party packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = "agentic-engineering"
VERSION = "2.1.0"
SKILL_FIELDS = {"name", "description"}
LOCAL_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def parse_frontmatter(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    require(lines and lines[0] == "---", f"{path.relative_to(ROOT)}: missing frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValidationError(f"{path.relative_to(ROOT)}: unclosed frontmatter") from exc

    values: Dict[str, str] = {}
    for line in lines[1:end]:
        require(":" in line, f"{path.relative_to(ROOT)}: malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        require(key not in values, f"{path.relative_to(ROOT)}: duplicate frontmatter field {key}")
        values[key] = value.strip().strip("\"'")
    return values


def markdown_files() -> Iterable[Path]:
    yield from ROOT.rglob("*.md")


def validate_required_files() -> None:
    required = [
        ROOT / ".codex-plugin/plugin.json",
        ROOT / ".agents/plugins/marketplace.json",
        ROOT / ".claude-plugin/plugin.json",
        ROOT / ".claude-plugin/marketplace.json",
        ROOT / "plugin.json",
        ROOT / "README.md",
        ROOT / "NOTICE.md",
        ROOT / "LICENSE",
        ROOT / "THIRD_PARTY_NOTICES.md",
        ROOT / "CHANGELOG.md",
        ROOT / "docs/COMPATIBILITY.md",
        ROOT / "docs/DECISIONS.md",
        ROOT / "docs/EVALUATION.md",
        ROOT / "docs/SKILL_RECIPES.md",
        ROOT / "docs/GITHUB_REVIEW.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / ".github/copilot-instructions.md",
        ROOT / "evals/cases.json",
        ROOT / "scripts/evaluate_behavior.py",
        ROOT / "scripts/sync_shared_references.py",
        ROOT / "scripts/sync_agent_instructions.py",
        ROOT / "LICENSES/Peter-Yang-MIT.txt",
        ROOT / "LICENSES/Solid-Skills-MIT-notice.md",
    ]
    for path in required:
        require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
    require(not (ROOT / "SKILL.md").exists(), "root SKILL.md would create a duplicate skill")
    require(not any((ROOT / "adapters").rglob("*")) if (ROOT / "adapters").exists() else True,
            "legacy adapters directory must be empty or absent")


def validate_skills() -> List[str]:
    names: List[str] = []
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    require(len(skill_dirs) == 5, f"expected five canonical skills, found {len(skill_dirs)}")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        require(skill_file.is_file(), f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
        fields = parse_frontmatter(skill_file)
        require(set(fields) == SKILL_FIELDS,
                f"{skill_file.relative_to(ROOT)}: canonical frontmatter must contain only name and description")
        name = fields["name"]
        description = fields["description"]
        require(name == skill_dir.name,
                f"{skill_file.relative_to(ROOT)}: name must match directory")
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None,
                f"{skill_file.relative_to(ROOT)}: invalid skill name")
        require(1 <= len(description) <= 1024,
                f"{skill_file.relative_to(ROOT)}: description must be 1..1024 characters")
        require(name not in names, f"duplicate skill name: {name}")
        names.append(name)

        metadata = skill_dir / "agents/openai.yaml"
        require(metadata.is_file(), f"{skill_dir.relative_to(ROOT)}: missing agents/openai.yaml")
        metadata_text = metadata.read_text(encoding="utf-8")
        for field in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation:"):
            require(field in metadata_text, f"{metadata.relative_to(ROOT)}: missing {field}")
        require("products:" not in metadata_text,
                f"{metadata.relative_to(ROOT)}: unsupported policy.products field")

    require(set(names) == {
        NAME,
        "implementation-quality",
        "pr-readiness",
        "pr-feedback-closure",
        "reliable-ai-coding",
    },
            f"unexpected canonical skills: {', '.join(names)}")
    return names


def _clean_link(raw: str) -> str:
    target = raw.strip().split(" ", 1)[0]
    return target.strip("<>")


def validate_links() -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LOCAL_LINK.finditer(text):
            target = _clean_link(match.group(1))
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            require(target_path.exists(),
                    f"{path.relative_to(ROOT)}: broken local link {target}")
            require(ROOT in target_path.parents or target_path == ROOT,
                    f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            if SKILLS in path.parents:
                skill_root = next(
                    candidate for candidate in path.parents
                    if candidate.parent == SKILLS
                )
                require(skill_root in target_path.parents or target_path == skill_root,
                        f"{path.relative_to(ROOT)}: skill link escapes its package: {target}")


def validate_manifests() -> None:
    codex = load_json(ROOT / ".codex-plugin/plugin.json")
    claude = load_json(ROOT / ".claude-plugin/plugin.json")
    copilot = load_json(ROOT / "plugin.json")
    manifests = [codex, claude, copilot]

    for manifest in manifests:
        require(manifest.get("name") == NAME, "plugin manifest name drift")
        require(manifest.get("version") == VERSION, "plugin manifest version drift")
        require(manifest.get("author", {}).get("name") == "Luis Lobo",
                "plugin manifest author drift")

    descriptions = {manifest.get("description") for manifest in manifests}
    keywords = {tuple(manifest.get("keywords", [])) for manifest in manifests}
    require(len(descriptions) == 1, "plugin manifest description drift")
    require(len(keywords) == 1, "plugin manifest keyword drift")
    require("ai-coding" in codex.get("keywords", []),
            "plugin manifests must expose the reliable AI-coding capability")

    require(codex.get("skills") == "./skills/", "Codex skills path must be ./skills/")
    require(codex.get("interface", {}).get("developerName") == "Luis Lobo",
            "Codex developer metadata missing")
    require(claude.get("skills") == "./skills/", "Claude skills path must be ./skills/")
    require("commands" not in claude, "Claude must use the canonical skills without command aliases")
    require(copilot.get("skills") == "skills/", "Copilot skills path must be skills/")

    codex_market = load_json(ROOT / ".agents/plugins/marketplace.json")
    claude_market = load_json(ROOT / ".claude-plugin/marketplace.json")
    require(codex_market.get("name") == "luislobo-agentic-engineering",
            "Codex marketplace name drift")
    require(claude_market.get("name") == "luislobo-agentic-engineering",
            "Claude marketplace name drift")
    require(codex_market["plugins"][0]["name"] == NAME,
            "Codex marketplace plugin name drift")
    require(claude_market["plugins"][0]["name"] == NAME,
            "Claude marketplace plugin name drift")
    require(codex_market["plugins"][0]["source"]["path"] == "./",
            "Codex marketplace must point to repository root")
    require(claude_market["plugins"][0]["source"] == "./",
            "Claude marketplace must point to repository root")
    require(claude_market["plugins"][0]["version"] == VERSION,
            "Claude marketplace version drift")


def validate_safety_contracts() -> None:
    status = (SKILLS / "pr-readiness/SKILL.md").read_text(encoding="utf-8")
    closure = (SKILLS / "pr-feedback-closure/SKILL.md").read_text(encoding="utf-8")
    closure_meta = (SKILLS / "pr-feedback-closure/agents/openai.yaml").read_text(encoding="utf-8")

    require("This skill never mutates" in status, "pr-readiness must declare its no-mutation boundary")
    require("Never edit code" in parse_frontmatter(SKILLS / "pr-readiness/SKILL.md")["description"],
            "pr-readiness description must prohibit edits")
    require("Use only when the user explicitly asks" in
            parse_frontmatter(SKILLS / "pr-feedback-closure/SKILL.md")["description"],
            "pr-feedback-closure must require explicit mutation intent")
    require("stop for human approval" in closure,
            "pr-feedback-closure must pause for disposition approval")
    require("Never merge without separate explicit authorization" in closure,
            "pr-feedback-closure must keep merge authorization separate")
    require("Always retrieve and read suppressed review material" in closure,
            "pr-feedback-closure must inspect suppressed review material")
    require("Always read suppressed review material" in status,
            "pr-readiness must inspect suppressed review material")
    require("allow_implicit_invocation: false" in closure_meta,
            "Codex metadata must disable implicit PR mutation")
    require(not (ROOT / "commands").exists(),
            "legacy command aliases must not reintroduce obsolete names")


def validate_instruction_contracts() -> None:
    main = (SKILLS / "agentic-engineering/SKILL.md").read_text(encoding="utf-8")
    implementation = (SKILLS / "implementation-quality/SKILL.md").read_text(encoding="utf-8")
    reliable = (SKILLS / "reliable-ai-coding/SKILL.md").read_text(encoding="utf-8")
    routing = (SKILLS / "reliable-ai-coding/references/skill-routing.md").read_text(
        encoding="utf-8",
    )
    require("## Non-negotiable gates" in main,
            "agentic-engineering must distinguish hard gates from heuristics")
    require(len(main) <= 10_000,
            "agentic-engineering SKILL.md exceeds the progressive-disclosure budget")
    require("## Precedence" in implementation,
            "implementation-quality must define guidance strength and precedence")
    prohibited = (
        "ALWAYS use this skill",
        "ALWAYS Start with Tests",
        "Value Objects are MANDATORY",
        "No more than two instance variables per class",
    )
    require(not any(phrase in implementation for phrase in prohibited),
            "implementation-quality reintroduced a context-free absolute")
    require("## Required gates" in reliable,
            "reliable-ai-coding must define its evidence and authorization gates")
    require("Inspect before edit" in reliable and "Evidence before acceptance" in reliable,
            "reliable-ai-coding must preserve inspect-before-edit and evidence gates")
    require(len(reliable) <= 10_000,
            "reliable-ai-coding SKILL.md exceeds the progressive-disclosure budget")
    descriptions = {
        name: parse_frontmatter(SKILLS / f"{name}/SKILL.md")["description"]
        for name in (NAME, "implementation-quality", "reliable-ai-coding")
    }
    require("Use reliable-ai-coding instead for ordinary" in descriptions[NAME],
            "agentic-engineering must route ordinary bounded work to reliable-ai-coding")
    require("reliable-ai-coding or agentic-engineering" in descriptions["implementation-quality"],
            "implementation-quality must identify both primary workflows that invoke it")
    require("Defer greenfield systems" in descriptions["reliable-ai-coding"],
            "reliable-ai-coding must defer consequential work to agentic-engineering")
    require("Applies to features, bugs, refactors, architecture" not in
            descriptions["reliable-ai-coding"],
            "reliable-ai-coding must not overlap agentic-engineering architecture triggers")
    for contract in (
        "one primary",
        "Escalate from `reliable-ai-coding` to `agentic-engineering`",
        "sequentially, not simultaneously",
    ):
        require(contract in routing,
                f"reliable-ai-coding routing contract missing: {contract}")


def validate_shared_references() -> None:
    canonical = SKILLS / "pr-feedback-closure/references/lifecycle.md"
    generated = SKILLS / "agentic-engineering/references/pr-feedback-closure.md"
    require(canonical.read_bytes() == generated.read_bytes(),
            "shared PR lifecycle reference drift; run scripts/sync_shared_references.py")


def validate_agent_instructions() -> None:
    canonical = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    copilot = (ROOT / ".github/copilot-instructions.md").read_text(encoding="utf-8")
    require(claude.startswith("@AGENTS.md"),
            "CLAUDE.md must import the canonical AGENTS.md")
    require(copilot.endswith(canonical),
            "Copilot instructions must be generated from AGENTS.md")
    require("suppressed review material" in canonical,
            "canonical agent instructions must require suppressed-comment intake")


def validate_evals() -> None:
    document = load_json(ROOT / "evals/cases.json")
    require(document.get("schema_version") == 1, "eval cases schema version must be 1")
    cases = document.get("cases")
    require(isinstance(cases, list) and len(cases) >= 10,
            "behavioral eval suite must contain the ten core cases")
    ids = [case.get("id") for case in cases]
    require(len(ids) == len(set(ids)), "behavioral eval case IDs must be unique")
    required_ids = {
        "tiny-fix-lean",
        "normal-pr-ceremony",
        "high-risk-migration",
        "audit-read-only",
        "feedback-approval-gate",
        "unknown-without-evidence",
        "merge-separate-authorization",
        "bounded-ai-coding-task",
        "skill-routing-meaningful-feature",
        "github-review-without-copilot",
    }
    require(required_ids.issubset(ids), "behavioral eval suite is missing a core case")


def validate_licensing() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    require("MIT License" in license_text and "Copyright (c) 2026 Luis Lobo" in license_text,
            "root MIT license is missing or has the wrong owner")
    notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    for source in ("Solid Skills", "no-ai-slop", "Peter Yang", "Ramziddin"):
        require(source.lower() in notices.lower(),
                f"THIRD_PARTY_NOTICES.md: missing {source}")
    peter_license = (ROOT / "LICENSES/Peter-Yang-MIT.txt").read_text(encoding="utf-8")
    require("Copyright (c) 2026 Peter Yang" in peter_license,
            "Peter Yang MIT notice is incomplete")


def validate_credits_and_docs() -> None:
    notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
    for credit in (
        "Luis Lobo",
        "Josh Bleecher Snyder",
        "Ramziddin",
        "Peter Yang",
        "Building Toward Computer Use with Anthropic",
    ):
        require(credit in notice, f"NOTICE.md: missing credit for {credit}")

    compatibility = (ROOT / "docs/COMPATIBILITY.md").read_text(encoding="utf-8")
    for platform in ("Codex", "Claude Code", "GitHub Copilot CLI", "Google Antigravity 2"):
        require(platform in compatibility, f"compatibility contract missing {platform}")

    github_review = (ROOT / "docs/GITHUB_REVIEW.md").read_text(encoding="utf-8")
    for contract in (
        "Copilot is optional",
        "@codex review",
        "@claude review",
        "@claude review always",
        "Claude Code GitHub Action",
        "In interactive mode",
        "In automation mode",
        "Antigravity has no universal GitHub mention",
        "repository-defined on-demand comment",
        "not an individual step",
        "Never combine `pull_request_target`",
        "gh",
        "GraphQL",
        "Unknown",
    ):
        require(contract in github_review,
                f"GitHub review contract missing: {contract}")

    lifecycle = (SKILLS / "pr-feedback-closure/references/lifecycle.md").read_text(
        encoding="utf-8",
    )
    require("@codex review" in lifecycle,
            "PR feedback closure must document configured Codex review")
    require("fresh Copilot review" not in lifecycle and "Copilot pass" not in lifecycle,
            "PR feedback closure must not require a Copilot-specific review")
    require("system-engineering workflow" not in lifecycle,
            "PR feedback closure must use the canonical agentic-engineering name")


def validate_all() -> None:
    validate_required_files()
    validate_skills()
    validate_links()
    validate_manifests()
    validate_safety_contracts()
    validate_instruction_contracts()
    validate_shared_references()
    validate_agent_instructions()
    validate_evals()
    validate_licensing()
    validate_credits_and_docs()


def main() -> int:
    try:
        validate_all()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: distribution, manifests, links, safety contracts, and credits")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
