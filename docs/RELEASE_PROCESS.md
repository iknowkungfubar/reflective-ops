# Release Process

## Versioning

ReflectiveOps uses semantic versioning.

- **PATCH** — wording, documentation, research citation, or behavior fix without a new public capability.
- **MINOR** — new skill or backward-compatible capability.
- **MAJOR** — incompatible skill contracts, safety-model changes requiring migration, or major structure changes.

## Pre-release

1. Update `VERSION`.
2. Update skill metadata versions if behavior changed.
3. Update `CHANGELOG.md`.
4. Review research claims.
5. Run:

```bash
make release-check
```

6. Run a private local denylist scan when the release originated from a private workspace.
7. Inspect the archive contents before publishing.
8. Verify the repository has no unexpected symlinks or generated files.

## GitHub settings

Before a public release, confirm repository security features are enabled where available.

## Release notes

Release notes should include:

- new or changed skills,
- safety changes,
- compatibility changes,
- important evidence updates,
- known limitations.
