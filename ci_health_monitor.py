#!/usr/bin/env python3
"""
CI/CD Pipeline Health Monitor
Module 3 Integration Project

Author: [Your Name]
Date: [Date]
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


# ==============================================================================
# CUSTOM EXCEPTIONS
# ==============================================================================

class ConfigurationError(Exception):
    """Raised when configuration is invalid or missing."""
    pass


class DataParsingError(Exception):
    """Raised when pipeline data cannot be parsed."""
    pass


# ==============================================================================
# TODO 1: Configuration Loader (15 points) - Est: 1-1.5 hours
# ==============================================================================

def load_config(config_file: str) -> dict:
    """
    Load and validate configuration from JSON file.

    Args:
        config_file: Path to configuration JSON file

    Returns:
        dict: Validated configuration dictionary

    Raises:
        ConfigurationError: If file not found, invalid JSON, or missing required keys

    Required Keys:
        - thresholds: dict with max_duration_seconds, min_success_rate, max_failure_streak
        - alert_config: dict with enabled, recipients, severity_levels

    Example:
        >>> config = load_config('config.json')
        >>> print(config['thresholds']['max_duration_seconds'])
        600
    """
    path = Path(config_file)

    if not path.exists():
        raise ConfigurationError(f"Configuration file not found: {config_file}")

    try:
        with path.open("r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigurationError(f"Invalid JSON in configuration file {config_file}: {e}")

    required_keys = ["thresholds", "alert_config"]
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(f"Missing required configuration key: '{key}'")

    return config


# ==============================================================================
# TODO 2: Pipeline Data Parser (15 points) - Est: 2-2.5 hours
# ==============================================================================

REQUIRED_RUN_FIELDS = ["id", "workflow", "conclusion", "duration_seconds", "timestamp"]


def _parse_timestamp(timestamp: str) -> datetime:
    """Parse an ISO 8601 timestamp like '2026-02-01T10:30:00Z' into a datetime."""
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))


def parse_pipeline_data(data_file: str, start_date: str = None, end_date: str = None) -> list:
    """
    Parse CI/CD pipeline run data from JSON file with optional date filtering.

    Args:
        data_file: Path to pipeline data JSON file
        start_date: Optional start date filter (YYYY-MM-DD)
        end_date: Optional end date filter (YYYY-MM-DD)

    Returns:
        list: List of validated workflow run dictionaries

    Raises:
        DataParsingError: If file not found, invalid JSON, or missing required fields
    """
    path = Path(data_file)

    if not path.exists():
        raise DataParsingError(f"Pipeline data file not found: {data_file}")

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise DataParsingError(f"Invalid JSON in pipeline data file {data_file}: {e}")

    if "workflow_runs" not in data:
        raise DataParsingError(f"Pipeline data file {data_file} is missing 'workflow_runs' key")

    runs = data["workflow_runs"]

    # Validate required fields exist in each run before filtering.
    for run in runs:
        for field in REQUIRED_RUN_FIELDS:
            if field not in run:
                raise DataParsingError(
                    f"Workflow run {run.get('id', '<unknown>')} is missing required field '{field}'"
                )

    # Apply optional date range filtering.
    if start_date or end_date:
        start_dt = _parse_timestamp(start_date + "T00:00:00Z") if start_date else None
        end_dt = _parse_timestamp(end_date + "T23:59:59Z") if end_date else None

        filtered = []
        for run in runs:
            run_dt = _parse_timestamp(run["timestamp"])
            if start_dt and run_dt < start_dt:
                continue
            if end_dt and run_dt > end_dt:
                continue
            filtered.append(run)
        runs = filtered

    return runs



# ==============================================================================
# TODO 3: Metrics Calculator (20 points) - Est: 2-3 hours
# ==============================================================================

def calculate_metrics(runs: list) -> dict:
    """
    Calculate CI/CD pipeline health metrics from workflow run data.

    Args:
        runs: List of workflow run dictionaries

    Returns:
        dict: Metrics including success_rate, avg_duration, test_pass_rate, etc.
    """
    if not runs:
        return {
            "total_runs": 0,
            "success_rate": 0.0,
            "message": "No runs to analyze"
        }

    total_runs = len(runs)
    successful = [r for r in runs if r["conclusion"] == "success"]
    success_rate = len(successful) / total_runs

    # Duration statistics
    durations = [r["duration_seconds"] for r in runs]
    avg_duration = sum(durations) / total_runs
    sorted_durations = sorted(durations)
    mid = len(sorted_durations) // 2
    if len(sorted_durations) % 2 == 0:
        median_duration = (sorted_durations[mid - 1] + sorted_durations[mid]) / 2
    else:
        median_duration = sorted_durations[mid]
    min_duration = min(durations)
    max_duration = max(durations)

    # Test pass rate (test_results may be missing on some runs)
    total_tests = 0
    total_test_failures = 0
    for r in runs:
        test_results = r.get("test_results", {})
        total_tests += test_results.get("total", 0)
        total_test_failures += test_results.get("failed", 0)

    if total_tests > 0:
        test_pass_rate = (total_tests - total_test_failures) / total_tests
    else:
        test_pass_rate = 1.0

    # Failures by workflow
    failures_by_workflow: Dict[str, int] = {}
    for r in runs:
        if r["conclusion"] != "success":
            failures_by_workflow[r["workflow"]] = failures_by_workflow.get(r["workflow"], 0) + 1

    # Slowest / fastest builds
    slowest_run = max(runs, key=lambda r: r["duration_seconds"])
    fastest_run = min(runs, key=lambda r: r["duration_seconds"])
    slowest_build = {
        "id": slowest_run["id"],
        "duration": slowest_run["duration_seconds"],
        "workflow": slowest_run["workflow"],
    }
    fastest_build = {
        "id": fastest_run["id"],
        "duration": fastest_run["duration_seconds"],
        "workflow": fastest_run["workflow"],
    }

    # Per-workflow metrics
    workflows: Dict[str, List[dict]] = {}
    for r in runs:
        workflows.setdefault(r["workflow"], []).append(r)

    per_workflow_metrics = {}
    for wf_name, wf_runs in workflows.items():
        wf_successful = [r for r in wf_runs if r["conclusion"] == "success"]
        wf_durations = [r["duration_seconds"] for r in wf_runs]
        per_workflow_metrics[wf_name] = {
            "runs": len(wf_runs),
            "success_rate": len(wf_successful) / len(wf_runs),
            "avg_duration": sum(wf_durations) / len(wf_durations),
        }

    return {
        "total_runs": total_runs,
        "success_rate": success_rate,
        "avg_duration": avg_duration,
        "median_duration": median_duration,
        "min_duration": min_duration,
        "max_duration": max_duration,
        "test_pass_rate": test_pass_rate,
        "total_tests": total_tests,
        "total_test_failures": total_test_failures,
        "failures_by_workflow": failures_by_workflow,
        "slowest_build": slowest_build,
        "fastest_build": fastest_build,
        "per_workflow_metrics": per_workflow_metrics,
    }



# ==============================================================================
# TODO 4: Anomaly Detection (20 points) - Est: 2.5-3 hours
# ==============================================================================

def detect_anomalies(metrics: dict, config: dict, runs: list) -> list:
    """
    Identify problematic patterns in CI/CD pipeline health.

    Args:
        metrics: Calculated metrics dictionary
        config: Configuration with thresholds
        runs: Original run data for detailed analysis

    Returns:
        list: List of anomaly dictionaries with type, severity, description
    """
    anomalies = []
    thresholds = config["thresholds"]

    # 1. Low success rate
    min_success_rate = thresholds.get("min_success_rate")
    if min_success_rate is not None and metrics.get("total_runs", 0) > 0:
        actual = metrics["success_rate"]
        if actual < min_success_rate:
            anomalies.append({
                "type": "low_success_rate",
                "severity": "CRITICAL",
                "description": (
                    f"Success rate {actual:.1%} below threshold {min_success_rate:.1%}"
                ),
                "affected_runs": [],
                "threshold_value": min_success_rate,
                "actual_value": actual,
                "recommendation": "Investigate recent failures and common error patterns",
            })

    # 2. Slow builds
    max_duration = thresholds.get("max_duration_seconds")
    if max_duration is not None:
        slow_builds = [r for r in runs if r["duration_seconds"] > max_duration]
        for build in slow_builds:
            anomalies.append({
                "type": "slow_build",
                "severity": "WARNING",
                "description": (
                    f"Build {build['id']} took {build['duration_seconds']}s "
                    f"(threshold: {max_duration}s)"
                ),
                "affected_runs": [build["id"]],
                "threshold_value": max_duration,
                "actual_value": build["duration_seconds"],
                "recommendation": "Check for infrastructure issues or inefficient test suites",
            })

    # 3. Failure streaks (per workflow, in chronological order)
    max_failure_streak = thresholds.get("max_failure_streak")
    if max_failure_streak is not None:
        workflows: Dict[str, List[dict]] = {}
        for r in runs:
            workflows.setdefault(r["workflow"], []).append(r)

        for wf_name, wf_runs in workflows.items():
            wf_runs_sorted = sorted(wf_runs, key=lambda r: r["timestamp"])
            consecutive_failures = 0
            streak_run_ids = []
            reported = False
            for run in wf_runs_sorted:
                if run["conclusion"] != "success":
                    consecutive_failures += 1
                    streak_run_ids.append(run["id"])
                else:
                    consecutive_failures = 0
                    streak_run_ids = []

                if consecutive_failures >= max_failure_streak and not reported:
                    anomalies.append({
                        "type": "failure_streak",
                        "severity": "CRITICAL",
                        "description": (
                            f"Workflow '{wf_name}' failed {consecutive_failures} "
                            f"consecutive times"
                        ),
                        "affected_runs": list(streak_run_ids),
                        "threshold_value": max_failure_streak,
                        "actual_value": consecutive_failures,
                        "recommendation": (
                            f"Immediate investigation required for {wf_name} workflow"
                        ),
                    })
                    reported = True  # only report once per workflow

    # 4. Low test pass rate
    test_pass_rate_threshold = thresholds.get("test_pass_rate_threshold")
    if test_pass_rate_threshold is not None and metrics.get("total_tests", 0) > 0:
        actual = metrics["test_pass_rate"]
        if actual < test_pass_rate_threshold:
            anomalies.append({
                "type": "low_test_pass_rate",
                "severity": "WARNING",
                "description": (
                    f"Test pass rate {actual:.1%} below threshold "
                    f"{test_pass_rate_threshold:.1%}"
                ),
                "affected_runs": [],
                "threshold_value": test_pass_rate_threshold,
                "actual_value": actual,
                "recommendation": "Review flaky test patterns affecting test reliability",
            })

    return anomalies


# ==============================================================================
# TODO 5: Report Generation (20 points) - Est: 1.5-2 hours
# ==============================================================================

def calculate_health_score(metrics: dict, anomalies: list) -> int:
    """Calculate overall health score (0-100)."""
    score = 100

    # Deduct for low success rate
    if metrics.get('success_rate', 1.0) < 0.95:
        score -= 15

    # Deduct for anomalies
    for anomaly in anomalies:
        if anomaly['severity'] == 'CRITICAL':
            score -= 10
        elif anomaly['severity'] == 'WARNING':
            score -= 5

    return max(0, score)


def determine_status(anomalies: list) -> str:
    """Determine overall status based on anomalies."""
    critical_count = len([a for a in anomalies if a['severity'] == 'CRITICAL'])

    if critical_count > 0:
        return 'NEEDS_ATTENTION'
    elif len(anomalies) > 0:
        return 'REVIEW_RECOMMENDED'
    else:
        return 'HEALTHY'


def generate_report(metrics: dict, anomalies: list, output_path: str, format: str = 'json') -> None:
    """
    Generate comprehensive health report in multiple formats.

    Args:
        metrics: Calculated metrics dictionary
        anomalies: List of detected anomalies
        output_path: Output file path
        format: Output format ('json', 'csv', or 'text')

    Raises:
        ValueError: If unsupported format specified
    """
    if format not in ("json", "csv", "text"):
        raise ValueError(f"Unsupported report format: {format}")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    health_score = calculate_health_score(metrics, anomalies)
    status = determine_status(anomalies)

    critical_count = len([a for a in anomalies if a['severity'] == 'CRITICAL'])
    warning_count = len([a for a in anomalies if a['severity'] == 'WARNING'])

    try:
        if format == "json":
            report_data = {
                "report_metadata": {
                    "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "tool_version": "1.0.0",
                },
                "metrics_summary": metrics,
                "anomalies": anomalies,
                "health_score": health_score,
                "status": status,
                "top_recommendations": [a["recommendation"] for a in anomalies if "recommendation" in a],
            }
            with path.open("w", encoding="utf-8") as f:
                json.dump(report_data, f, indent=2)

        elif format == "csv":
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["metric_name", "value", "threshold", "status"])
                writer.writerow(["total_runs", metrics.get("total_runs", 0), "-", "OK"])
                writer.writerow([
                    "success_rate",
                    f"{metrics.get('success_rate', 0) * 100:.2f}",
                    "-",
                    "OK" if metrics.get("success_rate", 0) >= 0.95 else "BELOW_THRESHOLD",
                ])
                writer.writerow([
                    "avg_duration", f"{metrics.get('avg_duration', 0):.2f}", "-", "OK"
                ])
                writer.writerow([
                    "test_pass_rate",
                    f"{metrics.get('test_pass_rate', 1.0) * 100:.2f}",
                    "-",
                    "OK" if metrics.get("test_pass_rate", 1.0) >= 0.98 else "BELOW_THRESHOLD",
                ])
                writer.writerow(["critical_anomalies", critical_count, "-", "ACTION_REQUIRED" if critical_count else "OK"])
                writer.writerow(["warning_anomalies", warning_count, "-", "REVIEW" if warning_count else "OK"])

        elif format == "text":
            lines = []
            lines.append("=" * 40)
            lines.append("CI/CD Pipeline Health Report")
            lines.append("=" * 40)
            lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
            lines.append("")
            lines.append("METRICS SUMMARY")
            lines.append("-" * 40)
            lines.append(f"Total Runs:              {metrics.get('total_runs', 0)}")
            lines.append(f"Success Rate:            {metrics.get('success_rate', 0):.2%}")
            lines.append(f"Average Duration:        {metrics.get('avg_duration', 0):.1f}s")
            lines.append(f"Median Duration:         {metrics.get('median_duration', 0):.1f}s")
            lines.append(f"Test Pass Rate:          {metrics.get('test_pass_rate', 1.0):.2%}")
            lines.append(f"Total Test Failures:     {metrics.get('total_test_failures', 0)}")
            lines.append("")

            per_wf = metrics.get("per_workflow_metrics", {})
            if per_wf:
                lines.append("WORKFLOW BREAKDOWN")
                lines.append("-" * 40)
                for wf_name, wf_metrics in per_wf.items():
                    lines.append(f"{wf_name}:")
                    lines.append(f"  - Runs: {wf_metrics['runs']}")
                    lines.append(f"  - Success Rate: {wf_metrics['success_rate']:.2%}")
                    lines.append(f"  - Avg Duration: {wf_metrics['avg_duration']:.1f}s")
                    lines.append("")

            lines.append("ANOMALIES DETECTED")
            lines.append("-" * 40)
            if anomalies:
                for a in anomalies:
                    lines.append(f"[{a['severity']}] {a['type']}")
                    lines.append(f"  - {a['description']}")
                    if a.get("recommendation"):
                        lines.append(f"  - Recommendation: {a['recommendation']}")
                    lines.append("")
            else:
                lines.append("None - pipeline is healthy!")
                lines.append("")

            lines.append("OVERALL HEALTH ASSESSMENT")
            lines.append("-" * 40)
            lines.append(f"Health Score: {health_score}/100")
            lines.append(f"Status: {status}")
            lines.append("")
            lines.append("=" * 40)
            lines.append("End of Report")
            lines.append("=" * 40)

            with path.open("w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")

        logging.info(f"{format.upper()} report saved to {output_path}")

    except OSError as e:
        logging.error(f"Failed to write report to {output_path}: {e}")
        raise


# ==============================================================================
# TODO 6: Main Function and CLI (15 points) - Est: 1-1.5 hours
# ==============================================================================

def setup_logging(verbose: bool = False) -> None:
    """
    Configure logging based on verbosity level.

    This function is provided for you.

    Args:
        verbose: If True, enables DEBUG level logging
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    This function is provided for you - it handles CLI argument parsing.
    You can use it as-is, or customize it to add additional arguments.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Monitor CI/CD pipeline health and detect anomalies',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze pipeline data with default config
  %(prog)s sample_data/github_actions_runs.json

  # Generate JSON report
  %(prog)s sample_data/github_actions_runs.json --output report.json --format json

  # Filter by date range
  %(prog)s sample_data/github_actions_runs.json --start-date 2026-02-01 --end-date 2026-02-04

  # Verbose logging
  %(prog)s sample_data/github_actions_runs.json --verbose
