#!/usr/bin/env python3
"""
Test suite for Module 3 Exercise 2: File Operations
"""

import sys
import os
import tempfile
import csv
import json
from pathlib import Path
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import using importlib to avoid numeric import issues
spec = importlib.util.spec_from_file_location(
    "file_ops_solution",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "file_operations.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

read_file_safely = solution_module.read_file_safely
write_log_entry = solution_module.write_log_entry
count_words_in_file = solution_module.count_words_in_file
process_csv_data = solution_module.process_csv_data
read_json_config = solution_module.read_json_config
write_json_report = solution_module.write_json_report
filter_log_file = solution_module.filter_log_file


def test_read_file_safely():
    """Test read_file_safely function."""
    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Test content")
        temp_file = f.name
    
    result = read_file_safely(temp_file)
    assert result == "Test content"
    
    # Test non-existent file
    result = read_file_safely("/nonexistent/file.txt")
    assert result is None
    
    os.unlink(temp_file)
    print("✓ test_read_file_safely passed")


def test_write_log_entry():
    """Test write_log_entry function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        temp_log = f.name
    
    result = write_log_entry(temp_log, "Test message")
    assert result == True
    
    content = Path(temp_log).read_text()
    assert "Test message" in content
    assert "[" in content  # Timestamp present
    
    os.unlink(temp_log)
    print("✓ test_write_log_entry passed")


def test_count_words_in_file():
    """Test count_words_in_file function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Hello world\nPython scripting\n")
        temp_file = f.name
    
    result = count_words_in_file(temp_file)
    assert result['word_count'] == 4
    assert result['line_count'] > 0
    
    os.unlink(temp_file)
    print("✓ test_count_words_in_file passed")


def test_process_csv_data():
    """Test process_csv_data function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age'])
        writer.writeheader()
        writer.writerow({'name': 'Alice', 'age': '25'})
        writer.writerow({'name': 'Bob', 'age': '30'})
        temp_csv = f.name
    
    result = process_csv_data(temp_csv)
    assert len(result) == 2
    assert result[0]['name'] == 'Alice'
    
    os.unlink(temp_csv)
    print("✓ test_process_csv_data passed")


def test_read_json_config():
    """Test read_json_config function."""
    test_data = {'host': 'localhost', 'port': 8080}
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(test_data, f)
        temp_json = f.name
    
    result = read_json_config(temp_json)
    assert result == test_data
    
    os.unlink(temp_json)
    print("✓ test_read_json_config passed")


def test_write_json_report():
    """Test write_json_report function."""
    test_data = {'status': 'complete', 'count': 100}
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as f:
        temp_json = f.name
    
    result = write_json_report(temp_json, test_data)
    assert result == True
    
    with open(temp_json, 'r') as f:
        loaded = json.load(f)
    assert loaded == test_data
    
    os.unlink(temp_json)
    print("✓ test_write_json_report passed")


def test_filter_log_file():
    """Test filter_log_file function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        f.write("INFO: Starting\n")
        f.write("ERROR: Connection failed\n")
        f.write("INFO: Retrying\n")
        f.write("error: Auth failed\n")
        input_log = f.name
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.log') as f:
        output_log = f.name
    
    result = filter_log_file(input_log, output_log)
    assert result == 2
    
    os.unlink(input_log)
    os.unlink(output_log)
    print("✓ test_filter_log_file passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for Exercise 2: File Operations")
    print("=" * 60)
    
    tests = [
        test_read_file_safely,
        test_write_log_entry,
        test_count_words_in_file,
        test_process_csv_data,
        test_read_json_config,
        test_write_json_report,
        test_filter_log_file
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
