# Contributing

Contributions are welcome.

## Before opening a pull request

Read:

- `AGENTS.md`
- `docs/SAFETY_MODEL.md`
- `docs/PRIVACY.md`
- `docs/SKILL_AUTHORING_GUIDE.md`

Then run:

```bash
make release-check
```

## Contribution types

Good contributions include:

- improved skill procedures,
- better counterexamples,
- additional synthetic eval cases,
- improved accessibility,
- research corrections,
- stronger privacy checks,
- portability improvements,
- documentation fixes.

## Public-data requirement

Do not contribute examples or wording copied from:

- private conversations,
- private journals,
- medical records,
- private email,
- private connected accounts,
- model memory about a real person,
- unpublished private repositories.

Examples must be synthetic or derived from clearly public material that can legally be reused.

If an example is based on a real situation, generalize it **before** submitting and remove all identifying details. Synthetic examples are preferred.

## Research contributions

For material claims:

1. cite the source,
2. state what it actually supports,
3. note major limitations,
4. avoid claiming more certainty than the evidence provides.

Prefer systematic reviews and meta-analyses when available.

## Pull requests

A pull request should explain:

- what changed,
- why,
- safety implications,
- privacy implications,
- evals added or changed,
- research sources changed, if any.

## Commit quality

Keep commits focused and descriptive.

Do not include secrets in commit messages, patches, examples, fixtures, or test data.

## Licensing

By contributing, you agree that your contribution is licensed under the repository's Apache License 2.0.
