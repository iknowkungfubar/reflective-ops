# Compatibility

ReflectiveOps uses the vendor-neutral Agent Skills format described at:

https://agentskills.io/specification

## Expected client behavior

A compatible client should be able to discover a skill from its `name` and `description`, then load the complete `SKILL.md` when activated.

## No required tools

ReflectiveOps skills do not require:

- shell access,
- filesystem write access,
- network access,
- external APIs,
- persistent memory.

A client may optionally provide tools, but the skill should not depend on them unless a future version explicitly declares that requirement.

## Installation

Installation locations differ by client and may change over time.

Use the current documentation for the AI client and place the desired ReflectiveOps skill directory in its supported Agent Skills location.

Do not rely on a hard-coded operating-system home path from this repository.

## Progressive disclosure

Install all skills if desired, but allow the client to load only the relevant skill instructions for each task.
