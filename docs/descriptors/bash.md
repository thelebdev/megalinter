---
title: BASH linters in MegaLinter
description: bash-exec, shellcheck, shfmt are available to analyze BASH files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/bash.yml -->
# BASH

## Linters

| Linter                           | Configuration key                     | Status                                                                                                                                 |
|----------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [bash-exec](bash_bash_exec.md)   | [BASH_EXEC](bash_bash_exec.md)        |                                                                                                                                        |
| [shellcheck](bash_shellcheck.md) | [BASH_SHELLCHECK](bash_shellcheck.md) | [![GitHub last commit](https://img.shields.io/github/last-commit/koalaman/shellcheck)](https://github.com/koalaman/shellcheck/commits) |
| [shfmt](bash_shfmt.md)           | [BASH_SHFMT](bash_shfmt.md)           | [![GitHub last commit](https://img.shields.io/github/last-commit/mvdan/sh)](https://github.com/mvdan/sh/commits)                       |

## Linted files

- File extensions:
  - `.sh`
  - `.bash`
  - `.dash`
  - `.ksh`

## Configuration in MegaLinter

| Variable                  | Description                   | Default value |
|---------------------------|-------------------------------|---------------|
| BASH_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| BASH_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |


## Behind the scenes

### Installation

- APK packages (Linux):
  - [bash](https://pkgs.alpinelinux.org/packages?branch=edge&name=bash)