"""
    )

    # Positional argument
    parser.add_argument(
        'data_file',
        help='Path to pipeline data JSON file'
    )

    # Optional arguments
    parser.add_argument(
        '--config',
        default='config.json',
        help='Path to configuration file (default: config.json)'
    )

    parser.add_argument(
        '--start-date',
        help='Filter runs from this date (YYYY-MM-DD format)'
    )

    parser.add_argument(
        '--end-date',
        help='Filter runs until this date (YYYY-MM-DD format)'
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
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    return parser.parse_args()


def main() -> int:
    """
    Main entry point for the CI Health Monitor.

    This orchestrates the entire workflow:
    1. Parse command-line arguments
    2. Setup logging
    3. Load configuration
    4. Parse pipeline data
    5. Calculate metrics
    6. Detect anomalies
    7. Generate report

    Returns:
        int: Exit code (0=success, 1=error, 130=user cancelled)
    """
    args = parse_arguments()
    setup_logging(args.verbose)

    try:
        logging.info(f"Loading configuration from {args.config}")
        config = load_config(args.config)

        logging.info(f"Parsing pipeline data from {args.data_file}")
        runs = parse_pipeline_data(args.data_file, args.start_date, args.end_date)
        logging.info(f"Found {len(runs)} workflow runs")

        logging.info("Calculating metrics...")
        metrics = calculate_metrics(runs)
        logging.info(
            f"Success rate: {metrics.get('success_rate', 0):.1%}, "
            f"avg duration: {metrics.get('avg_duration', 0):.1f}s"
        )

        logging.info("Detecting anomalies...")
        anomalies = detect_anomalies(metrics, config, runs)
        critical_count = len([a for a in anomalies if a['severity'] == 'CRITICAL'])
        warning_count = len([a for a in anomalies if a['severity'] == 'WARNING'])

        if anomalies:
            logging.warning(
                f"Found {len(anomalies)} anomalies "
                f"({critical_count} critical, {warning_count} warnings)"
            )
        else:
            logging.info("No anomalies detected - pipeline is healthy!")

        if args.output:
            generate_report(metrics, anomalies, args.output, format=args.format)
            print(f"\n✓ {args.format.upper()} report saved to {args.output}")
        else:
            print_summary(metrics, anomalies)

        return 1 if critical_count > 0 else 0

    except ConfigurationError as e:
        logging.error(f"Configuration error: {e}")
        return 1

    except DataParsingError as e:
        logging.error(f"Data parsing error: {e}")
        return 1

    except KeyboardInterrupt:
        logging.info("Operation cancelled by user")
        return 130

    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        return 1


def print_summary(metrics: dict, anomalies: list) -> None:
    """
    Print a formatted summary of pipeline health to the console.

    This function is provided for you, but you can customize it.

    Args:
        metrics: Dictionary of calculated metrics
        anomalies: List of detected anomalies
    """
    print("\n" + "=" * 70)
    print("CI/CD PIPELINE HEALTH SUMMARY")
    print("=" * 70)
    print()

    # Calculate health score (0-100)
    health_score = 100
    health_score -= len([a for a in anomalies if a.get('severity') == 'CRITICAL']) * 20
    health_score -= len([a for a in anomalies if a.get('severity') == 'WARNING']) * 5
    health_score = max(0, health_score)

    # Determine status
    if health_score >= 80:
        status = "HEALTHY"
    elif health_score >= 60:
        status = "REVIEW_RECOMMENDED"
    else:
        status = "NEEDS_ATTENTION"

    print(f"Health Score: {health_score}/100")
    print(f"Status: {status}")
    print()
    print(f"Total Runs: {metrics.get('total_runs', 0)}")
    print(f"Success Rate: {metrics.get('success_rate', 0):.1%}")
    print(f"Average Duration: {metrics.get('avg_duration', 0):.1f} seconds")
    print(f"Test Pass Rate: {metrics.get('test_pass_rate', 1.0):.1%}")
    print()

    critical_count = len([a for a in anomalies if a.get('severity') == 'CRITICAL'])
    warning_count = len([a for a in anomalies if a.get('severity') == 'WARNING'])

    print(f"Anomalies: {len(anomalies)} total ({critical_count} critical, {warning_count} warnings)")

    if critical_count > 0:
        print()
        print("CRITICAL ISSUES:")
        for anomaly in anomalies:
            if anomaly.get('severity') == 'CRITICAL':
                print(f"  • {anomaly.get('description', 'Unknown issue')}")

    print("=" * 70)


if __name__ == '__main__':
    # Run the main function and exit with its return code
    sys.exit(main())