# Module 3: Hands-On Exercises - Python Scripting Fundamentals

**Focus:** Python Scripting, File I/O, System Tasks, and Exception Handling  
**Duration:** Weeks 5-6  
**Testing:** Automated with `./check_my_work.sh`

---

## 📚 Overview

These exercises reinforce **Python scripting concepts** from Module 3 lectures. Each exercise builds practical automation skills using Python for system administration and DevOps tasks.

**Learning Approach:**
1. Complete TODOs in order (they build on each other)
2. Test frequently with `./check_my_work.sh` or individual test files
3. Reference solutions/ only after attempting yourself
4. Focus on understanding Python fundamentals and best practices

---

## 📋 Exercise List

### 🎯 Exercise 0: Quick Win - Python Basics ⭐ (START HERE!)
**File:** `quickstart.py`  
**Duration:** 20-30 minutes  
**Points:** 50
**Difficulty:** Easy 🟢

**Purpose:** Build confidence with a quick success before tackling larger exercises.

**Topics:**
- Basic functions with return values
- Working with time/date in Python
- Simple file writing
- Built-in testing

**TODOs:** (Only 3!)
1. ✅ get_system_info - Return dictionary with system information
2. ✅ greet_with_time - Return time-based greeting
3. ✅ log_message - Write message to file with timestamp

**Why Start Here:**
- ✅ Only 3 TODOs (vs 7 in other exercises)
- ✅ Realistic 20-30 minute completion time
- ✅ Immediate success builds confidence
- ✅ Tests built into the script (no separate test file)

**Test Your Work:**
```bash
python3 quickstart.py
# Should see all tests pass!
```

**After Completing:** You're ready for the full exercises below! 🚀

---

### Exercise 1: Python Fundamentals ⭐
**File:** `python_fundamentals.py`  
**Duration:** 45-60 minutes  
**Points:** 100

**Topics:**
- Python script structure
- Variables and data types
- Lists and dictionaries
- Functions with parameters and return values
- String formatting and manipulation
- Basic control flow

**TODOs:**
1. ✅ greet_user - Basic function with string formatting
2. ✅ calculate_statistics - Work with lists and math operations
3. ✅ manage_inventory - Dictionary operations
4. ✅ format_user_info - String formatting with f-strings
5. ✅ filter_even_numbers - List comprehension
6. ✅ find_longest_word - String processing
7. ✅ merge_dictionaries - Dictionary merging

**Common Pitfalls:**
- Forgetting to use `if __name__ == "__main__":` guard
- Not returning values from functions
- Modifying lists while iterating over them
- Using `==` vs `is` for comparison

**Test Your Work:**
```bash
./check_my_work.sh
# or test just fundamentals:
python3 tests/test_fundamentals.py
```

---

### Exercise 2: File I/O and Text Processing ⭐
**File:** `file_operations.py`  
**Duration:** 60-75 minutes  
**Points:** 100

**Topics:**
- Reading and writing files with `with` statements
- Line-by-line file processing
- CSV file handling
- JSON file operations
- File encoding
- Error handling for file operations

**TODOs:**
1. ✅ read_file_safely - Read file with error handling
2. ✅ write_log_entry - Append to log file with timestamp
3. ✅ count_words_in_file - Text analysis
4. ✅ process_csv_data - Read and analyze CSV files
5. ✅ read_json_config - Parse JSON configuration
6. ✅ write_json_report - Generate JSON output
7. ✅ filter_log_file - Extract specific log entries

**Common Pitfalls:**
- Not using `with` statements (files not closed properly)
- Forgetting to specify encoding (use `encoding='utf-8'`)
- Not handling FileNotFoundError and PermissionError
- Using `read()` on large files instead of line-by-line processing

**Test Your Work:**
```bash
./check_my_work.sh
# or test just file operations:
python3 tests/test_file_operations.py
```

---

### Exercise 3: System Interaction (os, sys, subprocess) ⭐
**File:** `system_tasks.py`  
**Duration:** 60-75 minutes  
**Points:** 100

**Topics:**
- Using `os` module for filesystem operations
- Path manipulation with `pathlib`
- Environment variables
- Running external commands with `subprocess`
- Command-line argument parsing
- Exit codes

**TODOs:**
1. ✅ list_directory_contents - Use os.listdir() and os.path
2. ✅ create_directory_structure - Create nested directories
3. ✅ get_file_info - Retrieve file metadata with os.stat()
4. ✅ find_files_by_extension - Walk directory tree
5. ✅ get_environment_variable - Read env vars with defaults
6. ✅ run_shell_command - Execute commands with subprocess
7. ✅ parse_command_args - Use argparse for CLI

**Common Pitfalls:**
- Using string concatenation for paths instead of `os.path.join()` or `pathlib`
- Not checking if files/directories exist before operations
- Using `shell=True` in subprocess (security risk)
- Forgetting to handle subprocess exceptions

**Test Your Work:**
```bash
./check_my_work.sh
# or test just system tasks:
python3 tests/test_system_tasks.py
```

---

### Exercise 4: Exception Handling and Robustness ⭐
**File:** `exception_handling.py`  
**Duration:** 60-75 minutes  
**Points:** 100

**Topics:**
- try-except-finally blocks
- Catching specific exception types
- Custom exceptions
- Error messages and logging
- Defensive programming
- Input validation

