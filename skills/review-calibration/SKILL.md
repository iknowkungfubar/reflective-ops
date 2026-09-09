---
name: review-calibration
description: Review real results from a plan, behavior, conversation, decision, or experiment; compare predictions with outcomes, update hypotheses, and choose the next cycle.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Review Calibration

## Objective

Use real outcome data to make the next model less wrong.

## Invoke when

The user has results from:

- a plan,
- routine,
- conversation,
- decision,
- experiment,
- transition test.

## Procedure

### 1. Planned versus actual
What was intended?
What happened?

### 2. Prediction check
For important predictions record:

- predicted outcome,
- confidence,
- observed outcome,
- error.

### 3. Behavioral data
When relevant:

- attempts,
- completions,
- misses,
- contexts,
- exceptions.

### 4. Surprise
Ask:
> What happened that the current model did not predict?

Unexpected observations are high-value evidence.

### 5. Hypothesis update
For each active hypothesis:

- confidence before,
- new evidence,
- confidence now,
- reason.

### 6. Intervention decision

Choose:

- continue,
- simplify,
- intensify,
- change cue,
- change environment,
- replace hypothesis,
- stop,
- seek outside expertise.

### 7. Next cycle
Set one to three actions.

## Output

### Scoreboard
Minimal metrics.

### Prediction errors
What the model got wrong.

### Updated hypotheses
Confidence changes.

### Decision
Continue / modify / stop / escalate.

### Next cycle
One to three actions and a review trigger.

## Anti-shame rule

Do not interpret missed actions as moral failure. Ask what the miss reveals about the system.

## Mandatory evidence and safety rules

- Do not diagnose the user or a third party.
- Do not present generated psychological explanations as discovered facts.
- Do not invent hidden motives, intentions, memories, or feelings.
- Separate observations, interpretations, hypotheses, predictions, and unknowns.
- For material conclusions, consider at least one credible competing explanation.
- Identify evidence that would weaken the leading hypothesis.
- Preserve the user's decision authority.
- Do not copy user-specific personal information into reusable artifacts, examples, or public material.
- Treat examples in this skill as procedural illustrations, not templates for assuming facts about a user.
