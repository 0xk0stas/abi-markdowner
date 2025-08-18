# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.16] - 2025-08-18

### Changed
- Migrated from setup.py to pyproject.toml for modern Python packaging
- Moved pytest from runtime to development dependencies
- Renamed LICENCE to LICENSE for standard convention
- Added comprehensive test suite with 10 meaningful tests
- Added MANIFEST.in for proper package distribution
- Added pytest configuration and coverage settings
- Improved project metadata and classifiers

### Added
- CHANGELOG.md following Keep a Changelog format
- Development dependencies configuration
- Code coverage configuration
- Enhanced test suite covering core functionality

## [0.1.15] - 2024-XX-XX

### Added
- Initial release of abi-markdowner
- Convert MultiversX Smart Contract ABI files to Markdown documentation
- Support for endpoints, views, events, and types
- Matrix-style input/output tables
- Automatic Table of Contents generation
- Deployment links support via deployments.json
- Command-line interface with customizable parameters

### Features
- **Convert ABI to Markdown:** Generates comprehensive Markdown documentation from smart contract ABI files
- **Customizable Output:** Organizes endpoints, views, events, and types with formatted tables
- **Matrix-Style Input/Output Tables:** Clear formatting with support for optional and multi-value parameters
- **Automatic Table of Contents:** Includes a TOC for easy navigation
- **Deployment Links:** Supports multiple mainnet and devnet addresses with customizable labels
