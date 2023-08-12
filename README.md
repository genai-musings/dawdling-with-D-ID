# dawdling-with-D-ID

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Bandit](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/bandit.yml/badge.svg)](https://github.com/genai-musings/dawdling-with-D-ID/actions/new?category=security)
[![Super-Linter](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![CodeQL](https://github.com/genai-musings/dawdling-with-D-ID/workflows/CodeQL/badge.svg?branch=main)
[![Markdown Links Check](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/md-links.yml/badge.svg)](https://github.com/gaurav-nelson/github-action-markdown-link-check)
[![Spell-Checker](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/spellcheck.yaml/badge.svg)](https://github.com/rojopolis/spellcheck-github-actions)
[![Unit-Tests](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/test.yml/badge.svg)](https://github.com/actions/setup-python)
[![Code-Coverage](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/coverage.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Docker-Build-Push](https://github.com/genai-musings/dawdling-with-D-ID/actions/workflows/docker-build-push.yml/badge.svg)](https://hub.docker.com/)

Repository for dawdling with D-ID Studio.

 This repository contains Python code, and associated unit tests, which uses the D-ID Studio API to retrieve talks from an account.

## To run program

Your D-ID API key needs to be passed to program via an environment variable

```shell
export DID_KEY="Your DID Api key"
python main.py
```

To generate an D-ID key browse to [D-ID API Keys](https://studio.d-id.com/account-settings) and select "Generate key".

## Credits

You can generate talks using a trial account at [D-ID Studio](https://studio.d-id.com/). To generate talks you need credits, after the trial period expires you will need to purchase [D-ID Studio Credits](https://www.d-id.com/pricing/) to continue using the studio.

## To run unit tests

```shell
pytest
```

## To build and run an instance of a Docker image locally.

The username and password for Docker Hub are stored as secrets this GitHub repository.

**Note:** To set up the secrets in your GitHub repository, go to the repository page, navigate to the "Settings" tab, and then select "Secrets" from the left menu. Add a secret named DOCKERHUB_USERNAME with the Docker Hub username to be used, and another secret named DOCKERHUB_PASSWORD with the Docker Hub password to be used.

### Build

Build the Docker image.

```shell
docker build -t dawdling-with-d-id .
```

### Run

Run the Docker image as a container.

```shell
export DID_KEY="Your D-ID key"
docker run -it -e DID_KEY= "Your D-ID Key" dawdling-with-d-id
```

## To pull and run an instance of the Docker image from Docker Hub

### Pull

```shell
docker pull <dockerhub-username>/dawdling-with-d-id:<tag>
```

Replace <dockerhub-username> with your Docker Hub username and <tag> with the specific tag of the Docker image you want to pull.

### Run

```shell
export DID_KEY="Your D-ID key"
docker run -it -e DID_KEY= "Your D-ID Key" <dockerhub-username>/dawdling-with-d-id:<tag>
```

## D-ID Studio API Reference

For more information on the API available see the [D-ID Studio API Reference Documentation](https://docs.d-id.com/reference/get-started).
