# Regression Test Runner (Python)

## Overview
Lightweight Python-based regression test framework that dynamically discovers test cases, executes them, and generates execution reports with timing and logging.

## Features
- Dynamic test discovery (auto-detects test modules)
- Executes test cases and tracks pass/fail status
- Measures execution time for each test
- CLI-based filtering to run specific tests
- Logs execution details for traceability
- Generates summary reports
- Modular and extensible design

## Project Structure
src/ → core logic (runner, reporter, utils),

tests/ → test cases,

main.py → entry point.


## How to Run
Run all tests:
python main.py,

Run specific test:
python main.py --filter login

### Example Use Case
- Execute regression test suites
- Identify failing test cases quickly
- Track execution performance

