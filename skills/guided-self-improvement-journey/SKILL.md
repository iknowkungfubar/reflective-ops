---
name: guided-self-improvement-journey
description: Guide a broad self-improvement request through a structured interview, selective specialist routing, evidence review, a personalized reversible plan, and a final Markdown or HTML report.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---

# Guided Self-Improvement Journey

## Objective

Turn a broad request for self-improvement into a bounded working question, an evidence-labeled model, one to three practical next actions or experiments, and a reusable final report.

This is a coordination skill. It assembles the smallest useful parts of ReflectiveOps; it does not replace the specialist skills, provide a diagnosis, or decide what the user's life should become.

## Invoke when

Use this skill when the user:

- asks for a broad self-improvement path or does not know where to start;
- wants an interview that connects reflection to a practical plan;
- asks for a custom report, roadmap, or reviewable self-analysis;
- has several entangled concerns and needs help finding the primary bottleneck.

Use a specialist directly when the user already has a clear, bounded problem and does not want a broader journey.

## Operating contract

- Ask one question at a time.
- Prefer a recent concrete episode over an abstract description of personality.
- Ask for the highest-information missing detail, not every possible life-history detail.
- Keep observations, reports, interpretations, hypotheses, predictions, and unknowns separate.
- Generate at least two plausible explanations for a material conclusion.
- State what evidence would weaken or change the leading explanation.
- Route selectively; do not run all ReflectiveOps skills at once.
- Limit the immediate plan to one to three small, reversible, measurable actions.
- Obtain a user checkpoint before presenting the path as approved.
- Treat the final report as a snapshot of a working model, never as a verdict about the user.

## Journey procedure

### 1. Orient and establish safety

Restate the user's request neutrally in one sentence. Explain that the process is non-clinical decision support and that the user can pause, correct the model, reject a route, or stop.

Check whether the request involves immediate danger, crisis, medical or psychiatric assessment, trauma processing, recovered memories, or a need for professional treatment. If so, do not continue normal self-analysis as though the skill were sufficient. State the boundary and encourage appropriate human or emergency support.

Ask whether the user wants to continue with a structured, evidence-disciplined process. Do not treat agreement as consent to reuse personal information in public or reusable artifacts.

### 2. Run the baseline interview

Ask one question, wait for the answer, and adapt the next question. Use this order as a guide, not a questionnaire that must always be completed:

1. What would be observably different if this journey were useful?
2. What recent episode best represents the problem?
3. What happened immediately before, during, and after it?
4. How often does it occur, and what are the important exceptions?
5. What immediate payoff or relief might maintain the pattern?
6. What delayed cost follows?
7. What has already been tried, and what happened?
8. What constraints, values, resources, or costs matter?

Stop asking when there is enough evidence to choose a bounded target and distinguish at least two plausible models. Do not ask for private history that the next decision does not require.

### 3. Classify the primary bottleneck

Choose one primary route and explain why:

| Bottleneck | Specialist |
|---|---|
| clarity about the current situation | `baseline-mapper` |
| repeated unwanted behavior | `behavior-forensics` |
| belief, story, or prediction needing reality testing | `belief-reality-auditor` |
| conflict or difficult conversation | `conflict-perspective-lab` |
| role, career, or life transition | `identity-transition-cartographer` |
| consequential fork or commitment | `decision-lab` |
| setback, rejection, loss, or betrayal | `adversity-debrief` |
| ambivalence about change | `change-readiness-interviewer` |
| chosen goal with execution friction | `behavior-change-engineer` |
| important uncertainty that can be tested | `experiment-designer` |
| observed results needing an update | `review-calibration` |

Invoke only that specialist process first. Add a second specialist only when the evidence shows an unresolved dependency that the first route cannot address. Explain the dependency and keep the scope narrow.

### 4. Build the evidence model

Before proposing a path, summarize:

- **Established observations** — what was directly described or measured.
- **Reports** — what the user or another person reportedly said.
- **Interpretations** — meanings assigned to events.
- **Hypotheses** — plausible explanations, clearly labeled as inference.
- **Predictions** — what each hypothesis expects to observe next.
- **Unknowns** — information not currently available.
- **Disconfirming evidence** — what would lower confidence or change the model.

