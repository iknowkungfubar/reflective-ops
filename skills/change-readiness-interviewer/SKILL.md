---
name: change-readiness-interviewer
description: Explore ambivalence when a user knows what they think they should change but is not committed, confident, or ready; preserve autonomy before planning action.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Change Readiness Interviewer

## Objective

Explore ambivalence before prescribing a behavior plan.

## Invoke when

The user:

- knows what they think they should do but resists,
- repeatedly makes plans they do not follow,
- feels split about a change,
- asks for motivation when commitment is uncertain.

This skill borrows non-clinical principles associated with motivational interviewing. It does not present itself as clinical motivational interviewing.

## Procedure

### 1. Define the target behavior
Make it observable.

### 2. Explore both sides
Ask:

- What would improve if this changed?
- What does the current situation provide or protect?
- What would be hard or costly about changing?

Treat reasons for the status quo as information, not resistance to defeat.

### 3. Importance
If useful:
> How important is this change right now on a rough zero-to-ten scale?

Then:
> Why that number rather than a lower number?

### 4. Confidence
If useful:
> If you chose to make the change, how confident are you that you could?

Then:
> What would raise confidence by one point?

### 5. Autonomy check
Ask:
> Is this actually your goal, or mainly something you believe you are supposed to want?

## Route

Choose:

- not chosen → stop planning it,
- chosen but not ready → reduce scope or gather resources,
- ready → `behavior-change-engineer`,
- uncertain → `experiment-designer`.

## Output

- target,
- reasons for change,
- reasons for status quo,
- importance,
- confidence,
- primary obstacle,
- user-chosen next step.

## Anti-manipulation rule

Do not selectively amplify only statements that favor change.

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
