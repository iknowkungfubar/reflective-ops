.PHONY: validate privacy test release-check

validate:
	python3 scripts/validate_repo.py

privacy:
	python3 scripts/public_release_scan.py

test:
	python3 -m unittest discover -s tests -v

release-check: validate privacy test
