# CHANGELOG.md

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.0] - 2024-10-02

- [CHANGED] method to retrieve created talks
- [FIXED] upgraded version of upload-artifact in coverage workflow

## [1.7.0] - 2024-09-06

- [ADDED] Safety GitHub Action workflow to check Python dependencies for known security vulnerabilities.
- [ADDED] Trivy scan of the Docker image for vulnerabilities
- [FIXED] Vulnerabilities in docker images reported by Trivy
- [CHANGED] Updates to README.md

## [1.6.0] - 2023-10-19

- [ADDED] Talk creation from text and image URL feature
- [ADDED] Ensured docker image pushed to Docker Hub before README.md

## [1.5.2] - 2023-10-16

- [CHANGED] Updates to README.md
- [CHANGED] Updates to codeowners

## [1.5.1] - 2023-10-09

- [FIXED] Incorrect link in README.md

## [1.5.0] - 2023-10-08

- [ADDED] GitHub Action Linting to Super-Linter workflow
- [ADDED] Shell Script Linting to Super-Linter workflow
- [ADDED] Maintainer and description labels to Dockerfile
- [ADDED] Workflow to automatically update Image description on Docker Hub with contents of README.md
- [CHANGED] Updates to README.md.

## [1.4.1] - 2023-08-17

- [FIXED] Code scanning security error

## [1.4.0] - 2023-08-03

- [ADDED] Dockerized application.

## [1.3.0] - 2023-08-11

- [ADDED] CodeQL Security Action
- [ADDED] Bandit Security Action
- [ADDED] Code Coverage Action
- [ADDED] Dependabot check

## [1.2.0] - 2023-06-21

- [CHANGED] Migrated application to use Talks rather Animations API

## [1.1.0] - 2023-06-20

- [CHANGED] Fine tuned markdown link checker GitHub action triggers

## [1.0.0] - 2023-06-15

- [ADDED] Initial Release
