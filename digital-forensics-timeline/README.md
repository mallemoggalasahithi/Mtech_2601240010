# Digital Forensics Timeline Builder

## 1. Project Overview

Digital Forensics Timeline Builder is a Python-based application that collects events from multiple forensic log files and creates a single chronological timeline.

The project helps investigators organize system, application, browser, and authentication events in one place. It uses sorting algorithms, multiprocessing, filtering techniques, and data export functionality to simplify forensic event analysis.

## 2. Problem Statement

Forensic information is often stored in different log files, with events recorded at different times and in different formats.

Manually arranging these events is time-consuming and can lead to errors. Investigators may also find it difficult to identify relevant activities across multiple sources.

This project automates the process by parsing multiple log files, combining their events, sorting them chronologically, filtering important events, searching for specific information, and exporting the final timeline.

## 3. Main Features

- Parse multiple forensic log files.
- Represent events using a structured data model.
- Combine events from different sources.
- Sort events using Merge Sort.
- Use multiprocessing for parallel processing.
- Filter events by user.
- Filter events by severity.
- Filter events by source.
- Filter events by event type.
- Search events using keywords.
- Export timelines to CSV format.
- Export timelines to JSON format.
- Provide a graphical user interface for timeline analysis.
- Support automated unit testing.
- Support property-based testing.
- Perform static type checking using mypy.
- Check code quality using Ruff.
- Measure performance using benchmarking.
- Support automated checks through GitHub Actions CI/CD.

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
│   ├── main.py
│   └── gui.py
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
```

*Note: The structure above represents the intended organization. Actual filenames should match the files present in the repository.*

## 5. Technologies Used

- **Python:** Main programming language.
- **Merge Sort:** Sorting events by timestamp.
- **Multiprocessing:** Processing event collections in parallel.
- **Tkinter:** Building the graphical user interface.
- **CSV and JSON:** Exporting timeline data.
- **Pytest:** Running automated tests.
- **Hypothesis:** Supporting property-based testing.
- **mypy:** Checking type annotations.
- **Ruff:** Checking code quality and style.
- **Git and GitHub:** Version control and source code hosting.
- **GitHub Actions:** Automating continuous integration checks.
- **Docker:** Supporting containerized execution when configured.

## 6. System Requirements

- Python 3.10 or a compatible version supported by the project dependencies.
- Windows, Linux, or another compatible operating system.
- Git for version control.
- A code editor such as Visual Studio Code.
- Required Python packages listed in `requirements.txt`.

Docker is optional for running the application directly with Python, unless a particular workflow requires it.

## 7. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/mallemoggalasahithi/Mtech_2601240010.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Mtech_2601240010/digital-forensics-timeline
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS:**

```bash
source .venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## 8. Running the Application

From the project root directory, execute:

```bash
python -m src.main
```

The application reads the configured forensic log files, processes the events, and generates a chronological timeline.

For the graphical interface, if the GUI module is available, run:

```bash
python -m src.gui
```

The exact command and required input files depend on the project's implementation.

## 9. Working Methodology

The project follows these main steps:

1. **Input collection:** Load events from system, application, browser, and authentication logs.
2. **Parsing:** Read the log entries and convert them into structured event objects.
3. **Normalization:** Prepare event fields, including timestamps and source information, for consistent processing.
4. **Event combination:** Combine parsed events from all configured sources.
5. **Chronological sorting:** Arrange events by timestamp using Merge Sort.
6. **Parallel processing:** Use multiprocessing where appropriate to process event collections.
7. **Filtering:** Narrow down events based on severity, user, source, or event type.
8. **Searching:** Find events containing specified keywords.
9. **Exporting:** Save the resulting timeline in CSV or JSON format.
10. **Validation:** Run automated tests and code-quality checks.

## 10. Algorithms and Computational Concepts

### 10.1 Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm. It divides the input into smaller parts, sorts those parts recursively, and merges them into a sorted sequence.

In this project, Merge Sort is used to arrange forensic events chronologically according to their timestamps.

Its typical time complexity is:

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n log n)

Its auxiliary space complexity for a standard array-based implementation is generally O(n).

### 10.2 Multiprocessing

Multiprocessing allows independent work to be performed by multiple processes. The project uses multiprocessing for parallel processing of event collections where appropriate.

The actual performance improvement depends on dataset size, process overhead, and the implementation.

### 10.3 Filtering and Searching

Filtering allows investigators to focus on relevant records by applying criteria such as user, severity, source, or event type.

Keyword searching helps locate specific terms or activities within the timeline.

## 11. Testing and Quality Assurance

Testing helps verify that the application processes and sorts forensic events correctly.

The project supports the following quality checks:

- **Unit testing:** Checks individual components such as parsers, sorting algorithms, filters, and exporters.
- **Property-based testing:** Tests sorting behavior against defined properties across generated inputs.
- **Static type checking:** Uses mypy to identify type-related issues.
- **Code-quality checking:** Uses Ruff to identify style and linting problems.
- **Performance benchmarking:** Measures execution performance for selected workloads.
- **Continuous integration:** Uses GitHub Actions to automate configured checks.

Run the test suite from the project root:

```bash
pytest
```

Run static type checking if mypy is installed and configured:

```bash
mypy src
```

Run Ruff checks if Ruff is installed and configured:

```bash
ruff check .
```

The reported results depend on the current source code, installed dependencies, and test configuration.

## 12. Performance Analysis

The application uses Merge Sort to maintain chronological ordering of forensic events. For n events, a standard Merge Sort implementation has O(n log n) time complexity.

Multiprocessing may improve throughput for sufficiently large workloads, but it also introduces process creation, data transfer, and coordination overhead.

Performance benchmarking can compare sequential and parallel processing using consistent input datasets. Meaningful comparisons should record the dataset size, execution time, and test environment.

No specific performance improvement is claimed without measured benchmark results.

## 13. Applications

Digital Forensics Timeline Builder can support:

- Organizing system activity records.
- Reviewing application event histories.
- Examining browser activity logs.
- Reviewing authentication events.
- Searching for events associated with a particular user.
- Identifying events by severity or source.
- Preparing chronological records for further forensic investigation.
- Exporting organized event data for reporting and analysis.

The tool organizes supplied log data; it does not independently establish whether an event represents malicious activity or prove that a log entry is authentic.

## 14. Limitations

- The quality of the timeline depends on the input log format and available timestamps.
- Unsupported or malformed log entries may require additional parser handling.
- Different systems may use different time zones or timestamp formats.
- Multiprocessing benefits depend on the workload and system resources.
- Results should be reviewed in context before drawing forensic conclusions.
- The application processes the log sources configured in the project; additional formats may require new parsers.

## 15. Future Enhancements

Potential improvements include:

- Supporting additional forensic log formats.
- Improving timestamp normalization and time-zone handling.
- Adding more advanced search and filtering options.
- Improving the GUI with timeline visualizations.
- Adding more detailed event summaries and reports.
- Comparing sequential and parallel performance on larger datasets.
- Expanding test coverage for malformed and unusual log entries.
- Improving deployment and reproducibility through containerization.
- Enhancing documentation and usage examples.

## 16. Conclusion

Digital Forensics Timeline Builder provides a structured way to collect and organize events from multiple forensic log files into a chronological timeline.

By combining log parsing, Merge Sort, multiprocessing, filtering, keyword searching, and CSV/JSON exporting, the application reduces the effort required to organize forensic records.

Automated tests, static type checking, code-quality checks, performance benchmarking, and continuous integration help improve maintainability and reliability.

The project demonstrates how Python programming and computational-thinking concepts can be applied to forensic log organization and timeline analysis.
