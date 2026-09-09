---
name: life-systems-orchestrator
description: Route broad self-reflection, life-management, behavior, decision, conflict, transition, or debriefing requests to the smallest appropriate ReflectiveOps specialist skill.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.0.0"
---


# Life Systems Orchestrator

## Objective

Route a broad self-reflection or life-management concern to the **smallest appropriate specialist process**.

## Invoke when

- the user's problem is broad,
- several life domains are entangled,
- the correct specialist is unclear,
- a previous skill has completed and a next route is needed.

## Routing table

| Need | Route |
|---|---|
| “Where do I start?” | `baseline-mapper` |
| Repeated unwanted behavior | `behavior-forensics` |
| Belief or story needs reality testing | `belief-reality-auditor` |
| Conflict or difficult conversation | `conflict-perspective-lab` |
| Role/career/life transition | `identity-transition-cartographer` |
| Consequential fork | `decision-lab` |
| Setback, rejection, loss, or betrayal | `adversity-debrief` |
| Ambivalent about change | `change-readiness-interviewer` |
| Goal chosen; execution is the problem | `behavior-change-engineer` |
| Important uncertainty can be tested | `experiment-designer` |
| Real outcome data exists | `review-calibration` |

## Procedure

1. Restate the working problem neutrally in one sentence.
2. Classify the primary bottleneck:
   - clarity,
   - belief,
   - behavior,
   - relationship,
   - identity,
   - decision,
   - adversity,
   - ambivalence,
   - execution,
   - review.
3. If two routes fit, choose the route that can reduce the most important uncertainty first.
4. State the selected route and why.
5. Use only that specialist process.
6. Route to `experiment-designer` or `review-calibration` when real-world testing becomes appropriate.

## Avoid

- running all skills at once,
- generating a complete “life diagnosis,”
- interpreting every problem as a cognitive distortion,
- creating a giant plan before identifying the bottleneck.

## Completion

One primary target and one specialist process are selected.

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
