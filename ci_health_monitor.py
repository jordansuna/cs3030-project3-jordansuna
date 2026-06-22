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
    # TODO: Implement configuration loading
    #
    # Steps:
    # 1. Convert config_file to Path object
    # 2. Check if file exists, raise ConfigurationError if not
    # 3. Open and read file using 'with' statement
    # 4. Parse JSON using json.load(), catch json.JSONDecodeError
    # 5. Validate required keys exist (thresholds, alert_config)
    # 6. Return config dictionary
    #
    # Hints:
    # - Use Path(config_file).exists() to check file
    # - Use try-except for json.JSONDecodeError
    # - Check keys with: if 'key' not in config: raise ConfigurationError(...)
    # - Remember to close file (or use 'with' statement - it auto-closes!)
    
    pass


# ==============================================================================
# TODO 2: Pipeline Data Parser (15 points) - Est: 2-2.5 hours
# ==============================================================================

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
        
    Example:
        >>> runs = parse_pipeline_data('sample_data/github_actions_runs.json')
        >>> print(len(runs))
        45
        >>> runs_filtered = parse_pipeline_data('sample_data/github_actions_runs.json',
        ...                                      start_date='2026-02-01',
        ...                                      end_date='2026-02-03')
        >>> print(len(runs_filtered))
        28
    """
    # TODO: Implement pipeline data parsing
    #
    # Steps:
    # 1. Read JSON file (similar to load_config)
    # 2. Extract 'workflow_runs' list from data
    # 3. If start_date or end_date provided, filter runs by timestamp
    #    - Parse run timestamp with datetime.fromisoformat()
    #    - Compare with start_date/end_date
    # 4. Validate each run has required fields
    # 5. Return filtered list of runs
    #
    # Hints:
    # - Timestamp format: '2026-02-01T10:30:00Z'
    # - Use datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    # - Required fields: id, workflow, conclusion, duration_seconds, timestamp
    # - Use list comprehension for filtering
    
    pass


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
        
    Example:
        >>> runs = parse_pipeline_data('sample_data/github_actions_runs.json')
        >>> metrics = calculate_metrics(runs)
        >>> print(f"Success Rate: {metrics['success_rate']:.2%}")
        Success Rate: 91.11%
    """
    # TODO: Implement metrics calculation
    #
    # Steps:
    # 1. Handle empty runs list (return dict with total_runs=0)
    # 2. Calculate success rate: successful runs / total runs
    # 3. Calculate duration statistics (average, median, min, max)
    # 4. Calculate test pass rate from test_results
    # 5. Count failures by workflow type
    # 6. Identify slowest and fastest builds
    # 7. Calculate per-workflow metrics
    #
    # Hints:
    # - successful = [r for r in runs if r['conclusion'] == 'success']
    # - durations = [r['duration_seconds'] for r in runs]
    # - median = sorted(durations)[len(durations) // 2]
    # - Group by workflow: use dict to collect runs per workflow
    # - test_results might be missing in some runs - handle with .get()
    
    if not runs:
        return {
            "total_runs": 0,
            "success_rate": 0.0,
            "message": "No runs to analyze"
        }
    
    pass


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
        
    Example:
        >>> anomalies = detect_anomalies(metrics, config, runs)
        >>> for a in anomalies:
        ...     print(f"[{a['severity']}] {a['type']}: {a['description']}")
        [CRITICAL] low_success_rate: Success rate 91.1% below threshold 95.0%
        [WARNING] slow_build: Build 12390 took 780s (threshold: 600s)
    """
    # TODO: Implement anomaly detection
    #
    # Anomaly Types to Detect:
    # 1. Low Success Rate (CRITICAL if < min_success_rate)
    # 2. Slow Builds (WARNING if duration > max_duration_seconds)
    # 3. Failure Streaks (CRITICAL if consecutive failures >= max_failure_streak)
    # 4. Low Test Pass Rate (WARNING if < test_pass_rate_threshold)
    #
    # Steps:
    # 1. Initialize empty anomalies list
    # 2. Check success rate against threshold
    # 3. Find builds exceeding duration threshold
    # 4. Detect consecutive failures per workflow
    # 5. Check test pass rate
    # 6. Return anomalies list
    #
    # Hints:
    # - thresholds = config['thresholds']
    # - Each anomaly dict should have: type, severity, description, affected_runs, recommendation
    # - For failure streaks: group runs by workflow, sort by timestamp, count consecutive failures
    # - Use helpful descriptions: f"Success rate {rate:.1%} below threshold {threshold:.1%}"
    
    anomalies = []
    thresholds = config['thresholds']
    
    pass


# ==============================================================================
# TODO 5: Report Generation (20 points) - Est: 1.5-2 hours
# ==============================================================================

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
        
    Example:
        >>> generate_report(metrics, anomalies, 'report.json', format='json')
        ✓ JSON report saved to report.json
    """
    # TODO: Implement report generation
    #
    # Supported Formats:
    # 1. JSON - Complete data dump with metadata
    # 2. CSV - Summary metrics in table format
    # 3. TEXT - Human-readable formatted report
    #
    # Steps:
    # 1. Convert output_path to Path object
    # 2. Create parent directory if needed (parents=True, exist_ok=True)
    # 3. Build report data with metadata (timestamp, version)
    # 4. Calculate health score (use helper function)
    # 5. Write report in requested format
    # 6. Handle errors with try-except
    # 7. Log success or failure
    #
    # Hints:
    # - JSON: json.dump(data, f, indent=2)
    # - CSV: import csv, use csv.writer
    # - TEXT: Format with f-strings, use '=' * 40 for separators
    # - Create directory: Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    pass


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
    # TODO: Implement the main workflow
    #
    # Step 1: Parse arguments and setup logging (provided for you)
    args = parse_arguments()
    setup_logging(args.verbose)
    
    # Step 2: Wrap everything in try-except for error handling
    try:
        # TODO: Load configuration
        # Call load_config(args.config)
        # Store result in a variable called 'config'
        # logging.info() to tell user what you're doing
        
        # TODO: Parse pipeline data
        # Call parse_pipeline_data() with args.data_file, args.start_date, args.end_date
        # Store result in a variable called 'runs'
        # logging.info() to show how many runs were parsed
        
        # TODO: Calculate metrics
        # Call calculate_metrics(runs)
        # Store result in a variable called 'metrics'
        # logging.info() to show key metrics
        
        # TODO: Detect anomalies
        # Call detect_anomalies(metrics, config, runs)
        # Store result in a variable called 'anomalies'
        # logging.info() to show how many anomalies found
        
        # TODO: Generate report
        # If args.output is provided:
        #   - Call generate_report(metrics, anomalies, args.output, args.format)
        #   - Print success message
        # Else:
        #   - Call print_summary(metrics, anomalies) to show console output
        
        # TODO: Check for critical anomalies and return appropriate exit code
        # Count critical anomalies
        # If critical_count > 0:
        #   - Log a warning about critical issues
        #   - return 1
        # Otherwise return 0
        
        pass  # Remove this once you implement the above
        
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
