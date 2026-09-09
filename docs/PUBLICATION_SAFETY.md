# Publication Safety

The repository includes `scripts/public_release_scan.py`, which checks for common secret and personal-data patterns.

It cannot prove that a repository is private-data-free. Human review remains necessary.

## Standard check

```bash
make release-check
```

## Private local denylist

Before publishing material developed in a private workspace, a maintainer may run an additional local scan against private terms that must never appear publicly.

Create a denylist **outside the repository** with one literal term per line, then set:

```text
REFLECTIVEOPS_PRIVATE_DENYLIST=<path-to-local-file>
```

and run:

```bash
python3 scripts/public_release_scan.py
```

The denylist file itself must never be committed.

Useful private denylist entries may include, for example:

- private usernames,
- private hostnames,
- private repository names,
- personal names,
- private domains,
- internal project codenames.

Do not document the actual values in the public repository.

## Before release

Review:

- git diff,
- git status,
- commit history being published,
- examples,
- fixtures,
- screenshots,
- workflow logs,
- generated archives.

A clean working tree does not guarantee that earlier commits are safe. If sensitive data ever entered Git history, follow GitHub's current secret-removal guidance rather than merely deleting it in a later commit.
