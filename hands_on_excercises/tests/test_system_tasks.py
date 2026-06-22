#!/usr/bin/env python3
"""
Test suite for Module 3 Exercise 3: System Tasks
"""

import sys
import os
import tempfile
from pathlib import Path
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import using importlib to avoid numeric import issues
spec = importlib.util.spec_from_file_location(
    "system_tasks_solution",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "system_tasks.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

list_directory_contents = solution_module.list_directory_contents
create_directory_structure = solution_module.create_directory_structure
get_file_info = solution_module.get_file_info
find_files_by_pattern = solution_module.find_files_by_pattern
get_env_var = solution_module.get_env_var
run_shell_command = solution_module.run_shell_command
parse_arguments = solution_module.parse_arguments


def test_list_directory_contents():
    """Test list_directory_contents function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files and directories
        Path(tmpdir, "file1.txt").touch()
        Path(tmpdir, "file2.txt").touch()
        Path(tmpdir, "subdir1").mkdir()
        Path(tmpdir, "subdir2").mkdir()
        
        result = list_directory_contents(tmpdir)
        assert result is not None
        assert len(result['files']) == 2
        assert len(result['directories']) == 2
    
    print("✓ test_list_directory_contents passed")


def test_create_directory_structure():
    """Test create_directory_structure function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir) / "project"
        result = create_directory_structure(str(base), ["src", "docs", "tests"])
        
        assert len(result) == 3
        assert Path(base, "src").exists()
        assert Path(base, "docs").exists()
        assert Path(base, "tests").exists()
    
    print("✓ test_create_directory_structure passed")


def test_get_file_info():
    """Test get_file_info function."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Test content")
        temp_file = f.name
    
    result = get_file_info(temp_file)
    assert result is not None
    assert result['is_file'] == True
    assert result['is_dir'] == False
    assert result['exists'] == True
    assert result['extension'] == '.txt'
    assert result['size_bytes'] > 0
    
    os.unlink(temp_file)
    print("✓ test_get_file_info passed")


def test_find_files_by_pattern():
    """Test find_files_by_pattern function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        Path(tmpdir, "file1.py").touch()
        Path(tmpdir, "file2.txt").touch()
        subdir = Path(tmpdir, "subdir")
        subdir.mkdir()
        Path(subdir, "file3.py").touch()
        
        result = find_files_by_pattern(tmpdir, "*.py")
        assert len(result) == 2
    
    print("✓ test_find_files_by_pattern passed")


def test_get_env_var():
    """Test get_env_var function."""
    # Test with existing env var
    result = get_env_var("PATH", "/default")
    assert result != ""
    
    # Test with non-existent var and default
    result = get_env_var("NONEXISTENT_VAR_12345", "default_value")
    assert result == "default_value"
    
    print("✓ test_get_env_var passed")


def test_run_shell_command():
    """Test run_shell_command function."""
    result = run_shell_command("echo Hello")
    assert result['success'] == True
    assert "Hello" in result['stdout']
    assert result['returncode'] == 0
    
    print("✓ test_run_shell_command passed")


def test_parse_arguments():
    """Test parse_arguments function."""
    result = parse_arguments(['-i', 'input.txt', '-o', 'output.txt', '-v'])
    assert result['input'] == 'input.txt'
    assert result['output'] == 'output.txt'
    assert result['verbose'] == True
    
    result = parse_arguments(['-i', 'in.txt', '-o', 'out.txt'])
    assert result['verbose'] == False
    
    print("✓ test_parse_arguments passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for Exercise 3: System Tasks")
    print("=" * 60)
    
    tests = [
        test_list_directory_contents,
        test_create_directory_structure,
        test_get_file_info,
        test_find_files_by_pattern,
        test_get_env_var,
        test_run_shell_command,
        test_parse_arguments
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
