---
name: decision-lab
description: Analyze a consequential fork or difficult decision using explicit criteria, hidden options, independent premortems, reversibility, value of information, and decision triggers.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Decision Lab

## Objective

Improve decision quality under uncertainty without pretending to predict the future.

## Invoke when

The user faces a meaningful fork with real trade-offs.

## 1. Define the decision

Capture:

- exact decision,
- deadline,
- default/do-nothing path,
- options,
- constraints,
- hard red lines.

Always look for hidden options:

- delay,
- staged commitment,
- trial,
- partial version,
- information-gathering step.

## 2. Criteria

Ask what matters to the user.

Possible criteria:

- downside,
- time,
- energy,
- learning,
- meaning,
- relationship impact,
- reversibility,
- option value,
- probability of success,
- worst-case survivability.

Do not assign weights without user input.

## 3. Independent premortem

For each option separately:

Imagine a relevant future date when the option failed badly.

Work backward:

- plausible failure path,
- early warning signs,
- false assumptions,
- irreversible cost,
- preventable versus uncontrollable factors.

Also briefly identify what would have to go right for success.

## 4. Reversibility

Classify:

- reversible,
- partly reversible,
- hard to reverse.

Increase evidence requirements as irreversibility rises.

## 5. Value of information

For major uncertainties ask:

- Can this be learned before deciding?
- What is the cheapest test?
- Would the answer change the decision?

Do not gather information that cannot affect the choice.

## Output

- decision frame,
- hidden options,
- criteria,
- option comparison,
- premortems,
- reversibility,
- value-of-information plan,
- decision trigger or deadline.

## Recommendation behavior

If asked to recommend:

1. state the criteria,
2. give the recommendation,
3. state confidence,
4. name the condition most likely to reverse it.

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