**TODOs:**
1. ✅ safe_divide - Handle ZeroDivisionError
2. ✅ read_integer_from_user - Validate user input
3. ✅ safe_file_reader - Comprehensive file error handling
4. ✅ validate_email - Input validation with exceptions
5. ✅ process_data_safely - Multiple exception types
6. ✅ create_custom_exception - Define custom exception class
7. ✅ retry_operation - Implement retry logic with exceptions

**Common Pitfalls:**
- Catching too broad exceptions (use `except Exception` sparingly)
- Not providing helpful error messages
- Swallowing exceptions without logging
- Not cleaning up resources in `finally` blocks

**Test Your Work:**
```bash
./check_my_work.sh
# or test just exception handling:
python3 tests/test_exception_handling.py
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+ installed
- Basic understanding of Python syntax
- Completed Module 3 lectures

### Setup
```bash
# Navigate to module03 exercises
cd hands_on_excercises/module03

# Make check script executable
chmod +x check_my_work.sh

# Run all tests to see initial status
./check_my_work.sh
```

### Working on Exercises

1. **Start with Exercise 1** and complete TODOs in order
2. **Test frequently:**
   ```bash
   # Run all tests
   ./check_my_work.sh
   
   # Run specific exercise test
   python3 tests/test_fundamentals.py
   ```
3. **Check your score:**
   ```bash
   ./check_my_work.sh --summary
   ```

---

## 📝 Scoring

Each exercise is worth **100 points** based on:
- **Correctness** (70%): Does it work as specified?
- **Code Quality** (20%): Proper formatting, naming, structure
- **Error Handling** (10%): Appropriate exception handling

**Total Possible:** 400 points

---

## 💡 Tips for Success

### Python Best Practices
1. **Use meaningful variable names**: `user_count` not `uc`
2. **Follow PEP 8**: Consistent style and formatting
3. **Write docstrings**: Document your functions
4. **Use `with` statements**: For files and resources
5. **Handle exceptions**: Don't let scripts crash unexpectedly

### Common Python Patterns
```python
# Reading files safely
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Line-by-line processing
with open('file.txt', 'r') as f:
    for line in f:
        process(line.strip())

# Exception handling
try:
    result = risky_operation()
except SpecificError as e:
    handle_error(e)
finally:
    cleanup()

# Command-line arguments
import argparse
parser = argparse.ArgumentParser(description='...')
parser.add_argument('filename', help='...')
args = parser.parse_args()
```

### Debugging Tips
1. **Use print statements** to see variable values
2. **Test functions individually** before combining
3. **Check error messages carefully** - they tell you what's wrong
4. **Use Python's interactive mode** (`python3` then type code)
5. **Read the TODO comments** - they contain important hints

---

## 🔍 Testing Details

### Automated Testing
The `check_my_work.sh` script runs all tests and provides:
- ✅ Which TODOs are complete
- ❌ Which TODOs have issues
- 💯 Your current score
- 📊 Summary by exercise

### Test Files
- `tests/test_fundamentals.py` - Tests for Exercise 1
- `tests/test_file_operations.py` - Tests for Exercise 2
- `tests/test_system_tasks.py` - Tests for Exercise 3
- `tests/test_exception_handling.py` - Tests for Exercise 4

### Running Individual Tests
```bash
# Run specific test file
python3 tests/test_fundamentals.py

# Run with verbose output
python3 tests/test_fundamentals.py -v

# Run specific test function
python3 -m pytest tests/test_fundamentals.py::test_greet_user -v
```

---

## 📚 Additional Resources

### Python Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP 8 Style Guide](https://pep8.org/)

### File I/O
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [CSV Module](https://docs.python.org/3/library/csv.html)
- [JSON Module](https://docs.python.org/3/library/json.html)

### System Operations
- [os Module](https://docs.python.org/3/library/os.html)
- [pathlib Module](https://docs.python.org/3/library/pathlib.html)
- [subprocess Module](https://docs.python.org/3/library/subprocess.html)

### Exception Handling
- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

---

## 🆘 Getting Help

### When You're Stuck
1. **Re-read the TODO comments** - they have specific requirements
2. **Review the corresponding lecture** - examples are there
3. **Check the test error messages** - they tell you what's expected
4. **Look at Python documentation** - for module usage
5. **Ask in Slack** - describe what you've tried

### Questions to Ask
✅ "I'm getting a FileNotFoundError in TODO 2. How do I check if a file exists?"  
✅ "What's the difference between `read()` and `readlines()`?"  
✅ "My function returns None instead of the expected value. What am I missing?"  

❌ "Can someone give me the answer for TODO 3?"  
❌ "I don't understand anything, please help."  

---

## ✅ Completion Checklist

Before considering exercises complete:

- [ ] All 28 TODOs implemented across 4 exercises
- [ ] All tests passing (`./check_my_work.sh` shows 400/400)
- [ ] Code follows Python best practices (PEP 8)
- [ ] Functions have proper docstrings
- [ ] Error handling implemented where appropriate
- [ ] No hardcoded paths or values (use parameters)
- [ ] Scripts are executable with proper shebang
- [ ] Tested with various inputs including edge cases

---

## 🎯 Learning Outcomes

After completing these exercises, you will be able to:

✅ Write well-structured Python scripts  
✅ Perform file I/O operations safely  
✅ Process CSV and JSON data  
✅ Interact with the operating system using Python  
✅ Handle exceptions gracefully  
✅ Parse command-line arguments  
✅ Build robust automation tools  

These skills are **essential** for DevOps, system administration, and automation roles.

---

**Good luck! Remember: The goal is to learn, not just to complete. Understand each concept before moving forward.**
