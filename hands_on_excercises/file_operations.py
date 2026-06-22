#!/usr/bin/env python3
"""
Module 3 Exercise 2: File I/O and Text Processing
Topics: Reading/writing files, CSV, JSON, error handling
Duration: 60-75 minutes
"""

# ==============================================================================
# EXERCISE OVERVIEW
# ==============================================================================
# This exercise reinforces file I/O concepts from Lecture 3.2:
# - Reading and writing files with context managers
# - Processing text files line-by-line
# - CSV file handling
# - JSON file operations
# - File error handling
# ==============================================================================

import csv
import json
from datetime import datetime


# ==============================================================================
# TODO 1: Read File Safely with Error Handling
# ==============================================================================
# Create a function called read_file_safely() that:
# - Takes a filename as parameter
# - Tries to read and return the file contents
# - Uses 'with' statement and utf-8 encoding
# - Catches FileNotFoundError and PermissionError
# - Returns None if error occurs, prints error message
#
# Example: read_file_safely("data.txt")
# Returns: File contents as string, or None if error

def read_file_safely(filename):
    """Read file contents safely with error handling."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 2: Append Log Entry with Timestamp
# ==============================================================================
# Create a function called write_log_entry() that:
# - Takes a log_file path and message as parameters
# - Appends the message to the file with a timestamp
# - Format: "[YYYY-MM-DD HH:MM:SS] message\n"
# - Uses 'with' statement and append mode ('a')
# - Returns True on success, False on error
#
# Example: write_log_entry("app.log", "Server started")
# Appends: "[2026-02-03 10:30:45] Server started\n"

def write_log_entry(log_file, message):
    """Append a timestamped log entry to a file."""
    # TODO: Implement this function
    # Hint: Use datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pass


# ==============================================================================
# TODO 3: Count Words in File
# ==============================================================================
# Create a function called count_words_in_file() that:
# - Takes a filename as parameter
# - Reads the file and counts total words
# - Returns a dictionary with:
#   - 'word_count': total number of words
#   - 'line_count': total number of lines
#   - 'char_count': total number of characters
# - Splits words by whitespace
# - Returns None if file not found
#
# Example: count_words_in_file("text.txt")
# Returns: {'word_count': 150, 'line_count': 10, 'char_count': 800}

def count_words_in_file(filename):
    """Count words, lines, and characters in a file."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 4: Process CSV Data
# ==============================================================================
# Create a function called process_csv_data() that:
# - Takes a CSV filename as parameter
# - Reads the CSV file using csv.DictReader
# - Returns a list of dictionaries (one per row)
# - Handles FileNotFoundError
# - Returns empty list if error
#
# Example: process_csv_data("users.csv")
# Returns: [{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': '30'}]

def process_csv_data(filename):
    """Read and return CSV data as list of dictionaries."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 5: Read JSON Configuration
# ==============================================================================
# Create a function called read_json_config() that:
# - Takes a JSON filename as parameter
# - Reads and parses the JSON file
# - Returns the parsed data (usually a dictionary)
# - Handles FileNotFoundError and json.JSONDecodeError
# - Returns None if error occurs
#
# Example: read_json_config("config.json")
# Returns: {'host': 'localhost', 'port': 8080}

def read_json_config(filename):
    """Read and parse a JSON configuration file."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 6: Write JSON Report
# ==============================================================================
# Create a function called write_json_report() that:
# - Takes a filename and a data dictionary as parameters
# - Writes the data to a JSON file with nice formatting
# - Uses indent=2 for pretty printing
# - Returns True on success, False on error
#
# Example: write_json_report("report.json", {'status': 'complete', 'count': 100})
# Creates: Formatted JSON file

def write_json_report(filename, data):
    """Write data to a JSON file with formatting."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 7: Filter Log File for Errors
# ==============================================================================
# Create a function called filter_log_file() that:
# - Takes an input_file and output_file as parameters
# - Reads input_file line by line
# - Writes only lines containing "ERROR" to output_file
# - Case-insensitive search (check for "error", "Error", "ERROR")
# - Returns count of error lines found
#
# Example: filter_log_file("app.log", "errors.log")
# Returns: 15 (if 15 error lines were found)

def filter_log_file(input_file, output_file):
    """Filter log file to extract only error lines."""
    # TODO: Implement this function
    # Hint: Use 'ERROR' in line.upper() for case-insensitive check
    pass


# ==============================================================================
# Main function for testing
# ==============================================================================
def main():
    """Main function to test all implementations."""
    print("Module 3 - Exercise 2: File I/O and Text Processing")
    print("=" * 60)
    
    # Create test files
    with open('test_file.txt', 'w') as f:
        f.write("Hello, World!\nPython is great.\n")
    
    # Test TODO 1
    print("\nTODO 1: read_file_safely")
    try:
        result = read_file_safely("test_file.txt")
        print(f"  Result: {result[:30]}..." if result else "  Result: None")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 2
    print("\nTODO 2: write_log_entry")
    try:
        result = write_log_entry("test.log", "Test message")
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 3
    print("\nTODO 3: count_words_in_file")
    try:
        result = count_words_in_file("test_file.txt")
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n" + "=" * 60)
    print("Run './check_my_work.sh' to validate your solutions")


if __name__ == "__main__":
    main()
