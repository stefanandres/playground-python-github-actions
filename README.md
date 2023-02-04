# playground-python-github-actions

[![integration-test-deployment](https://github.com/stefanandres/playground-python-github-actions/actions/workflows/main.yaml/badge.svg)](https://github.com/stefanandres/playground-python-github-actions/actions/workflows/main.yaml)

This repository contains a very basic python app with very basic unit-testing.

The app is automatically unit-tested when submitting a pull request. When the PR is merged:
* App docker image will be build and pushed to ghcr as package
* Integration tests are run (very basic as well)
* A sample deployment command will be displayed

## Repo settings

### Protecting main branch

* Branch protection rules - Require status checks to pass before merging - Run unit-test
* Require a pull request before merging

## Local development

```shell
$EDITOR app.py

# Test-run app
make run

# Run unit-test
make test

# Run integration-test
make build
make integration
```

## Possible improvements

* Add dependabot/renovate to keep up with dependency management of Dockerfile and workflow includes
* Add workflow for tags to publish automatically tag for specific releases instead of just merges into main branch
