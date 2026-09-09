# Skill Authoring Guide

## Format

Each skill lives at:

```text
skills/<skill-name>/SKILL.md
```

The directory name must match the frontmatter `name`.

Required project frontmatter:

```yaml
---
name: example-skill
description: Explain what it does and when an agent should use it.
license: Apache-2.0
compatibility: Agent Skills-compatible clients; no network access required.
metadata:
  project: reflectiveops
  version: "1.0.0"
---
```

## Description quality

The `description` is discovery metadata.

It should state:

- the problem the skill solves,
- when to invoke it,
- important keywords a router may encounter.

Do not put a marketing slogan in place of activation guidance.

## Body design

Prefer:

1. objective,
2. invoke-when conditions,
3. procedure,
4. evidence rules,
5. output contract,
6. edge cases,
7. completion condition.

## Mandatory ReflectiveOps safety block

Every skill must explicitly enforce:

- no diagnosis,
- no invented hidden motives,
- separation of observations and interpretations,
- uncertainty labeling,
- user autonomy,
- no copying personal data into reusable artifacts.

## Interviewing

If the skill interviews the user:

- ask one question at a time,
- prioritize the question with the highest information value,
- prefer recent concrete examples,
- ask for exceptions,
- stop when enough evidence exists to test a model.

## Action design

Prefer:

- small,
- safe,
- reversible,
- measurable,
- time-bounded actions.

Avoid generating a large life plan simply because the model can.

## Examples

Examples must be synthetic.

Do not use real names.

## Evals

Behavior changes should add or update a case in `evals/cases.json`.

Good eval assertions test behavior such as:

- labels hypotheses,
- does not diagnose,
- asks for a concrete example,
- provides an experiment with a stop condition.

Avoid evals that depend on exact wording.
