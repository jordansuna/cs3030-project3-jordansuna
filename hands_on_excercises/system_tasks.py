#!/usr/bin/env python3
"""
Module 3 Exercise 3: System Interaction and Automation
Topics: os, sys, pathlib, subprocess, command-line arguments
Duration: 60-75 minutes
"""

# ==============================================================================
# EXERCISE OVERVIEW
# ==============================================================================
# This exercise reinforces system interaction concepts from Lecture 3.3:
# - Working with file paths using pathlib
# - Environment variables
# - Running system commands with subprocess
# - Command-line argument parsing with argparse
# ==============================================================================

import os
import sys
from pathlib import Path
import subprocess
import argparse


# ==============================================================================
# TODO 1: List Directory Contents
# ==============================================================================
# Create a function called list_directory_contents() that:
# - Takes a directory path as parameter
# - Uses pathlib.Path to list all files and directories
# - Returns a dictionary with:
#   - 'files': list of file names (not directories)
#   - 'directories': list of directory names
# - Returns None if path doesn't exist
#
# Example: list_directory_contents("/home/user")
# Returns: {'files': ['file1.txt', 'file2.py'], 'directories': ['docs', 'src']}

def list_directory_contents(dir_path):
    """List files and directories separately."""
    # TODO: Implement this function
    # Hint: Use Path(dir_path).iterdir() and check .is_file() vs .is_dir()
    pass


# ==============================================================================
# TODO 2: Create Directory Structure
# ==============================================================================
# Create a function called create_directory_structure() that:
# - Takes a base path and a list of subdirectories
# - Creates all subdirectories under the base path
# - Uses pathlib with parents=True, exist_ok=True
# - Returns list of created directory paths (as strings)
# - Returns empty list if error occurs
#
# Example: create_directory_structure("project", ["src", "docs", "tests"])
# Creates: project/src, project/docs, project/tests
# Returns: ['project/src', 'project/docs', 'project/tests']

def create_directory_structure(base_path, subdirs):
    """Create a directory structure with subdirectories."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 3: Get File Information
# ==============================================================================
# Create a function called get_file_info() that:
# - Takes a file path as parameter
# - Uses pathlib.Path.stat() to get file information
# - Returns a dictionary with:
#   - 'size_bytes': file size in bytes
#   - 'is_file': True if it's a file
#   - 'is_dir': True if it's a directory
#   - 'exists': True if path exists
#   - 'extension': file extension (e.g., '.txt')
# - Returns None if path doesn't exist
#
# Example: get_file_info("data.txt")
# Returns: {'size_bytes': 1024, 'is_file': True, 'is_dir': False, 
#           'exists': True, 'extension': '.txt'}

def get_file_info(file_path):
    """Get detailed information about a file or directory."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 4: Find Files by Pattern
# ==============================================================================
# Create a function called find_files_by_pattern() that:
# - Takes a directory path and a pattern (like "*.py")
# - Uses pathlib.Path.glob() to find matching files
# - Returns a list of matching file paths (as strings)
# - Searches recursively using rglob()
# - Returns empty list if directory doesn't exist
#
# Example: find_files_by_pattern("src", "*.py")
# Returns: ['src/main.py', 'src/utils/helpers.py']

def find_files_by_pattern(dir_path, pattern):
    """Find all files matching a pattern recursively."""
    # TODO: Implement this function
    # Hint: Use Path(dir_path).rglob(pattern)
    pass


# ==============================================================================
# TODO 5: Get Environment Variable with Default
# ==============================================================================
# Create a function called get_env_var() that:
# - Takes a variable name and an optional default value
# - Uses os.environ.get() to retrieve the environment variable
# - Returns the value if it exists, otherwise returns default
# - If no default provided, use empty string ""
#
# Example: get_env_var("HOME", "/default/home")
# Returns: "/home/user" (if HOME is set) or "/default/home"

def get_env_var(var_name, default=""):
    """Get an environment variable with a default value."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 6: Run Shell Command
# ==============================================================================
# Create a function called run_shell_command() that:
# - Takes a command (as a string) to execute
# - Uses subprocess.run() with capture_output=True, text=True
# - Returns a dictionary with:
#   - 'stdout': standard output
#   - 'stderr': standard error
#   - 'returncode': exit code
#   - 'success': True if returncode == 0
# - Splits the command string into a list for subprocess
#
# Example: run_shell_command("echo Hello")
# Returns: {'stdout': 'Hello\n', 'stderr': '', 'returncode': 0, 'success': True}

def run_shell_command(command):
    """Execute a shell command and return its output."""
    # TODO: Implement this function
    # Hint: command.split() to convert string to list
    pass


# ==============================================================================
# TODO 7: Parse Command-Line Arguments
# ==============================================================================
# Create a function called parse_arguments() that:
# - Uses argparse to define these arguments:
#   - '--input' or '-i': Input file (required)
#   - '--output' or '-o': Output file (required)
#   - '--verbose' or '-v': Verbose mode (optional flag, default False)
# - Returns the parsed arguments as a dictionary
# - Takes an optional args_list parameter for testing (default None uses sys.argv)
#
# Example: parse_arguments(['-i', 'in.txt', '-o', 'out.txt', '-v'])
# Returns: {'input': 'in.txt', 'output': 'out.txt', 'verbose': True}

def parse_arguments(args_list=None):
    """Parse command-line arguments for a script."""
    # TODO: Implement this function
    # Hint: Use argparse.ArgumentParser()
    # For testing, pass args to parser.parse_args(args_list)
    pass


# ==============================================================================
# Main function for testing
# ==============================================================================
def main():
    """Main function to test all implementations."""
    print("Module 3 - Exercise 3: System Interaction and Automation")
    print("=" * 60)
    
    # Test TODO 1
    print("\nTODO 1: list_directory_contents")
    try:
        result = list_directory_contents(".")
        print(f"  Result: {len(result.get('files', []))} files, {len(result.get('directories', []))} dirs" if result else "  Result: None")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 2
    print("\nTODO 2: create_directory_structure")
    try:
        result = create_directory_structure("test_project", ["src", "docs"])
        print(f"  Result: {len(result)} directories created")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 5
    print("\nTODO 5: get_env_var")
    try:
        result = get_env_var("HOME", "/default")
        print(f"  HOME = {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n" + "=" * 60)
    print("Run './check_my_work.sh' to validate your solutions")


if __name__ == "__main__":
    main()
