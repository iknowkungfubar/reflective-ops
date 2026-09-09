---
name: belief-reality-auditor
description: Reality-test an action-relevant belief, prediction, interpretation, identity conclusion, or mind-reading claim by separating evidence from story and designing discriminating tests.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Belief Reality Auditor

## Objective

Replace an **untested story** with a better-calibrated model.

## Invoke when

A belief materially affects the user's actions, such as:

- “I always fail.”
- “Nobody respects me.”
- “If I make one mistake, people will think I am incompetent.”
- “This path is closed to me.”
- “They ignored me because they do not care.”

## Decompose the claim

Capture:

1. exact claim,
2. scope,
3. claim type:
   - factual,
   - interpretation,
   - prediction,
   - value judgment,
   - mind-reading,
   - identity conclusion,
4. confidence if useful,
5. behavior caused by the belief.

## Evidence audit

Create:

- supporting evidence,
- conflicting evidence,
- ambiguous evidence,
- missing evidence.

Ask:
> What observation would meaningfully reduce confidence in this belief?

If no possible evidence could change it, classify it as a narrative, identity statement, or value judgment rather than a testable claim.

## Alternative models

Generate at least two plausible interpretations when evidence permits.

For each:
- what it explains,
- what it fails to explain,
- what it predicts.

Do not force a “positive” alternative when the original belief is well-supported.

## Reality test

When safe, turn the disagreement into a small behavioral test.

## Output

### Claim map
Fact / interpretation / prediction / identity conclusion.

### Evidence ledger
Support / conflict / ambiguous / missing.

### Competing models
With confidence labels.

### What would change the model
Concrete evidence.

### Next test
One real-world observation or experiment.

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
