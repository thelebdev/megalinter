---
title: RUBY linters in MegaLinter
description: rubocop is available to analyze RUBY files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/ruby.yml -->
# RUBY

## Linters

| Linter                     | Configuration key       | Status                                                                                                                               |
|----------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [rubocop](ruby_rubocop.md) | [RUBY](ruby_rubocop.md) | [![GitHub last commit](https://img.shields.io/github/last-commit/rubocop-hq/rubocop)](https://github.com/rubocop-hq/rubocop/commits) |

## Linted files

- File extensions:
  - `.rb`

## Configuration in MegaLinter

| Variable                  | Description                   | Default value |
|---------------------------|-------------------------------|---------------|
| RUBY_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| RUBY_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |

