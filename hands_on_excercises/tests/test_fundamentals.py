#!/usr/bin/env python3
"""
Test suite for Module 3 Exercise 1: Python Fundamentals
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import all functions from the student's exercise module
import importlib.util
spec = importlib.util.spec_from_file_location(
    "fundamentals_solution",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "python_fundamentals.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

# Import functions
greet_user = solution_module.greet_user
calculate_statistics = solution_module.calculate_statistics
manage_inventory = solution_module.manage_inventory
format_user_info = solution_module.format_user_info
filter_even_numbers = solution_module.filter_even_numbers
find_longest_word = solution_module.find_longest_word
merge_dictionaries = solution_module.merge_dictionaries


def test_greet_user():
    """Test greet_user function."""
    assert greet_user("Alice") == "Hello, Alice! Welcome to Python scripting."
    assert greet_user("Bob") == "Hello, Bob! Welcome to Python scripting."
    print("✓ test_greet_user passed")


def test_calculate_statistics():
    """Test calculate_statistics function."""
    result = calculate_statistics([1, 2, 3, 4, 5])
    assert result['sum'] == 15
    assert result['average'] == 3.0
    assert result['min'] == 1
    assert result['max'] == 5
    
    result = calculate_statistics([10, 20, 30])
    assert result['sum'] == 60
    assert result['average'] == 20.0
    print("✓ test_calculate_statistics passed")


def test_manage_inventory():
    """Test manage_inventory function."""
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = manage_inventory(items)
    assert result['apple'] == 3
    assert result['banana'] == 2
    assert result['orange'] == 1
    print("✓ test_manage_inventory passed")


def test_format_user_info():
    """Test format_user_info function."""
    user = {'name': 'Alice', 'age': 30, 'city': 'Seattle'}
    result = format_user_info(user)
    assert "Alice" in result
    assert "30" in result
    assert "Seattle" in result
    print("✓ test_format_user_info passed")


def test_filter_even_numbers():
    """Test filter_even_numbers function."""
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5, 7]) == []
    assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]
    print("✓ test_filter_even_numbers passed")


def test_find_longest_word():
    """Test find_longest_word function."""
    assert find_longest_word(["cat", "elephant", "dog"]) == "elephant"
    assert find_longest_word(["hello", "world"]) == "hello"
    assert find_longest_word(["a", "bb", "ccc"]) == "ccc"
    print("✓ test_find_longest_word passed")


def test_merge_dictionaries():
    """Test merge_dictionaries function."""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    result = merge_dictionaries(dict1, dict2)
    assert result == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    dict1 = {'a': 1}
    dict2 = {'a': 2, 'b': 3}
    result = merge_dictionaries(dict1, dict2)
    assert result['a'] == 2  # dict2 should override
    print("✓ test_merge_dictionaries passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for Exercise 1: Python Fundamentals")
    print("=" * 60)
    
    tests = [
        test_greet_user,
        test_calculate_statistics,
        test_manage_inventory,
        test_format_user_info,
        test_filter_even_numbers,
        test_find_longest_word,
        test_merge_dictionaries
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
