# Guided Self-Improvement Journey Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a selective guided journey skill that turns an interview into an evidence-labeled self-improvement path and renders the same report content through Markdown and polished HTML/CSS templates.

**Architecture:** Keep orchestration and reasoning in a new Agent Skill, with no runtime engine or dependencies. Treat `templates/FINAL_REPORT.md` as the portable content contract and `templates/final-report.html` plus `templates/final-report.css` as a dependency-free presentation layer over the same sections. Extend repository validation through synthetic evals and focused structural tests, then update public documentation and the minor release metadata.

**Tech Stack:** Agent Skills Markdown with YAML frontmatter, Markdown, semantic HTML5, CSS media queries/print styles, Python standard-library validation and unittest.

**Spec:** `docs/superpowers/specs/2026-09-09-guided-self-improvement-journey-design.md`

## Global Constraints

- Preserve user autonomy; do not diagnose, mind-read, recover memories, or present hypotheses as facts.
- Ask one question at a time and prefer recent concrete evidence.
- Route selectively; do not run all skills by default.
- Limit immediate actions to one to three small, reversible, measurable steps.
- Keep the public repository synthetic, dependency-free, network-free, and free of user-specific data.
- The HTML/CSS template uses no JavaScript, remote fonts, external images, telemetry, or network requests.
- `make release-check` is the final verification gate.

## File map

- Create `skills/guided-self-improvement-journey/SKILL.md`: staged journey procedure, routing, interview, evidence model, report population, safety, and completion contract.
- Create `templates/FINAL_REPORT.md`: GitHub-readable report content template with all twelve required sections.
- Create `templates/final-report.html`: semantic HTML report shell using clearly marked placeholders and accessible evidence/status labels.
- Create `templates/final-report.css`: responsive, high-contrast, print-friendly visual system with no external dependencies.
- Modify `evals/cases.json`: add synthetic behavior cases for interview-first routing, selective orchestration, plan safety, and report completeness.
- Modify `tests/test_repo_content.py`: add structural tests for the new skill and presentation templates.
- Modify `README.md`: document the guided journey as the recommended broad-request entry point and explain Markdown/HTML report outputs.
- Modify `AGENT_INTEGRATION.md`: add the guided journey route and final-report rendering instructions.
- Modify `docs/ARCHITECTURE.md`: document the staged journey and presentation-layer split.
- Modify `CHANGELOG.md`, `VERSION`, and `pyproject.toml`: publish the new capability as version 1.1.0.
- Modify all existing skill metadata versions from 1.0.0 to 1.1.0 so the package metadata matches the release line.

---

### Task 1: Add failing structural tests and synthetic eval cases

**Files:**
- Modify: `tests/test_repo_content.py`
- Modify: `evals/cases.json`

**Interfaces:**
- Tests consume repository paths and JSON eval records; they produce failures until the new skill and templates exist.
- Later tasks rely on test names and required markers as the acceptance contract.

- [ ] **Step 1: Add tests for the new skill and report assets**

Add focused unittest methods that assert:

```python
journey = ROOT / "skills" / "guided-self-improvement-journey" / "SKILL.md"
self.assertTrue(journey.exists())
journey_text = journey.read_text(encoding="utf-8").lower()
for phrase in ("one question at a time", "competing hypotheses", "do not diagnose", "final_report.md", "final-report.html"):
    self.assertIn(phrase.lower(), journey_text)

for rel in ("templates/FINAL_REPORT.md", "templates/final-report.html", "templates/final-report.css"):
    self.assertTrue((ROOT / rel).exists())

html = (ROOT / "templates/final-report.html").read_text(encoding="utf-8").lower()
self.assertIn("<main", html)
self.assertIn("privacy", html)
self.assertNotIn("<script", html)
```

- [ ] **Step 2: Add synthetic eval records**

Add six cases for the new skill with assertions covering interview-first behavior, selective routing, uncertainty labeling, reversible action design, twelve-section report completeness, and privacy/safety boundaries. Every record must set `synthetic` to `true` and use stable IDs beginning with `guided-`.

- [ ] **Step 3: Run the focused tests to verify RED**

Run:

```bash
python3 -m unittest tests.test_repo_content -v
```

Expected: failures report the missing journey skill/templates and the eval count/skill mismatch. No implementation files exist yet, so this demonstrates the tests detect the feature gap.

---

### Task 2: Implement the guided journey skill

**Files:**
- Create: `skills/guided-self-improvement-journey/SKILL.md`

**Interfaces:**
- Consumes: the existing specialist skill names, `core/SESSION_PROTOCOL.md`, and the report template section contract.
- Produces: a client-readable procedure that returns a working journey state plus populated report content; no executable API is introduced.

- [ ] **Step 1: Write Agent Skills frontmatter and activation contract**

Use `name: guided-self-improvement-journey`, an activation-oriented description mentioning broad self-improvement, structured interview, selective routing, personalized path, and final report, `license: Apache-2.0`, Agent Skills compatibility, and metadata version `1.1.0`.

- [ ] **Step 2: Add the ten-stage procedure**

Document orientation/safety, baseline interview, bottleneck classification, one specialist pass, evidence review, path selection, action/experiment design, user checkpoint, final synthesis, and review/calibration. State that the skill may stop early and must never invent missing answers.

- [ ] **Step 3: Add routing and output rules**

