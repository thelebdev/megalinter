---
title: CLOUDFORMATION linters in MegaLinter
description: cfn-lint is available to analyze CLOUDFORMATION files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/cloudformation.yml -->
# CLOUDFORMATION

## Linters

| Linter                                 | Configuration key                            | Status                                                                                                                                                 |
|----------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cfn-lint](cloudformation_cfn_lint.md) | [CLOUDFORMATION](cloudformation_cfn_lint.md) | [![GitHub last commit](https://img.shields.io/github/last-commit/aws-cloudformation/cfn-lint)](https://github.com/aws-cloudformation/cfn-lint/commits) |

## Linted files

- File extensions:
  - `.yml`
  - `.yaml`
  - `.json`

- Detected file content:
  - `AWSTemplateFormatVersion`
  - `(AWS|Alexa|Custom)::`

## Configuration in MegaLinter

| Variable                            | Description                   | Default value |
|-------------------------------------|-------------------------------|---------------|
| CLOUDFORMATION_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| CLOUDFORMATION_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |

