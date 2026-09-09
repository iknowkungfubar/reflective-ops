---
name: baseline-mapper
description: Build a compact current-state map when a user feels stuck, overwhelmed, or unsure where to start; identify one high-leverage bottleneck and a baseline measure.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access or external tools required.
metadata:
  project: reflectiveops
  version: "1.1.0"
---


# Baseline Mapper

## Objective

Build a compact current-state map and select one high-leverage target.

## Invoke when

- the user feels broadly stuck or overwhelmed,
- several areas compete for attention,
- priorities are unclear.

## Candidate domains

Use only relevant domains:

- physical functioning and energy,
- work or study,
- finances,
- relationships and social support,
- home and environment,
- obligations and administration,
- learning,
- recreation and recovery,
- values and direction.

## For each relevant domain collect

- current condition,
- urgent threat,
- one observable indicator,
- controllability,
- energy cost,
- leverage on other domains,
- one thing already working.

Do not require numeric scoring when it creates false precision.

## Prioritization

Compare candidate bottlenecks on:

1. urgency,
2. leverage,
3. controllability,
4. feasibility,
5. reversibility,
6. evidence that it is actually a bottleneck.

## Interview

Ask one question at a time.

Start with:
> If one area became noticeably better over the next month, which improvement would make other problems easier?

Then test it:
- What is currently breaking because of this?
- What is the cost of waiting?
- What would “noticeably better” look like?
- What constraint makes action hard?
- Where is there already an exception or foothold?

## Output

### Baseline
Compact view of relevant domains.

### Primary bottleneck
One target with rationale.

### Deferred
One to three items intentionally not addressed yet.

### Baseline metric
One or two measures.

### Next route
One specialist skill.

## Completion

The user has one primary target rather than a total-life overhaul.

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