Map bottlenecks to existing specialist skills, permit a second route only for an evidence-based dependency, and instruct the agent to populate the Markdown and HTML templates from the same structured content. Require one to three immediate actions, metrics, thresholds, stop conditions, confounds, and a review trigger.

- [ ] **Step 4: Add explicit safety, privacy, and completion blocks**

Include the project’s mandatory safety concepts plus crisis/clinical escalation, no forced meaning-making, no private-data reuse, and completion only when the user has a bounded target, acknowledged uncertainty, an approved next path, and a scheduled review.

- [ ] **Step 5: Run repository validation to verify GREEN for this task**

Run:

```bash
python3 scripts/validate_repo.py
python3 -m unittest tests.test_repo_content -v
```

Expected: the new skill passes frontmatter and mandatory safety validation; the structural tests pass once the templates are added in Task 3.

---

### Task 3: Add the final report content and presentation templates

**Files:**
- Create: `templates/FINAL_REPORT.md`
- Create: `templates/final-report.html`
- Create: `templates/final-report.css`

**Interfaces:**
- Consumes: the twelve-section report contract in the approved design specification.
- Produces: portable Markdown plus semantic HTML/CSS presentations with identical section order and clearly marked placeholders.

- [ ] **Step 1: Add the Markdown report template**

Create all twelve required sections in order. Use placeholders such as `[working question]` and `[H1 — plausible explanation]`, label status as a working draft/approved plan/reviewed update, and include a publication privacy warning.

- [ ] **Step 2: Add the semantic HTML report template**

Create `<!doctype html>`, `header`, `nav`/contents, `main`, `section`, `article`, and `footer` landmarks. Include the same twelve headings, placeholder markers, evidence-status text labels, action/experiment cards, and a visible privacy notice. Do not add scripts or external resources.

- [ ] **Step 3: Add the CSS presentation system**

Define a restrained editorial visual system with readable measure, clear hierarchy, cards for evidence/hypotheses/actions, responsive layout, `:focus-visible` styles, contrast-safe status labels, and `@media print` rules. Use system font stacks and CSS variables only.

- [ ] **Step 4: Run focused template tests**

Run:

```bash
python3 -m unittest tests.test_repo_content -v
```

Expected: all repository-content tests pass, including semantic HTML, no-script, and privacy-marker assertions.

---

### Task 4: Update documentation and release metadata

**Files:**
- Modify: `README.md`
- Modify: `AGENT_INTEGRATION.md`
- Modify: `docs/ARCHITECTURE.md`
- Modify: `CHANGELOG.md`
- Modify: `VERSION`
- Modify: `pyproject.toml`
- Modify: `skills/*/SKILL.md` metadata version values

**Interfaces:**
- Documentation consumes the new skill and template names; release metadata produces a coherent 1.1.0 package identity.

- [ ] **Step 1: Update README and integration guidance**

Make the guided journey the recommended route for broad self-improvement requests, explain that it interviews before selective routing, and document both Markdown and optional HTML/CSS report outputs with their privacy limitations.

- [ ] **Step 2: Update architecture documentation**

Add the journey as the top-level flow above the existing specialist router, describe the shared structured report content, and state that HTML is presentation-only and not an execution engine.

- [ ] **Step 3: Update release metadata and changelog**

Set `VERSION` and `pyproject.toml` to `1.1.0`, add a dated `1.1.0` changelog entry, and update all skill metadata versions to `1.1.0`.

- [ ] **Step 4: Run the complete release gate**

Run:

```bash
make release-check
git diff --check HEAD~1..HEAD
```

Expected: repository validation, public-release scan, and all unit tests pass. Any Markdown hard-break warnings must be reviewed and preserved only where intentional.

---

### Task 5: Commit, push, and verify delivery

**Files:**
- No additional source files; verify the complete branch diff and remote state.

**Interfaces:**
- Consumes: the completed local branch and GitHub repository settings.
- Produces: a pushed feature branch containing the verified implementation, ready for a protected-`main` pull request.

- [ ] **Step 1: Review the final file set and privacy surface**

Run:

```bash
git status --short --branch
git diff --stat origin/main...HEAD
git ls-files | sort
python3 scripts/public_release_scan.py
```

Confirm only the planned repository files changed and no personal data, secrets, private paths, or network dependencies were added.

- [ ] **Step 2: Commit the implementation**

Use:

```bash
git add AGENT_INTEGRATION.md CHANGELOG.md README.md VERSION pyproject.toml docs/ARCHITECTURE.md evals/cases.json tests/test_repo_content.py templates skills/guided-self-improvement-journey skills/*/SKILL.md
git commit -m "feat: add guided self-improvement journey reports"
```

- [ ] **Step 3: Push the feature branch**

Use:

```bash
git push --set-upstream origin feat/guided-self-improvement-journey
```

Do not bypass protected `main`; the branch is ready for a pull request and required `validate` check.

- [ ] **Step 4: Verify the remote branch and CI**

Run:

```bash
gh api repos/iknowkungfubar/reflective-ops/branches/feat%2Fguided-self-improvement-journey --jq '{name,sha}'
gh run list --repo iknowkungfubar/reflective-ops --branch feat/guided-self-improvement-journey --limit 5
```

Expected: the remote branch SHA matches the local commit and the validation workflow completes successfully.