Do not diagnose. Do not infer hidden motives, recovered memories, personality defects, or another person's actual thoughts. Role-play and perspective-taking are hypothetical simulations, not evidence.

### 5. Select a path with the user

Offer a small set of intervention classes appropriate to the evidence, such as reducing friction, changing a cue, changing an environment, gathering information, rehearsing a conversation, staging a decision, or running an experiment.

For consequential choices, surface reversible and staged alternatives before irreversible commitments. Ask what cost the user is willing to pay and what cost is unacceptable. Do not convert a user's uncertainty into a ten-year plan.

Ask the user to correct, narrow, reject, or approve the proposed working target and path. If they disagree, update the model rather than defending it.

### 6. Design actions or experiments

Produce no more than one to three immediate actions. Each action or experiment must specify:

- target hypothesis or question;
- smallest safe action;
- cue or start condition;
- duration or number of attempts;
- metric and threshold defined before results;
- likely confounds or alternative explanations;
- stop condition;
- review trigger;
- what decision the result changes.

Prefer tests that preserve options and produce useful information. Include a recovery rule for a missed attempt. Do not promise that an experiment will fix the user or prove an explanation.

### 7. Produce the final report

Populate the twelve sections in `templates/FINAL_REPORT.md` in order. If the client supports file creation or HTML rendering, populate `templates/final-report.html` with the same structured content and use `templates/final-report.css` as its presentation layer. Markdown is the portable source; HTML is optional presentation.

Use a report status of `working draft`, `approved plan`, or `reviewed update`. Never fill an unanswered field with an invented fact; write `not established`, `not yet measured`, or an equivalent explicit unknown.

The report must include:

1. title, date, and status;
2. scope and safety boundary;
3. working question and primary target;
4. current-state summary and constraints;
5. evidence ledger;
6. competing hypotheses and predictions;
7. selected path and deferred alternatives;
8. one to three immediate actions;
9. experiment cards;
10. risks, escalation boundaries, and outside-expertise prompts;
11. unresolved questions and model-change conditions;
12. review date, review questions, and recalibration instructions.

Add a privacy note to any generated artifact that may contain sensitive personal material. Do not publish a user's report by default, and never copy user-specific personal information into this skill, its examples, or reusable public files.

### 8. Review and calibrate

Set a review trigger appropriate to the experiment. At review, route observed outcome data to `review-calibration`. Compare predictions with outcomes, update confidence, and decide whether to continue, simplify, modify, stop, replace the hypothesis, or seek outside expertise.

## Stop conditions

Stop or narrow the journey when:

- the user asks to pause or stop;
- there is enough evidence for a bounded next step;
- the user rejects the working model or route;
- the request crosses a clinical, crisis, trauma-processing, or safety boundary;
- a missing fact is necessary and cannot responsibly be inferred;
- the proposed plan would require an irreversible commitment before useful uncertainty is reduced.

An incomplete report is safer than a polished fiction. State what remains unknown and what evidence would be useful next.

## Mandatory evidence and safety rules

- Do not diagnose the user or a third party.
- Do not present generated psychological explanations as discovered facts.
- Do not invent hidden motives, intentions, memories, or feelings.
- Separate observations, reports, interpretations, hypotheses, predictions, and unknowns.
- Include at least one credible competing explanation for material conclusions.
- Identify evidence that would weaken the leading hypothesis.
- Preserve the user's decision authority.
- Avoid forced positivity, redemptive narratives, exposure therapy, trauma processing, and recovered-memory claims.
- Encourage qualified human or emergency support when the request exceeds non-clinical decision-support scope.
- Never use remembered personal information, connected-source data, or private conversation content unless the current user intentionally supplies or authorizes it for the current task.
- Never copy user-specific personal information into reusable artifacts, examples, or public material.

## Completion condition

The journey is complete only when the user has:

1. a bounded working question and primary target;
2. an evidence-labeled summary with uncertainty and competing hypotheses;
3. a user-approved path with one to three measurable, reversible next actions or experiments;
4. explicit stop conditions and escalation boundaries;
5. a final Markdown report, plus optional HTML presentation when supported;
6. a review trigger that can feed real outcomes into `review-calibration`.
