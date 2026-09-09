# Guided Self-Improvement Journey Design

## Status

Approved design for implementation planning.

## Purpose

Add a guided, evidence-disciplined workflow that helps an Agent Skills-compatible client move from a broad self-improvement request to a bounded, personalized, measurable path and a reusable final report.

The workflow is a coordination skill, not a new psychological theory, diagnostic system, therapy protocol, or autonomous life-planning authority.

## Design principles

- Preserve the user's autonomy and right to stop, change direction, or reject a hypothesis.
- Ask one question at a time and prefer the question with the highest information value.
- Use a recent concrete episode before making broad interpretations.
- Route selectively to the smallest useful specialist process; do not run all skills by default.
- Keep observations, reports, interpretations, hypotheses, predictions, and unknowns visibly separate.
- Require competing explanations and disconfirming evidence for material conclusions.
- Convert insight into one to three small, reversible, measurable actions or experiments.
- Treat the final report as a snapshot of a working model, not a verdict about the person.
- Use structured content as the source of truth; render it into Markdown and HTML presentation layers.
- Keep the public repository synthetic, dependency-free, network-free, and free of user-specific data.

## User journey

The skill follows these stages, with explicit stop/checkpoint behavior:

1. **Orientation and safety** — restate the request neutrally, establish scope, identify crisis or clinical boundaries, and obtain permission to proceed.
2. **Baseline interview** — ask one question at a time about the target, a recent episode, frequency, context, triggers, consequences, exceptions, constraints, and prior attempts.
3. **Bottleneck classification** — select the smallest primary route from clarity, belief, behavior, relationship, identity, decision, adversity, ambivalence, execution, or review.
4. **Specialist pass** — invoke only the selected specialist skill. A second route is allowed only when the new evidence creates a clear unresolved dependency.
5. **Model and evidence review** — summarize established facts, user reports, interpretations, competing hypotheses, evidence for and against, missing evidence, and confidence.
6. **Path selection** — choose a practical intervention class and confirm that the user accepts the target and its likely costs.
7. **Action or experiment design** — define one to three actions or experiments with cue, duration, metric, threshold, stop condition, confounds, and review trigger.
8. **User checkpoint** — ask the user to correct, narrow, reject, or approve the proposed path before presenting it as the working plan.
9. **Final synthesis** — populate the Markdown and HTML report contracts from the same structured content.
10. **Review and calibration** — schedule a review and route future outcome data to `review-calibration` rather than repeating unsupported advice.

The skill may stop early when the user has a sufficiently specific question, declines to continue, reaches a safe boundary, or lacks enough evidence for a responsible conclusion. It must not manufacture missing answers to complete the report.

## Report contract

The final report must include these sections, in this order:

1. Title, date, and status (`working draft`, `approved plan`, or `reviewed update`).
2. Scope and safety boundary.
3. Working question and primary target.
4. Current-state summary and relevant constraints.
5. Evidence ledger: observations, measures, reports, interpretations, and unknowns.
6. Competing hypotheses with confidence, supporting evidence, conflicting evidence, missing evidence, and predictions.
7. Selected path and rationale, including rejected or deferred alternatives.
8. Immediate actions, limited to one to three concrete steps.
9. Experiment cards with metrics, thresholds, stop conditions, and confounds.
10. Risks, escalation boundaries, and outside-expertise prompts where appropriate.
11. Unresolved questions and what would change the model.
12. Review date, review questions, and recalibration instructions.

The report must label inference as inference, avoid diagnostic language, avoid claims about another person's internal state, and avoid forced redemptive narratives.

## Presentation layers

### Markdown

`templates/FINAL_REPORT.md` is the portable source template. It must remain readable in GitHub, plain text, and version control, and must not require rendering tools.

### HTML/CSS

`templates/final-report.html` and `templates/final-report.css` are a dependency-free presentation template for the same report contract. The template must:

- use semantic landmarks and heading order;
- provide visible focus styles and sufficient color contrast;
- avoid color as the only way to communicate evidence status;
- include print styles for a clean paper/PDF export;
- remain responsive on narrow screens;
- use no JavaScript, remote fonts, external images, telemetry, or network requests;
- mark placeholders clearly so a renderer or agent cannot mistake them for user facts;
- include a short privacy note explaining that the report may contain sensitive user material and should not be published by default.

The HTML/CSS is a presentation template, not an application. ReflectiveOps does not promise a browser renderer or automatic file creation in every client.

## Skill interface

The new skill frontmatter must follow the existing Agent Skills contract and use the name `guided-self-improvement-journey`. Its description must be activation-oriented and mention broad self-improvement, structured interview, selective skill routing, personalized plan, and final report.

The body must define:

- invoke-when conditions;
- the journey procedure;
- routing and stop conditions;
- interview protocol;
- evidence and confidence rules;
- action/experiment requirements;
- report population instructions for both templates;
- safety and privacy requirements;
- completion criteria.

## Evaluation and validation

Add synthetic evaluation coverage for:

- broad request → interview before routing;
- selective specialist routing rather than all-skill execution;
- uncertainty and competing hypotheses;
- a measurable reversible plan with stop conditions;
- complete final-report section coverage;
- no diagnosis, mind-reading, or private-data reuse.

Extend repository content tests only where structural guarantees cannot be expressed in the eval cases. `make release-check` remains the final verification gate.

## Non-goals

- No runtime orchestration engine or persistent database.
- No clinical assessment, treatment plan, crisis service, or trauma-processing protocol.
- No automatic long-term life plan or promise of behavior change.
- No PDF-generation dependency or hosted report service.
- No requirement that every Agent Skills client support HTML file creation.
