#!/usr/bin/env python3
"""
Test suite for Module 3 Exercise 4: Exception Handling
"""

import sys
import os
import tempfile
from pathlib import Path
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import using importlib to avoid numeric import issues
spec = importlib.util.spec_from_file_location(
    "exception_solution",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "exception_handling.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

safe_divide = solution_module.safe_divide
read_integer = solution_module.read_integer
safe_file_reader = solution_module.safe_file_reader
validate_email = solution_module.validate_email
process_data_safely = solution_module.process_data_safely
DataValidationError = solution_module.DataValidationError
validate_age = solution_module.validate_age
retry_operation = solution_module.retry_operation


def test_safe_divide():
    """Test safe_divide function."""
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    assert safe_divide("10", 2) is None
    print("✓ test_safe_divide passed")


def test_read_integer():
    """Test read_integer function."""
    result = read_integer("Test: ", test_input="42")
    assert result == 42
    
    result = read_integer("Test: ", test_input="-10")
    assert result == -10
    
    print("✓ test_read_integer passed")


def test_safe_file_reader():
    """Test safe_file_reader function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Test content")
        temp_file = f.name
    
    result = safe_file_reader(temp_file)
    assert result == "Test content"
    
    # Test non-existent file
    result = safe_file_reader("/nonexistent/file.txt")
    assert result is None
    
    os.unlink(temp_file)
    print("✓ test_safe_file_reader passed")


def test_validate_email():
    """Test validate_email function."""
    assert validate_email("user@example.com") == True
    assert validate_email("test.user@company.co.uk") == True
    
    try:
        validate_email("invalid-email")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        validate_email("no-at-sign.com")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("✓ test_validate_email passed")


def test_process_data_safely():
    """Test process_data_safely function."""
    assert process_data_safely({'value': '10'}) == 10.0
    assert process_data_safely({'name': 'test'}) == "Missing key"
    assert process_data_safely({'value': 'abc'}) == "Invalid value"
    assert process_data_safely({'value': '0'}) == "Division by zero"
    print("✓ test_process_data_safely passed")


def test_data_validation_error():
    """Test DataValidationError class."""
    error = DataValidationError("Test error", error_code="TEST")
    assert "TEST" in str(error)
    assert "Test error" in str(error)
    print("✓ test_data_validation_error passed")


def test_validate_age():
    """Test validate_age function."""
    assert validate_age(25) == True
    assert validate_age(0) == True
    assert validate_age(150) == True
    
    try:
        validate_age(-5)
        assert False, "Should have raised DataValidationError"
    except DataValidationError as e:
        assert e.error_code == 'NEGATIVE'
    
    try:
        validate_age(200)
        assert False, "Should have raised DataValidationError"
    except DataValidationError as e:
        assert e.error_code == 'TOO_HIGH'
    
    print("✓ test_validate_age passed")


def test_retry_operation():
    """Test retry_operation function."""
    call_count = [0]
    
    def flaky_function():
        call_count[0] += 1
        if call_count[0] < 3:
            raise Exception("Temporary error")
        return "Success"
    
    result = retry_operation(flaky_function, max_attempts=3, delay=0.1)
    assert result == "Success"
    assert call_count[0] == 3
    
    print("✓ test_retry_operation passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for Exercise 4: Exception Handling")
    print("=" * 60)
    
    tests = [
        test_safe_divide,
        test_read_integer,
        test_safe_file_reader,
        test_validate_email,
        test_process_data_safely,
        test_data_validation_error,
        test_validate_age,
        test_retry_operation
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
