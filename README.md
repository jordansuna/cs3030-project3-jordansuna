# Project 3: DevOps CI/CD Health Monitor

**Module 3 Integration Project**  
**Total Points: 145**

---

## 📚 Learning Objectives

This project integrates all Module 3 Python concepts into a professional DevOps monitoring tool:

### Technical Skills (Module 3A - File I/O & System Interaction)
- **File Operations:** Read configuration files, process logs, write reports  
- **CSV/JSON Processing:** Parse CI/CD pipeline data and metrics  
- **pathlib:** Cross-platform file and directory operations  
- **subprocess:** Execute system commands and process output  
- **argparse:** Professional command-line interface

### Professional Skills (Module 3B - Exception Handling & Robustness)
- **Exception Handling:** Defensive programming with try-except patterns  
- **Error Recovery:** Retry logic and graceful degradation  
- **Logging:** Structured logging for troubleshooting  
- **Custom Exceptions:** Domain-specific error handling

### Industry Skills
- **Git Workflow:** Feature branches and professional commits  
- **Testing:** Automated testing with pytest  
- **Documentation:** Clear README and inline documentation  
- **Real-world Application:** Monitor CI/CD pipeline health

---

## 🎯 Project Overview

You will build `ci_health_monitor.py`, a DevOps automation tool that:

1. **Monitors Pipeline Status** - Reads GitHub Actions/Jenkins/GitLab CI logs  
2. **Analyzes Build Metrics** - Calculates success rates, average duration, failure patterns  
3. **Detects Anomalies** - Identifies slow builds, flaky tests, and infrastructure issues  
4. **Generates Reports** - Creates JSON/CSV reports and human-readable summaries  
5. **Sends Alerts** - Simulates alert dispatch for critical issues

**Real-world Application:** DevOps teams use CI/CD health monitoring to maintain fast, reliable deployment pipelines. This tool simulates monitoring GitHub Actions workflows, detecting problems like flaky tests, slow builds, and infrastructure failures - critical skills for Site Reliability Engineers (SREs) and DevOps engineers.

**Industry Context:**
- Companies lose thousands of dollars per hour when CI/CD pipelines fail
- Netflix, Google, Amazon monitor pipeline health 24/7
- SRE teams respond to pipeline alerts using automated monitoring
- This project simulates real observability workflows

---

## ⏱️ Time Commitment & Checkpoint Guide

**Estimated Time:** 10-14 hours over 12 days

**Recommended Schedule:**

| Day | Checkpoint | Time | What to Complete |
|-----|------------|------|------------------|
| **Day 1** | Setup & Configuration | 2-3 hrs | Setup project, implement Part 1 (config loading), understand data format |
| **Day 2** | Data Processing | 3-4 hrs | Implement Part 2 (parse logs), Part 3 (calculate metrics) |
| **Day 3** | Analysis & Detection | 3-4 hrs | Implement Part 4 (anomaly detection), Part 5 (report generation) |
| **Day 4** | Integration & Testing | 2-3 hrs | Implement Part 6 (main/CLI), run pytest, debug issues |
| **Day 5** | Git Workflow | 1-2 hrs | Verify branch history, clean commit messages |
| **Day 6** | Video & Submit | 1-2 hrs | Record walkthrough video, final testing, submission |

**💡 Pro Tip:** This project is more complex than Project 2. Start Day 1, test frequently, commit often!

**Minimum Viable Product (MVP):**
- ✅ All 6 parts implemented and working  
- ✅ Proper exception handling (try-except in all file operations)  
- ✅ 4+ Git branches with 10+ commits  
- ✅ Pass at least 80% of pytest tests  
- ✅ Video walkthrough demonstrating functionality

**Bonus Features** (implement AFTER MVP is complete):
- 🌟 Email alert simulation (+5 points)  
- 🌟 Trending analysis (compare current vs historical metrics) (+5 points)  
- 🌟 HTML report generation (+5 points)  
- 🌟 GitHub API integration (fetch real workflow data) (+10 points)

---

## 💡 Getting Started

### Step 1: Clone Your Repository (5 minutes)
```bash
# Navigate to your CS3030 folder
cd ~/cs3030

# Clone your project3 repository using GitHub CLI
gh repo clone project3/<your-username>

# Example: gh repo clone project3/jsmith

# Navigate into the project
cd project3

# Verify files are present
ls -la
# You should see: ci_health_monitor.py, sample_data/, tests/, config.json, etc.
```

### Step 2: Understand the Data Format (15 minutes)

```bash
# Examine sample CI/CD pipeline data
cat sample_data/github_actions_runs.json

# Look at the structure:
# - workflow_runs: list of build executions
# - Each run has: id, status, conclusion, duration, timestamp, test_results

# Examine configuration
cat config.json
# Defines thresholds: max_duration, min_success_rate, alert recipients

# Examine sample logs
cat sample_data/build_logs/build_12345.log
# Contains build output, test results, error messages
```

**Understanding the Data:**
```json
{
  "workflow_runs": [
    {
      "id": 12345,
      "workflow": "main-ci",
      "status": "completed",
      "conclusion": "success",
      "duration_seconds": 342,
      "timestamp": "2026-02-01T10:30:00Z",
      "test_results": {
        "total": 145,
        "passed": 148,
        "failed": 2,
        "skipped": 0
      },
      "log_file": "sample_data/build_logs/build_12345.log"
    }
  ]
}
```

### Step 3: Read the Template (20 minutes)
```bash
# Open the starter code
code ci_health_monitor.py
# Or: vim ci_health_monitor.py
```

Look for TODO comments:
```python
# TODO 1: Implement load_config() - Load and validate config.json (15 pts) - Est: 1-1.5 hrs
# TODO 2: Implement parse_pipeline_data() - Parse JSON workflow data (20 pts) - Est: 2-2.5 hrs
# TODO 3: Implement calculate_metrics() - Compute success rates, duration stats (20 pts) - Est: 2-3 hrs
# TODO 4: Implement detect_anomalies() - Identify problems (25 pts) - Est: 2.5-3 hrs
# TODO 5: Implement generate_report() - Create JSON/CSV reports (20 pts) - Est: 1.5-2 hrs
# TODO 6: Implement main() - CLI interface with argparse (15 pts) - Est: 1-1.5 hrs
```

### Step 4: Implement Feature by Feature

**Recommended Order:**

1. **Part 1: load_config** (easiest - 1-1.5 hours)
   - Read JSON file with error handling
   - Validate required keys exist
   - Return config dictionary
   - Good warm-up for JSON processing!

2. **Part 2: parse_pipeline_data** (moderate - 2-2.5 hours)
   - Read JSON pipeline data
   - Filter by date range (optional parameter)
   - Return structured data
   - Practice pathlib + JSON + error handling

3. **Part 3: calculate_metrics** (moderate - 2-3 hours)
   - Success rate calculation
   - Average/median duration
   - Test pass rate aggregation
   - Dictionary and list comprehension practice

4. **Part 4: detect_anomalies** (challenging - 2.5-3 hours)
   - Compare metrics against thresholds
   - Detect slow builds, flaky tests, failures
   - Return anomaly list with details
   - Most complex logic - needs good testing!

