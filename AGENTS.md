# AGENTS.md

This file governs AI agents contributing to the ReflectiveOps repository.

## Mission

Improve ReflectiveOps as a public, evidence-disciplined Agent Skills project without introducing:

- personal data,
- secrets,
- unsupported psychological certainty,
- diagnostic claims,
- hidden dependencies,
- private conversation material,
- unsafe pseudo-therapy behavior.

## Source of truth

Priority order:

1. `SECURITY.md`
2. `docs/SAFETY_MODEL.md`
3. `docs/PRIVACY.md`
4. `docs/PROJECT_CHARTER.md`
5. this file
6. individual skill instructions
7. examples and templates

## Required workflow

Before editing:

1. Read the target skill.
2. Read `docs/SKILL_AUTHORING_GUIDE.md`.
3. If changing safety-sensitive behavior, read `docs/SAFETY_MODEL.md`.
4. If changing a research claim, read `docs/RESEARCH_METHOD.md`.

After editing:

```bash
make release-check
```

All checks must pass.

## Privacy rules

Never add:

- real user names,
- real conversation excerpts,
- account names,
- personal addresses,
- contact details,
- private repository information,
- machine usernames,
- private filesystem paths,
- API credentials,
- secrets,
- memory-derived personal context.

All scenarios must be synthetic and marked as synthetic where they appear as worked examples.

Do not create a committed denylist containing a real person's private identifiers. A maintainer may use the optional local denylist mechanism described in `docs/PUBLICATION_SAFETY.md`.

## Skill rules

Every `skills/<name>/SKILL.md` must:

- have a directory name exactly matching the frontmatter `name`,
- use a lowercase hyphenated name,
- include a useful activation-oriented `description`,
- include `license: Apache-2.0`,
- keep project version under `metadata.version`,
- be understandable without hidden context,
- include the project's mandatory evidence and safety rules,
- distinguish facts from interpretations,
- avoid clinical diagnosis,
- avoid mind-reading,
- favor falsifiable hypotheses and reversible tests.

## Research rules

When a material behavioral or psychological claim is added:

- prefer systematic reviews, meta-analyses, authoritative guidance, or primary research,
- distinguish evidence from project design choices,
- record important limitations,
- do not turn correlational findings into causal claims,
- do not imply that evidence for clinician-delivered treatment automatically validates AI delivery of that treatment,
- update `references/RESEARCH_BASIS.md` when the claim is central to a skill.

## Engineering rules

- Prefer the Python standard library for repository checks.
- Do not add a dependency without a clear need.
- Do not add network access to tests.
- Do not use symlinks.
- Keep CI least-privilege.
- Pin GitHub Actions to immutable full commit SHAs.
- Do not use `pull_request_target` for untrusted contribution validation.
- Do not add telemetry.
- Do not make outbound requests from the skills.

## Change discipline

Prefer small, reviewable changes.

A change to a skill should normally include:

- the skill change,
- a synthetic evaluation case if behavior changes,
- documentation or research updates if assumptions change,
- passing release checks.

Do not silently broaden project scope.
