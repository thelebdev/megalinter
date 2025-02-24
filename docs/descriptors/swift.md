---
title: SWIFT linters in MegaLinter
description: swiftlint is available to analyze SWIFT files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/swift.yml -->
# SWIFT

## Linters

| Linter                          | Configuration key           | Status                                                                                                                         |
|---------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [swiftlint](swift_swiftlint.md) | [SWIFT](swift_swiftlint.md) | [![GitHub last commit](https://img.shields.io/github/last-commit/realm/SwiftLint)](https://github.com/realm/SwiftLint/commits) |

## Linted files

- File extensions:
  - `.swift`

## Configuration in MegaLinter

| Variable                   | Description                   | Default value |
|----------------------------|-------------------------------|---------------|
| SWIFT_FILTER_REGEX_INCLUDE | Custom regex including filter |               |
| SWIFT_FILTER_REGEX_EXCLUDE | Custom regex excluding filter |               |

