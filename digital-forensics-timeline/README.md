# Digital Forensics Timeline Builder

## 1. Project Overview

Digital Forensics Timeline Builder is a Python-based application that
collects events from multiple forensic log files and creates a single
chronological timeline.

The project helps investigators organize system, application, browser,
and authentication events in one place.

## 2. Problem Statement

Forensic information is often stored in different log files with events
recorded at different times.

Manually arranging these events is time-consuming and can lead to errors.

This project automates the process by parsing multiple log files,
combining their events, sorting them chronologically, filtering important
events, and exporting the final timeline.

## 3. Main Features

- Parse multiple forensic log files
- Represent events using a structured data model
- Combine events from different sources
- Sort events using Merge Sort
- Use multiprocessing for parallel sorting
- Filter events by user
- Filter events by severity
- Filter events by source
- Filter events by event type
- Search events using keywords
- Export timeline to CSV
- Export timeline to JSON
- Automated unit testing
- Property-based testing
- Static type checking with mypy
- Code quality checking with Ruff
- Performance benchmarking
- GitHub Actions CI/CD

## 4. Project Structure

```text
digital-forensics-timeline/
│
├── data/
│   ├── system.log
│   ├── application.log
│   ├── browser.log
│   └── auth.log
│
├── src/
│   ├── models.py
│   ├── parsers.py
│   ├── merge_sort.py
│   ├── multiprocessing_sort.py
│   ├── timeline.py
│   ├── filters.py
│   ├── exporters.py
│   └── main.py
│
├── tests/
│   ├── test_merge_sort.py
│   ├── test_parsers.py
│   ├── test_timeline.py
│   ├── test_multiprocessing_sort.py
│   ├── test_parallel_timeline.py
│   ├── test_filters.py
│   ├── test_exporters.py
│   └── test_property_sort.py
│
├── benchmarks/
│   └── benchmark.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
└── README.md