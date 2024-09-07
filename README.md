# JamieLiu-Mini1

[![CI](https://github.com/nogibjj/JamieLiu-Mini1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/JamieLiu-Mini1/actions/workflows/hello.yml)

## Python GitHub Template

This repository provides a template for a Python project with a complete development setup, including a Devcontainer, Makefile, CI/CD with GitHub Actions, and dependency management.

## Features

- `.devcontainer` configuration for a consistent Python development environment using Docker.
- **Makefile** to streamline common tasks like setup, testing, linting.
- **GitHub Actions** for automated CI/CD pipeline (testing, linting, and deployment).
- `requirements.txt` for managing Python dependencies.

## Usage

1. **Clone the repository:**
   ```bash
   git clone git@github.com:nogibjj/JamieLiu-Mini1.git
   ```
2. **Install project dependencies:**
   ```bash
   make install
   ```
3. **Format the code:**
   ```bash
   make format
   ```
4. **Run linting checks:**
   ```bash
   make lint
   ```
5. **Run tests:**
   ```bash
   make test
   ```
6. **Run all steps (Install, Format, Lint, Test):**
   ```bash
   make all
   ```
