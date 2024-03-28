# Template repo for Python SDK  
This template helps developers get started with publishing the Python SDK to PyPI Registry.

## Prerequisites
The user will need the following:

- An account with PyPI Registry with an API token that can upload packages into the desired project

## Contents
This repository contains the following:

- A `README` that contains the instructions
- A GitHub Action workflow to publish the Python SDK to PyPI Registry.


## Instructions

1. Create a new target Python SDK Repo by clicking the **Use this template** button at the top of this repository.

2. Set the PyPI Registry's account Username as an actions secret `PYPI_USERNAME` and set the PyPI Registry's API token as an actions secret `PYPI_PASSWORD` in the target SDK Repo.

3. Run the GitHub Action `Generate SDKs using liblab` in the Control Repo that builds the SDK, and raises a PR against this target SDK Repo.

4. Review and merge the PR.

5. Create a release in the target SDK Repo.

6. The GitHub Action `Publish to PyPI Registry` in the target SDK Repo publishes the package to PyPI registry.