5. **Part 5: generate_report** (moderate - 1.5-2 hours)
   - Write JSON report file
   - Write CSV summary
   - Format human-readable output
   - Multiple file operations

6. **Part 6: main** (straightforward - 1-1.5 hours)
   - argparse setup (data_file positional, --config, --output, --verbose)
   - Orchestrate function calls
   - Handle exceptions at top level
   - Ties everything together!

### Step 5: The Development Loop (Repeat for Each Function)

**🔄 Integrated Workflow: Code → Test → Commit**

```bash
# 1. Create feature branch (2 min)
git checkout -b feature/config-loader

# 2. Code for 20-30 minutes
vim ci_health_monitor.py
# Implement ONE sub-task (e.g., "read JSON file")

# 3. Test immediately with Python REPL (2 min)
python3
>>> from ci_health_monitor import load_config
>>> config = load_config('config.json')
>>> print(config)
# Does it work? If not, fix and test again

# Or run the script:
./ci_health_monitor.py --help

# 4. Commit when working (1 min)
git add ci_health_monitor.py
git commit -m "Add JSON config file loading"

# 5. Continue coding next sub-task
# Implement next piece (e.g., "validate required keys")

# 6. Test again
python3 -c "from ci_health_monitor import load_config; print(load_config('config.json'))"

# 7. Commit again
git commit -am "Add config validation for required keys"

# Repeat until function is complete...

# 8. Run automated tests (3 min)
pytest tests/test_config.py -v

# 9. Merge to main (2 min)
git checkout main
git merge feature/config-loader
```

**Why This Workflow Matters:**
- ✅ **Small commits = easier debugging** - Pinpoint exactly what changed  
- ✅ **Frequent testing = catch errors early** - Don't wait until the end  
- ✅ **Real Python development** - This is professional workflow  
- ✅ **Natural Git history** - Your commits tell your development story

