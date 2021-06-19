# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

## [Unreleased]

## [Released]

## [1.0.0] - 19 Jun 2021

### Added
- Documentation about Black and Flake8
- Extra rules into pre-commit

### Changed
- CLI version changed to 1.0.0

### Fixed
- Fixed 404 link in the documentation.

## [0.1.4] - 19 Jun 2021

### Change
- Applied Black
- Applied Flake8

## [0.1.3] - 19 Jun 2021

### Added
- pre-commit framework
- Black
- Flake8
- New field in the table of history 'domain'

### Change
- Documentation in history command.

### Removed
- Removed 'settings' command from the rdap layout. [WIP]

## [0.1.2] - 19 Jun 2021

### Added
- Limit history to max records (25) to avoid flooding with a big file.

### Fixed
- Wrong type hints used in get_record()
- Bugfix in save_file_data() - removed unused constant.

### Changed
- Modified logic when saving content into a file in gather command

## [0.1.1] - 18 Jun 2021

### Fixed
- Documentation links

## [0.1.0] - 18 Jun 2021

### Changed
- History command.
- Version command.
- Check command.
- Gather command.
- Rdap Service.
- Error handlers.
- Removed unused functions and constants.

### Fixed
- Fix lots of bugs and catched many exceptions.
- Fix typos in many docstrings.

### Added
- Domain Validators.
- File Validators.
- User guide.
- Commands documentation.
- Settings file.
- Version Command.
- Settings Command.
