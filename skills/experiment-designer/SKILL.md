---
name: experiment-designer
description: Turn an uncertain belief, behavior hypothesis, transition idea, or decision assumption into the smallest safe, reversible, measurable, falsifiable real-world experiment.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Experiment Designer

## Objective

Maximize learning per unit of cost by turning uncertainty into a small real-world test.

## Invoke when

A meaningful belief, behavior hypothesis, transition idea, or decision assumption can be tested before a larger commitment.

## Experiment card

### Question
What needs to be learned?

### H1
A falsifiable leading hypothesis.

### H2
At least one plausible competing hypothesis.

### Test
The smallest safe action that distinguishes them.

### Predictions
What should be observed if H1 is true?
What should be observed if H2 is true?

### Metric
What will be recorded?

### Duration or sample
Enough repetitions to learn something without oversizing the test.

### Threshold
Define useful success or failure criteria before seeing results.

### Stop condition
Safety, cost, time, or evidence threshold.

### Confounds
What else could explain the result?

### Decision consequence
How will each possible result change the next action?

## Quality test

A useful experiment is:

- safe,
- ethical,
- reversible,
- small,
- observable,
- informative,
- time-bounded,
- connected to a real decision.

## Anti-confirmation rule

Design the test so the user's preferred story can lose.

## Output

Return a filled experiment card unless the user asks for more.

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