**🚫 Anti-Pattern (Don't Do This):**
```bash
# ❌ Write all 600 lines of code without testing
# ❌ Test once at the end - everything broken
# ❌ Try to fix 50 errors at once
# ❌ Make one commit: "finished project"
# ❌ Panic at 2am before deadline
```

### Step 6: Test and Debug (Ongoing)
```bash
# Run all tests
pytest tests/ -v

# Run tests for specific module
pytest tests/test_metrics.py -v

# Run with coverage report
pytest tests/ --cov=ci_health_monitor --cov-report=html

# Calculate your current score
python3 calculate_score.py

# Test manually with sample data
./ci_health_monitor.py sample_data/github_actions_runs.json --output report.json

# Fix issues, commit, repeat
```

### Step 7: Generate Submission Files (10 minutes)
```bash
# Generate branch history
git log --graph --oneline --all --decorate > branch_history.txt
git add branch_history.txt
git commit -m "Add branch history for submission"

# Push to GitHub
git push origin main

# Verify on GitHub.com:
# - All commits visible
# - Actions tab shows pytest passing
# - branch_history.txt present
```

### Step 8: Record Video Walkthrough (10-12 minutes)

See "Video Walkthrough" section below for detailed guidance.

---

## 🏗️ Project Structure

```
project3/
├── .github/                      # GitHub Actions configuration
│   ├── workflows/
│   │   └── autograding.yml       # Auto-grading workflow
│   └── scripts/
│       └── check_instructor_token.sh  # Token validation script
├── ci_health_monitor.py          # Your implementation (submit this)
├── config.json                   # Configuration file (provided)
├── requirements.txt              # Python dependencies (provided)
├── docs/                         # Project documentation
│   └── CI_CD_GUIDE.md            # Comprehensive CI/CD workflow guide
├── README.md                     # This file
├── sample_data/                  # Test data (provided)
│   ├── github_actions_runs.json  # Sample pipeline data
│   └── build_logs/               # Individual build logs
└── reports/                      # Generated reports directory
    └── health_report.json        # Sample output report
```

**Note:** Tests and grading scripts are NOT included in the student repository. When you push your code, the GitHub Actions workflow automatically fetches private test files from the instructor repository and runs them against your code.

**📘 Need help understanding the auto-grading workflow?** See the comprehensive [CI/CD Auto-Grading Guide](docs/CI_CD_GUIDE.md) for detailed information about:
- How automated testing works
- Viewing test results and scores
- Understanding workflow triggers
- Troubleshooting common issues
- Best practices for development workflow

---

## 📋 Requirements

### Part 1: Configuration Loader (15 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/config-loader
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/config-loader
git push origin main
```

---

**Function:** `load_config(config_file: str) -> dict`

Load and validate configuration from JSON file.

**Requirements:**
- ✅ Read JSON configuration file using pathlib and json module  
- ✅ Validate required keys exist: `thresholds`, `alert_config`  
- ✅ Handle FileNotFoundError with clear error message  
- ✅ Handle json.JSONDecodeError for invalid JSON  
- ✅ Return config dictionary with validated structure  
- ✅ Raise custom ConfigurationError for validation failures

**Example Usage:**
```python
config = load_config('config.json')
print(config['thresholds']['max_duration_seconds'])
# Output: 600

# Error handling example:
try:
    config = load_config('missing.json')
except ConfigurationError as e:
    print(f"Config error: {e}")
# Output: Config error: Configuration file not found: missing.json
```

**Configuration Structure:**
```json
{
  "thresholds": {
    "max_duration_seconds": 600,
    "min_success_rate": 0.95,
    "max_failure_streak": 3,
    "test_pass_rate_threshold": 0.98
  },
  "alert_config": {
    "enabled": true,
    "recipients": ["team@company.com"],
    "severity_levels": ["critical", "warning"]
  },
  "monitoring": {
    "lookback_days": 7,
    "exclude_workflows": ["nightly-tests"]
  }
}
```

**Implementation Approach:**

**Algorithm (Pseudocode):**
```
1. Convert config_file string to Path object
2. IF file does not exist:
     RAISE ConfigurationError with message
3. TRY:
     Open file for reading
     Parse JSON content
   EXCEPT JSONDecodeError:
     RAISE ConfigurationError with parse error details
4. FOR each required_key in ['thresholds', 'alert_config']:
     IF key not in parsed_config:
       RAISE ConfigurationError for missing key
5. RETURN validated config dictionary
```

**Key Python Concepts:**
- `pathlib.Path` for file path handling
- `Path.exists()` method to check file presence
- `with open()` context manager for file handling
- `json.load(f)` to parse JSON from file object
- `try-except` to catch `json.JSONDecodeError`
- Custom exception raising: `raise ConfigurationError("message")`
- Dictionary key checking: `if 'key' not in dict:`

**Starter Structure:**
```python
def load_config(config_file: str) -> dict:
    # 1. Create Path object
    # 2. Check existence
    # 3. Try to open and parse
    # 4. Validate keys
    # 5. Return config
    pass
```

---

### Part 2: Pipeline Data Parser (15 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/pipeline-parser
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/pipeline-parser
git push origin main
```

---

**Function:** `parse_pipeline_data(data_file: str, start_date: str = None, end_date: str = None) -> list`

Parse CI/CD pipeline run data from JSON file with optional date filtering.

**Requirements:**
- ✅ Read JSON file containing workflow runs using pathlib  
- ✅ Parse ISO 8601 timestamps (2026-02-01T10:30:00Z)  
- ✅ Filter runs by date range if provided (optional)  
- ✅ Handle missing or malformed JSON gracefully  
- ✅ Validate required fields exist in each run  
- ✅ Return list of validated workflow run dictionaries  
- ✅ Raise DataParsingError for invalid data

**Example Usage:**
```python
# Parse all runs
runs = parse_pipeline_data('sample_data/github_actions_runs.json')
print(f"Found {len(runs)} workflow runs")
# Output: Found 46 workflow runs

# Filter by date range
runs = parse_pipeline_data(
    'sample_data/github_actions_runs.json',
    start_date='2026-02-01',
    end_date='2026-02-07'
)
print(f"Found {len(runs)} runs in date range")
# Output: Found 28 runs in date range

# Examine run structure
print(runs[0])
# Output: {
#   'id': 12345,
#   'workflow': 'main-ci',
#   'status': 'completed',
#   'conclusion': 'success',
#   'duration_seconds': 342,
#   'timestamp': '2026-02-01T10:30:00Z',
#   'test_results': {'total': 145, 'passed': 148, 'failed': 2, 'skipped': 0}
# }
```

**Data Format:**
```json
{
  "workflow_runs": [
    {
      "id": 12345,
      "workflow": "main-ci",
      "status": "completed",
      "conclusion": "success",
      "duration_seconds": 342,
      "timestamp": "2026-02-01T10:30:00Z",
      "test_results": {
        "total": 145,
        "passed": 148,
        "failed": 2,
        "skipped": 0
      },
      "log_file": "sample_data/build_logs/build_12345.log"
    }
  ]
}
```

**Implementation Approach:**

**Algorithm (Pseudocode):**
```
1. Read and parse JSON file (similar to Part 1)
2. Extract 'workflow_runs' list from data dictionary
3. IF start_date OR end_date provided:
     Initialize filtered_list as empty
     FOR each run in runs:
       Parse run's timestamp to datetime object
       IF run date is within range:
         Add run to filtered_list
     SET runs = filtered_list
4. FOR each run in runs:
     FOR each required_field in ['id', 'workflow', 'conclusion', ...]:
       IF field missing:
         RAISE DataParsingError
5. RETURN validated runs list
```

**Date Filtering Logic:**
```
run_timestamp = '2026-02-01T10:30:00Z'
Parse to datetime: use datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
Compare: if start_date provided and run_date < parse(start_date): skip
Compare: if end_date provided and run_date > parse(end_date): skip
```

**Key Python Concepts:**
- `datetime.fromisoformat()` for parsing ISO 8601 dates
- String replace: `timestamp.replace('Z', '+00:00')` for timezone
- Dictionary `.get()` method with default value
- List comprehension or filtering with loops
- Datetime comparison operators (`<`, `>`)

**Required Fields to Validate:**
`['id', 'workflow', 'conclusion', 'duration_seconds', 'timestamp']`

---

### Part 3: Metrics Calculator (20 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/metrics-calculator
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/metrics-calculator
git push origin main
```

---

**Function:** `calculate_metrics(runs: list) -> dict`

Calculate CI/CD pipeline health metrics from workflow run data.

**Requirements:**
- ✅ Calculate overall success rate (successful runs / total runs)  
- ✅ Calculate average and median build duration  
- ✅ Calculate test pass rate across all runs  
- ✅ Identify slowest and fastest builds  
- ✅ Count failures by workflow type  
- ✅ Calculate metrics per workflow (breakdown)  
- ✅ Handle empty run list gracefully  
- ✅ Return structured metrics dictionary

**Example Usage:**
```python
runs = parse_pipeline_data('sample_data/github_actions_runs.json')
metrics = calculate_metrics(runs)

print(f"Success Rate: {metrics['success_rate']:.2%}")
# Output: Success Rate: 86.96%

print(f"Average Duration: {metrics['avg_duration']:.1f}s")
# Output: Average Duration: 386.3s

print(f"Test Pass Rate: {metrics['test_pass_rate']:.2%}")
# Output: Test Pass Rate: 98.84%

# Examine full metrics
import json
print(json.dumps(metrics, indent=2))
```

**Expected Metrics Structure:**
```json
{
  "total_runs": 46,
  "success_rate": 0.8696,
  "avg_duration": 386.35,
  "median_duration": 337.5,
  "min_duration": 180,
  "max_duration": 780,
  "test_pass_rate": 0.9884,
  "total_tests": 6630,
  "total_test_failures": 77,
  "failures_by_workflow": {
    "main-ci": 2,
    "deploy-production": 1,
    "nightly-tests": 0
  },
  "slowest_build": {
    "id": 12390,
    "duration": 780,
    "workflow": "integration-tests"
  },
  "fastest_build": {
    "id": 12355,
    "duration": 180,
    "workflow": "linter"
  },
  "per_workflow_metrics": {
    "main-ci": {
      "runs": 30,
      "success_rate": 0.9333,
      "avg_duration": 340.5
    },
    "deploy-production": {
      "runs": 10,
      "success_rate": 0.90,
      "avg_duration": 450.2
    }
  }
}
```

**Implementation Approach:**

**Algorithm (Pseudocode):**
```
1. IF runs list is empty:
     RETURN dictionary with total_runs=0, success_rate=0.0
     
2. Calculate Success Rate:
   - Filter runs where conclusion == 'success'
   - success_rate = count(successful) / count(total)
   
3. Calculate Duration Statistics:
   - Extract all duration_seconds values into list
   - avg_duration = sum(durations) / count(durations)
   - median_duration = sorted(durations)[middle_index]
   - min_duration = min(durations)
   - max_duration = max(durations)
   
4. Calculate Test Pass Rate:
   - For each run, extract test_results (use .get() for safety)
   - Sum all test totals across runs
   - Sum all test failures across runs
   - pass_rate = (total_tests - failed_tests) / total_tests

5. Identify Slowest and Fastest Builds:
   - slowest_build = run with maximum duration_seconds
   - fastest_build = run with minimum duration_seconds
   - Record id, duration_seconds, and workflow for each

6. Count Failures by Workflow:
   - For each run where conclusion != 'success':
       Increment failures_by_workflow[run['workflow']] count

7. Group Runs by Workflow:
   - Create empty dictionary workflows
   - For each run:
       Add run to workflows[run['workflow']] list
   - For each workflow in workflows:
       Calculate separate metrics (success_rate, avg_duration)

8. RETURN comprehensive metrics dictionary
```

**Key Python Concepts:**
- List comprehensions: `[r for r in runs if condition]`
- `len()` for counting
- `sum()` for totals
- `sorted()` for median calculation
- `min()` and `max()` built-ins
- Dictionary `.get(key, default)` for safe access
- Dictionary grouping pattern
- Generator expressions with `sum()`

**Expected Return Structure:**
```python
{
  'total_runs': int,
  'success_rate': float,           # 0.0 to 1.0
  'avg_duration': float,
  'median_duration': float,
  'min_duration': int,
  'max_duration': int,
  'test_pass_rate': float,         # 0.0 to 1.0
  'total_tests': int,
  'total_test_failures': int,
  'failures_by_workflow': {
    'workflow_name': int,          # count of failed runs
  },
  'slowest_build': {'id': int, 'duration': int, 'workflow': str},
  'fastest_build': {'id': int, 'duration': int, 'workflow': str},
  'per_workflow_metrics': {
    'workflow_name': {'runs': int, 'success_rate': float, 'avg_duration': float}
  }
}
```

---

### Part 4: Anomaly Detection (20 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/anomaly-detection
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/anomaly-detection
git push origin main
```

---

**Function:** `detect_anomalies(metrics: dict, config: dict, runs: list) -> list`

Identify problematic patterns in CI/CD pipeline health.

**Requirements:**
- ✅ Detect when success rate falls below threshold  
- ✅ Identify builds exceeding max duration threshold  
- ✅ Detect failure streaks (consecutive failures)  
- ✅ Identify flaky tests (tests that fail intermittently)  
- ✅ Flag workflows with declining performance trends  
- ✅ Return list of anomaly dictionaries with severity levels  
- ✅ Each anomaly includes: type, severity, description, affected_runs  
- ✅ Support configurable thresholds from config

**Example Usage:**
```python
config = load_config('config.json')
runs = parse_pipeline_data('sample_data/github_actions_runs.json')
metrics = calculate_metrics(runs)

anomalies = detect_anomalies(metrics, config, runs)

print(f"Found {len(anomalies)} anomalies")
# Output: Found 4 anomalies

for anomaly in anomalies:
    print(f"[{anomaly['severity']}] {anomaly['type']}: {anomaly['description']}")
# Output:
# [CRITICAL] low_success_rate: Success rate 86.96% below threshold 95.0%
# [WARNING] slow_build: Build 12390 took 780s (threshold: 600s)
# [WARNING] failure_streak: Workflow 'deploy-production' failed 3 consecutive times
# [CRITICAL] flaky_tests: Test 'test_database_connection' failed in 4 of last 10 runs
```

**Anomaly Structure:**
```python
{
    "type": "low_success_rate",
    "severity": "CRITICAL",
    "description": "Success rate 86.96% below threshold 95.0%",
    "affected_runs": [],  # List of run IDs
    "threshold_value": 0.95,
    "actual_value": 0.912,
    "recommendation": "Investigate recent failures in main-ci workflow"
}
```

**Anomaly Types to Detect:**

1. **Low Success Rate** (Critical if < threshold)
```python
if metrics['success_rate'] < config['thresholds']['min_success_rate']:
    anomalies.append({
        'type': 'low_success_rate',
        'severity': 'CRITICAL',
        'description': f"Success rate {metrics['success_rate']:.1%} below threshold {config['thresholds']['min_success_rate']:.1%}",
        # ...
    })
```

2. **Slow Builds** (Warning if duration > threshold)
```python
slow_builds = [r for r in runs if r['duration_seconds'] > config['thresholds']['max_duration_seconds']]
for build in slow_builds:
    anomalies.append({
        'type': 'slow_build',
        'severity': 'WARNING',
        'description': f"Build {build['id']} took {build['duration_seconds']}s (threshold: {config['thresholds']['max_duration_seconds']}s)",
        'affected_runs': [build['id']],
        # ...
    })
```

3. **Failure Streaks** (Critical if consecutive failures >= threshold)
```python
# Group runs by workflow, check for consecutive failures
for workflow_name in metrics['per_workflow_metrics']:
    workflow_runs = [r for r in runs if r['workflow'] == workflow_name]
    # Sort by timestamp
    workflow_runs.sort(key=lambda r: r['timestamp'])
    
    # Count consecutive failures
    consecutive_failures = 0
    for run in workflow_runs:
        if run['conclusion'] != 'success':
            consecutive_failures += 1
        else:
            consecutive_failures = 0
        
        if consecutive_failures >= config['thresholds']['max_failure_streak']:
            anomalies.append({
                'type': 'failure_streak',
                'severity': 'CRITICAL',
                'description': f"Workflow '{workflow_name}' failed {consecutive_failures} consecutive times",
                # ...
            })
            break
```

4. **Flaky Tests** (Warning if test fails intermittently)
```python
# Collect all test failures across runs
test_failures = {}
for run in runs:
    # Parse log file to identify which specific tests failed
    # For each failed test, track how often it fails
    # Flag tests that fail < 50% of time (flaky) but > 10% of time
```

**Implementation Approach:**

**Algorithm (Pseudocode):**
```
1. Initialize empty anomalies list
2. Extract thresholds from config dictionary

3. Check Success Rate:
   IF metrics['success_rate'] < thresholds['min_success_rate']:
     CREATE anomaly dict with:
       - type: 'low_success_rate'
       - severity: 'CRITICAL'
       - description, threshold_value, actual_value, recommendation
     APPEND to anomalies list
     
4. Check for Slow Builds:
   FOR each run in runs:
     IF run['duration_seconds'] > thresholds['max_duration_seconds']:
       CREATE anomaly dict for this slow build
       APPEND to anomalies
       
5. Check for Failure Streaks (per workflow):
   Group runs by workflow name
   FOR each workflow:
     Sort runs by timestamp (oldest first)
     Track consecutive_failures count
     FOR each run in chronological order:
       IF run failed:
         INCREMENT consecutive_failures
         IF consecutive_failures >= threshold:
           CREATE streak anomaly
           BREAK (only report once per workflow)
       ELSE:
         RESET consecutive_failures to 0
         
6. Check Test Pass Rate (optional):
   IF metrics['test_pass_rate'] < threshold:
     CREATE anomaly for low test pass rate
     
7. RETURN list of all detected anomalies
```

**Anomaly Dictionary Structure:**
```python
{
  'type': str,           # 'low_success_rate', 'slow_build', 'failure_streak'
  'severity': str,       # 'CRITICAL' or 'WARNING'
  'description': str,    # Human-readable explanation
  'affected_runs': list, # List of run IDs involved
  'threshold_value': float,
  'actual_value': float,
  'recommendation': str  # Suggested action
}
```

**Key Python Concepts:**
- Conditional logic with thresholds
- List append for building results
- Dictionary grouping (group runs by workflow)
- List sorting with `key` parameter: `sorted(runs, key=lambda r: r['timestamp'])`
- Tracking state in loops (consecutive counter)
- Boolean logic for severity classification

**Severity Assignment:**
- **CRITICAL**: Success rate issues, long failure streaks (>= threshold)
- **WARNING**: Individual slow builds, moderate test failures

---

### Part 5: Report Generation (20 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/report-generation
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/report-generation
git push origin main
```

---

**Function:** `generate_report(metrics: dict, anomalies: list, output_path: str, format: str = 'json') -> None`

Generate comprehensive health report in multiple formats.

**Requirements:**
- ✅ Support JSON, CSV, and TEXT output formats  
- ✅ Include metrics summary, anomalies, recommendations  
- ✅ Write to specified output file using pathlib  
- ✅ Handle file write errors gracefully  
- ✅ Create output directory if it doesn't exist  
- ✅ Include timestamp and report metadata  
- ✅ Format text output for human readability  
- ✅ Log report generation success/failure

**Example Usage:**
```python
config = load_config('config.json')
runs = parse_pipeline_data('sample_data/github_actions_runs.json')
metrics = calculate_metrics(runs)
anomalies = detect_anomalies(metrics, config, runs)

# Generate JSON report
generate_report(metrics, anomalies, 'reports/health_report.json', format='json')
# Output: Report saved to reports/health_report.json

# Generate CSV summary
generate_report(metrics, anomalies, 'reports/health_summary.csv', format='csv')
# Output: CSV summary saved to reports/health_summary.csv

# Generate human-readable text
generate_report(metrics, anomalies, 'reports/health_report.txt', format='text')
# Output: Text report saved to reports/health_report.txt
```

**JSON Report Format:**
```json
{
  "report_metadata": {
    "generated_at": "2026-02-04T14:30:00Z",
    "tool_version": "1.0.0",
    "data_source": "sample_data/github_actions_runs.json",
    "analysis_period": {
      "start_date": "2026-01-28",
      "end_date": "2026-02-04",
      "total_days": 7
    }
  },
  "metrics_summary": {
    "total_runs": 46,
    "success_rate": 0.8696,
    "avg_duration": 386.35,
    "median_duration": 337.5,
    "test_pass_rate": 0.9884,
    "total_test_failures": 77
  },
  "anomalies": [
    {
      "type": "low_success_rate",
      "severity": "CRITICAL",
      "description": "Success rate 86.96% below threshold 95.0%",
      "affected_runs": [],
      "recommendation": "Investigate recent failures and common error patterns"
    }
  ],
  "health_score": 85,
  "status": "NEEDS_ATTENTION",
  "top_recommendations": [
    "Address critical low success rate issue in main-ci workflow",
    "Investigate 3 slow builds exceeding 600s duration threshold",
    "Review flaky test patterns affecting test reliability"
  ]
}
```

**CSV Report Format:**
```csv
metric_name,value,threshold,status
total_runs,46,-,OK
success_rate,86.96,95.00,BELOW_THRESHOLD
avg_duration,386.35,600.0,OK
test_pass_rate,98.84,98.00,OK
critical_anomalies,1,-,ACTION_REQUIRED
warning_anomalies,3,-,REVIEW
```

**Text Report Format:**
```
========================================
CI/CD Pipeline Health Report
========================================
Generated: 2026-02-04 14:30:00 UTC
Analysis Period: 2026-01-28 to 2026-02-04 (7 days)
Data Source: sample_data/github_actions_runs.json

METRICS SUMMARY
----------------------------------------
Total Runs:              46
Success Rate:            86.96% ⚠️  (threshold: 95.00%)
Average Duration:        386.3s ✓  (threshold: 600s)
Median Duration:         337.5s
Test Pass Rate:          98.84% ✓  (threshold: 98.00%)
Total Test Failures:     77

WORKFLOW BREAKDOWN
----------------------------------------
main-ci:
  - Runs: 30
  - Success Rate: 93.33%
  - Avg Duration: 340.5s

deploy-production:
  - Runs: 10
  - Success Rate: 90.00%
  - Avg Duration: 450.2s

nightly-tests:
  - Runs: 5
  - Success Rate: 100.00%
  - Avg Duration: 780.0s

ANOMALIES DETECTED
----------------------------------------
[CRITICAL] Low Success Rate
  - Success rate 86.96% below threshold 95.00%
  - Recommendation: Investigate recent failures and common error patterns

[WARNING] Slow Build
  - Build 12390 (integration-tests) took 780s, exceeding threshold of 600s
  - Recommendation: Check for infrastructure issues or inefficient test suites

[WARNING] Failure Streak
  - Workflow 'deploy-production' has 3 consecutive failures
  - Recommendation: Immediate investigation required for deploy-production workflow

OVERALL HEALTH ASSESSMENT
----------------------------------------
Health Score: 85/100
Status: NEEDS ATTENTION ⚠️

Top Priority Actions:
1. Address critical low success rate issue in main-ci workflow
2. Investigate 3 slow builds exceeding 600s duration threshold
3. Review failure patterns in deploy-production workflow

========================================
End of Report
========================================
```

**Implementation Approach:**

**Algorithm (Pseudocode):**
```
1. Convert output_path to Path object
2. Create parent directories if needed: path.parent.mkdir(parents=True, exist_ok=True)

3. Build report_data dictionary:
   - Add metadata: timestamp, version
   - Add metrics_summary
   - Add anomalies list
   - Calculate health_score (use helper function)
   - Determine status (use helper function)

4. TRY:
     IF format == 'json':
       Open file for writing
       Use json.dump() with indent=2
       
     ELIF format == 'csv':
       Open file for writing
       Create csv.writer
       Write header row
       Write metrics as rows
       
     ELIF format == 'text':
       Open file for writing
       Write formatted sections:
         - Header with title and timestamp
         - Metrics section with key-value pairs
         - Anomalies section with formatted list
         - Recommendations section
       
     Log success message
     
   EXCEPT Exception:
     Log error
     Re-raise exception
```

**Text Format Example Structure:**
```
========================================
CI/CD Pipeline Health Report
========================================
Generated: 2026-02-09 10:30:00 UTC

METRICS SUMMARY
----------------------------------------
Total Runs:              46
Success Rate:            86.96%
Average Duration:        386.3s
...

ANOMALIES DETECTED
----------------------------------------
[CRITICAL] low_success_rate
  - Description: Success rate below threshold
  - Recommendation: Investigate failures
...
```

**Key Python Concepts:**
- `Path.parent.mkdir(parents=True, exist_ok=True)` for directory creation
- `with open(path, 'w')` for writing files
- `json.dump(data, file, indent=2)` for JSON formatting
- `csv.writer()` and `writerow()` for CSV files
- f-strings for formatted text output
- String multiplication for separators: `'=' * 40`
- `datetime.utcnow().isoformat()` for timestamps
- Try-except for error handling
- `logging.info()` and `logging.error()` for feedback

**Helper Functions Provided:**
- `calculate_health_score(metrics, anomalies)` → int (0-100)
- `determine_status(anomalies)` → str ('HEALTHY', 'REVIEW_RECOMMENDED', 'NEEDS_ATTENTION')
        return 'REVIEW_RECOMMENDED'
    else:
        return 'HEALTHY'

---

### Part 6: Main Function and CLI (15 points)

**🌿 Git Workflow — create your feature branch before starting:**
```bash
git checkout main && git pull
git checkout -b feature/cli-interface
```

> ⚠️ **Do NOT delete this branch after merging.** The instructor needs it to verify your work.

**When you finish this part, merge back to main:**
```bash
git checkout main
git merge feature/cli-interface
git push origin main
```

---

**Function:** `main()` with argparse CLI interface

Orchestrate all components with professional command-line interface.

**Requirements:**
- ✅ Use argparse for command-line argument parsing
- ✅ Support positional `data_file` argument and flags: --config, --output, --format, --verbose, --start-date, --end-date
- ✅ Implement --help with clear usage documentation
- ✅ Set up logging with configurable verbosity  
- ✅ Orchestrate function calls in correct order  
- ✅ Handle exceptions at top level with clear error messages  
- ✅ Exit with appropriate exit codes (0=success, 1=error)  
- ✅ Display summary statistics to console

**Example Usage:**
```bash
# Basic usage — prints summary to console
./ci_health_monitor.py sample_data/github_actions_runs.json

# Specify config file
./ci_health_monitor.py sample_data/github_actions_runs.json --config config.json

# Generate different report formats
./ci_health_monitor.py sample_data/github_actions_runs.json --output report.json --format json
./ci_health_monitor.py sample_data/github_actions_runs.json --output summary.csv --format csv
./ci_health_monitor.py sample_data/github_actions_runs.json --output report.txt --format text

# Enable verbose logging
./ci_health_monitor.py sample_data/github_actions_runs.json --verbose

# Filter by date range
./ci_health_monitor.py sample_data/github_actions_runs.json --start-date 2026-02-01 --end-date 2026-02-07

# Full example
./ci_health_monitor.py sample_data/github_actions_runs.json \
  --config config.json \
  --output reports/health_report.json \
  --format json \
  --start-date 2026-02-01 \
  --end-date 2026-02-07 \
  --verbose
```

**CLI Help Output:**
```bash
$ ./ci_health_monitor.py --help

usage: ci_health_monitor.py [-h] [--config CONFIG]
                             [--output OUTPUT] [--format {json,csv,text}]
                             [--start-date START_DATE] [--end-date END_DATE]
                             [--verbose]
                             data_file

Monitor CI/CD pipeline health and detect anomalies

positional arguments:
  data_file             Path to pipeline data JSON file

options:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file path (default: config.json)
  --output OUTPUT       Output report file path (if not specified, prints to console)
  --format {json,csv,text}
                        Output report format (default: text)
  --start-date START_DATE
                        Filter runs from this date (YYYY-MM-DD)
  --end-date END_DATE   Filter runs to this date (YYYY-MM-DD)
  --verbose             Enable verbose logging

Examples:
  # Basic analysis
  ./ci_health_monitor.py sample_data/github_actions_runs.json

  # Custom config and data
  ./ci_health_monitor.py prod_runs.json --config prod_config.json

  # Generate text report with date filtering
  ./ci_health_monitor.py sample_data/github_actions_runs.json --output report.txt --format text --start-date 2026-02-01

  # Verbose mode for debugging
  ./ci_health_monitor.py sample_data/github_actions_runs.json --verbose
```

**Console Output Example:**
```
[INFO] CI/CD Health Monitor v1.0.0
[INFO] Loading configuration from config.json
[INFO] Parsing pipeline data from sample_data/github_actions_runs.json
[INFO] Found 46 workflow runs
[INFO] Calculating metrics...
[INFO] Detecting anomalies...
[WARNING] Found 4 anomalies (1 critical, 3 warnings)

======================================================================
CI/CD PIPELINE HEALTH SUMMARY
======================================================================

Health Score: 60/100
Status: NEEDS_ATTENTION

Total Runs: 46
Success Rate: 86.96%
Average Duration: 386.3 seconds
Test Pass Rate: 98.84%

Anomalies: 4 total (1 critical, 3 warnings)
======================================================================
```

**Technical Implementation:**
```python
#!/usr/bin/env python3
"""
CI/CD Pipeline Health Monitor
"""

import argparse
import logging
import sys
from datetime import datetime


def setup_logging(verbose: bool = False) -> None:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='[%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Monitor CI/CD pipeline health and detect anomalies',
        epilog='''
Examples:
  # Basic analysis
  ./ci_health_monitor.py sample_data/github_actions_runs.json

  # Custom config and data
  ./ci_health_monitor.py prod_runs.json --config prod_config.json

  # Generate text report with date filtering
  ./ci_health_monitor.py sample_data/github_actions_runs.json --output report.txt --format text --start-date 2026-02-01

  # Verbose mode for debugging
  ./ci_health_monitor.py sample_data/github_actions_runs.json --verbose
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'data_file',
        help='Path to pipeline data JSON file'
    )

    parser.add_argument(
        '--config',
        default='config.json',
        help='Configuration file path (default: config.json)'
    )

    parser.add_argument(
        '--output',
        help='Output report file path (if not specified, prints to console)'
    )

    parser.add_argument(
        '--format',
        choices=['json', 'csv', 'text'],
        default='text',
        help='Output report format (default: text)'
    )

    parser.add_argument(
        '--start-date',
        help='Filter runs from this date (YYYY-MM-DD)'
    )

    parser.add_argument(
        '--end-date',
        help='Filter runs to this date (YYYY-MM-DD)'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )

    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_arguments()
    setup_logging(args.verbose)

    try:
        logging.info("CI/CD Health Monitor v1.0.0")

        # Load configuration
        logging.info(f"Loading configuration from {args.config}")
        config = load_config(args.config)

        # Parse pipeline data
        logging.info(f"Parsing pipeline data from {args.data_file}")
        runs = parse_pipeline_data(args.data_file, args.start_date, args.end_date)
        logging.info(f"Found {len(runs)} workflow runs")

        # Calculate metrics
        logging.info("Calculating metrics...")
        metrics = calculate_metrics(runs)

        # Detect anomalies
        logging.info("Detecting anomalies...")
        anomalies = detect_anomalies(metrics, config, runs)

        if anomalies:
            critical_count = len([a for a in anomalies if a['severity'] == 'CRITICAL'])
            warning_count = len([a for a in anomalies if a['severity'] == 'WARNING'])
            logging.warning(f"Found {len(anomalies)} anomalies ({critical_count} critical, {warning_count} warnings)")
        else:
            logging.info("No anomalies detected - pipeline is healthy!")

        # Generate report or print summary
        if args.output:
            logging.info(f"Generating {args.format.upper()} report...")
            generate_report(metrics, anomalies, args.output, format=args.format)
        else:
            print_summary(metrics, anomalies)

        return 0

    except ConfigurationError as e:
        logging.error(f"Configuration error: {e}")
        return 1
    except DataParsingError as e:
        logging.error(f"Data parsing error: {e}")
        return 1
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        if args.verbose:
            logging.exception("Full traceback:")
        return 1


def print_summary(metrics: dict, anomalies: list) -> None:
    """Print summary statistics to console."""
    print("\n" + "=" * 40)
    print("PIPELINE HEALTH SUMMARY")
    print("=" * 40)
    print(f"Total Runs:        {metrics['total_runs']}")

    # Success rate with indicator
    success_indicator = "✓" if metrics['success_rate'] >= 0.95 else "⚠️"
    print(f"Success Rate:      {metrics['success_rate']*100:.2f}% {success_indicator}")

    # Duration with indicator
    duration_indicator = "✓" if metrics['avg_duration'] <= 600 else "⚠️"
    print(f"Avg Duration:      {metrics['avg_duration']:.1f}s {duration_indicator}")

    # Test pass rate with indicator
    test_indicator = "✓" if metrics.get('test_pass_rate', 1.0) >= 0.98 else "⚠️"
    print(f"Test Pass Rate:    {metrics.get('test_pass_rate', 1.0)*100:.2f}% {test_indicator}")

    print()

    critical_count = len([a for a in anomalies if a['severity'] == 'CRITICAL'])
    warning_count = len([a for a in anomalies if a['severity'] == 'WARNING'])

    print(f"Critical Issues:   {critical_count}")
    print(f"Warnings:          {warning_count}")

    health_score = calculate_health_score(metrics, anomalies)
    print(f"Health Score:      {health_score}/100")

    print()

    status = determine_status(anomalies)
    status_display = {
        'HEALTHY': 'HEALTHY ✓',
        'REVIEW_RECOMMENDED': 'REVIEW RECOMMENDED ⚠️',
        'NEEDS_ATTENTION': 'NEEDS ATTENTION ⚠️'
    }
    print(f"Status: {status_display.get(status, status)}")

    print("=" * 40)


if __name__ == '__main__':
    sys.exit(main())
```

---

## 🧪 Testing Your Implementation

**📘 For detailed information about automated CI/CD testing**, see the [CI/CD Auto-Grading Guide](docs/CI_CD_GUIDE.md). This section covers local testing only.

### Running Automated Tests

```bash
# Install pytest if not already installed
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_metrics.py -v

# Run with coverage report
pytest tests/ --cov=ci_health_monitor --cov-report=html

# View coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

### Manual Testing Workflow

```bash
# Test 1: Basic functionality
./ci_health_monitor.py --verbose
# Expected: Should complete without errors, generate report

# Test 2: Custom output formats
./ci_health_monitor.py --output test.csv --format csv
./ci_health_monitor.py --output test.txt --format text
# Expected: Should create valid CSV and text files

# Test 3: Date filtering
./ci_health_monitor.py --start-date 2026-02-01 --end-date 2026-02-03
# Expected: Should filter runs and show fewer total runs

# Test 4: Error handling
./ci_health_monitor.py --config nonexistent.json
# Expected: Should show configuration error, exit code 1

# Test 5: Help text
./ci_health_monitor.py --help
# Expected: Should display usage information

# Test 6: Invalid format
./ci_health_monitor.py --format xml
# Expected: Should show argument error for invalid format choice
```

### Test Data Exploration

```bash
# View sample data structure
cat sample_data/github_actions_runs.json | python3 -m json.tool | head -50

# Count runs
cat sample_data/github_actions_runs.json | python3 -c "import json,sys; data=json.load(sys.stdin); print(len(data['workflow_runs']))"

# Check for failures
grep -c '"conclusion": "failure"' sample_data/github_actions_runs.json
```

---

## 📊 Grading Breakdown

### Part Distribution (115 base points)

| Part | Component | Points | What's Graded |
|------|-----------|--------|---------------|
| 1 | Configuration Loader | 15 | JSON parsing, validation, error handling |
| 2 | Pipeline Data Parser | 15 | Data parsing, date filtering, validation |
| 3 | Metrics Calculator | 20 | Calculation accuracy, edge cases |
| 4 | Anomaly Detection | 20 | Detection logic, thresholds, severity assignment |
| 5 | Report Generation | 20 | Multi-format output, formatting |
| 6 | Main Function/CLI | 15 | argparse, orchestration, logging |
| **Subtotal** | **Code Functionality** | **105** | |

### Professional Practice (45 points)

| Category | Points | What's Graded |
|----------|--------|---------------|
| Git Workflow | 10 | 4+ branches, 10+ commits, clear messages |
| Testing | 5 | Pass 80%+ of pytest tests |
| Code Quality & Documentation | 10 | PEP 8 style, docstrings, README, comments |
| Video Walkthrough | 20 | 5-7 min demo, code walkthrough, clear explanation |

### Total: 145 Points

---

## 🎥 Video Walkthrough Requirements

Create a 5-7 minute video demonstrating your project:

### Required Content

1. **Introduction** (30 seconds)
   - Your name and project title
   - Brief overview of what the tool does

2. **Code Walkthrough** (2-3 minutes)
   - Show ONE function in detail (recommend: `detect_anomalies`)
   - Explain your implementation approach
   - Highlight interesting code patterns or challenges
   - Point out error handling and exception handling

3. **Live Demonstration** (2-3 minutes)
   - Run the tool with sample data: `./ci_health_monitor.py --verbose`
   - Show different output formats (JSON, CSV, text)
   - Demonstrate date filtering
   - Show how anomalies are detected
   - Display a generated report

4. **Git Workflow** (30 seconds)
   - Show `git log --graph --oneline --all`
   - Highlight your feature branches and merge commits

5. **Testing** (30 seconds)
   - Run pytest: `pytest tests/ -v`
   - Show passing tests

### Recording Tips

- Use Zoom, OBS Studio, or QuickTime for recording
- Show your face (picture-in-picture) for engagement
- Use clear audio - test before recording full video
- Zoom in on code/terminal for readability
- Edit out long pauses or mistakes
- Add captions if helpful

### Submission
- Upload to YouTube/Google Drive/OneDrive (unlisted/private link OK)
- Include link in Canvas submission comments
- Or upload video file directly if under size limit

---

## 📁 Submission Checklist

Before submitting, verify:

### Code Files
- [ ] `ci_health_monitor.py` - Complete implementation
- [ ] All 6 parts implemented and tested
- [ ] Proper exception handling in all functions
- [ ] Docstrings for all functions
- [ ] PEP 8 compliant (run `black ci_health_monitor.py`)

### Git Requirements
- [ ] 4+ feature branches created
- [ ] 10+ commits with clear messages
- [ ] `branch_history.txt` generated and committed
- [ ] All branches merged to main
- [ ] Pushed to GitHub

### Testing
- [ ] Pass 80%+ of pytest tests
- [ ] Manual testing completed
- [ ] Reports generate correctly in all formats

### Documentation
- [ ] Code comments explain complex logic
- [ ] Function docstrings present
- [ ] README.md reviewed (this file)

### Video
- [ ] 5-7 minute walkthrough recorded
- [ ] Video uploaded and link obtained
- [ ] Video demonstrates all requirements

### Final Steps
- [ ] Run final test: `pytest tests/ -v`
- [ ] Run final score check: `python3 calculate_score.py`
- [ ] Generate final branch history: `git log --graph --oneline --all --decorate > branch_history.txt`
- [ ] Push to GitHub: `git push origin main`
- [ ] Submit to Canvas with video link

---

## 🚀 Bonus Features (Optional)

Implement AFTER completing MVP for extra credit:

### 1. Email Alert Simulation (+5 points)
```python
def send_alerts(anomalies: list, config: dict) -> None:
    """Simulate sending email alerts for critical anomalies."""
    critical_anomalies = [a for a in anomalies if a['severity'] == 'CRITICAL']
    
    if not critical_anomalies or not config['alert_config']['enabled']:
        return
    
    # Simulate email composition
    email_body = format_alert_email(critical_anomalies)
    recipients = config['alert_config']['recipients']
    
    print(f"\n[ALERT SIMULATION] Would send email to: {', '.join(recipients)}")
    print("=" * 50)
    print(email_body)
    print("=" * 50)
    
    # In real implementation, would use smtplib or email service API
```

### 2. Trending Analysis (+5 points)
```python
def analyze_trends(current_metrics: dict, historical_data_file: str) -> dict:
    """Compare current metrics to historical averages."""
    # Load historical data
    # Calculate deltas (current vs average)
    # Detect degrading trends (success rate declining, duration increasing)
    # Return trend analysis
    pass
```

### 3. HTML Report Generation (+5 points)
```python
def generate_html_report(metrics: dict, anomalies: list, output_path: str) -> None:
    """Generate interactive HTML report with charts."""
    # Create HTML template
    # Embed Chart.js for visualizations
    # Generate success rate timeline chart
    # Generate duration distribution histogram
    # Format anomalies as styled cards
    pass
```

### 4. GitHub API Integration (+10 points)
```python
import requests

def fetch_github_workflow_runs(repo: str, token: str) -> list:
    """Fetch real workflow run data from GitHub API."""
    # Use GitHub REST API: GET /repos/{owner}/{repo}/actions/runs
    # Handle pagination
    # Transform API response to internal format
    # Cache results for efficiency
    pass
```

---

## 💡 Tips for Success

### Start Early!
- This project is more complex than Project 2
- Python has more moving parts than Bash
- Exception handling requires thought and testing
- Don't underestimate the time needed

### Test Frequently
- Test after implementing each sub-function
- Use Python REPL for quick function testing: `python3`
- Run pytest regularly: `pytest tests/test_config.py -v`
- Don't wait until everything is done to test!

### Use the Python REPL for Debugging
```python
# Quick testing without running full script
python3
>>> from ci_health_monitor import load_config
>>> config = load_config('config.json')
>>> print(config['thresholds'])
>>> # Test your functions interactively!
```

### Git Workflow Matters
- Create feature branch for each part: `git checkout -b feature/config-loader`
- Commit frequently (every 20-30 min when code works)
- Write clear commit messages: "Add JSON config validation"
- Merge to main after completing and testing each part

### Exception Handling is Critical
- Every file operation needs try-except
- Catch specific exceptions (FileNotFoundError, json.JSONDecodeError)
- Provide helpful error messages
- Don't use bare `except:` - catch specific exceptions!

### Read the Module 3 Decision Trees
- Review "Python vs Bash for Scripting" decision tree
- Review "pathlib vs os.path" decision tree
- Review "subprocess methods" decision tree
- Apply the right tools for each task!

### Use Module 3 Concepts
- **pathlib** for file operations (not os.path or string manipulation)
- **Context managers** (`with` statements) for file handling
- **argparse** for CLI (not sys.argv directly)
- **json/csv modules** for data processing
- **Logging** for debugging (not print statements)
- **Custom exceptions** for domain-specific errors

### Ask Questions Early
- Use office hours if stuck > 1 hour
- Post to discussion board (without sharing full solution code)
- Review Module 3 lecture notes and exercises
- Check pytest error messages - they're very helpful!

---

## 🔗 Related Module 3 Content

### Lectures
- Module 3A.1: File I/O and Text Processing → Parts 1, 2, 5
- Module 3A.2: System Interaction → Parts 2, 6
- Module 3B.1: Exception Handling → All parts (error handling)
- Module 3B.2: CLI Tools → Part 6 (argparse)

### Hands-On Exercises
- `file_operations.py` → Parts 1, 2, 5 (file I/O patterns)
- `system_tasks.py` → Part 6 (argparse examples)
- `exception_handling.py` → All parts (error handling patterns)
- `quickstart.py` → Overall Python structure

### Decision Trees
- "When to use Python vs Bash" → Project justification
- "pathlib vs os.path" → Parts 1, 2, 5
- "subprocess methods" → Part 6 (optional system commands)
- "argparse vs sys.argv" → Part 6

---

## 🎓 Learning Outcomes Alignment

This project demonstrates mastery of these Module 3 outcomes:

- ✅ **PY-FUND** - Python fundamentals (functions, dicts, lists, comprehensions)
- ✅ **FILE-IO** - File I/O with context managers, CSV/JSON processing
- ✅ **SYS-INT** - pathlib for file operations, argparse for CLI
- ✅ **AUTO-DEC** - Applied decision frameworks (Python vs Bash, pathlib vs os.path)
- ✅ **EXCEPT** - Comprehensive exception handling and custom exceptions
- ✅ **ERROR-REC** - Structured logging and error recovery patterns
- ✅ **PY-AUTO** - Complete professional Python automation script

---

## 📞 Getting Help

### If You're Stuck
1. **Read error messages carefully** - Python errors are informative!
2. **Test one function at a time** - Isolate the problem
3. **Use print debugging** - Or better, use logging module
4. **Review Module 3 lecture notes** - Similar patterns covered
5. **Check Module 3 exercises** - Many similar examples
6. **Run pytest for specific function** - `pytest tests/test_config.py -v`
7. **Ask in office hours** - Bring specific error messages

### Resources
- **Python Documentation**: https://docs.python.org/3/
- **pathlib Guide**: https://realpython.com/python-pathlib/
- **argparse Tutorial**: https://docs.python.org/3/howto/argparse.html
- **pytest Documentation**: https://docs.pytest.org/
- **Module 3 Lecture Notes**: In course repository
- **Module 3 Exercises**: `hands_on_exercises/module03/`

---

## 🏆 Success Criteria

You'll know you're done when:

- ✅ All 6 parts implemented and working
- ✅ `pytest tests/ -v` shows 80%+ passing
- ✅ `python3 calculate_score.py` shows target score
- ✅ Can run: `./ci_health_monitor.py --verbose` without errors
- ✅ Reports generate correctly (JSON, CSV, text)
- ✅ Git history shows 4+ branches, 10+ commits
- ✅ Code has proper exception handling everywhere
- ✅ Video walkthrough complete (5-7 minutes)
- ✅ All files pushed to GitHub
- ✅ Ready to submit!

**Good luck! Remember: Start early, test often, commit frequently!** 🚀

---

---

## 📄 Generating branch_history.txt

After merging all your feature branches to main, generate the branch history file so the instructor can verify your Git workflow:

**Step 1 — Make sure you are on main and up to date:**
```bash
git checkout main
git pull
```

**Step 2 — Generate the file:**
```bash
git log --graph --oneline --all --decorate > branch_history.txt
```

**Step 3 — Commit and push it:**
```bash
git add branch_history.txt
git commit -m "docs: add branch history for submission"
git push origin main
```

**What this file shows:**
- Every branch you created (`feature/config-loader`, `feature/pipeline-parser`, etc.)
- The merge commits that brought each branch into `main`
- A visual graph of your development history

> ⚠️ **Do not delete your feature branches before generating this file.** The graph will be empty or misleading if branches are removed. The instructor uses both the live branches and this file to grade the Git workflow portion.

**Questions?** Review this README, check Module 3 materials, or ask in office hours!
