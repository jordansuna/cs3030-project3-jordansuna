#!/usr/bin/env python3
"""
Module 3 Exercise 4: Exception Handling and Robust Programming
Topics: try-except, custom exceptions, input validation, retry logic
Duration: 60-75 minutes
"""

# ==============================================================================
# EXERCISE OVERVIEW
# ==============================================================================
# This exercise reinforces exception handling concepts from Lecture 3.4:
# - Using try-except blocks effectively
# - Handling specific exception types
# - Creating custom exceptions
# - Input validation
# - Implementing retry logic
# ==============================================================================

import time
from typing import Any


# ==============================================================================
# TODO 1: Safe Division with Exception Handling
# ==============================================================================
# Create a function called safe_divide() that:
# - Takes two parameters: numerator and denominator
# - Returns the division result
# - Catches ZeroDivisionError and returns None
# - Catches TypeError (if non-numeric inputs) and returns None
# - Prints appropriate error messages
#
# Example: safe_divide(10, 2) → 5.0
# Example: safe_divide(10, 0) → None (prints error)

def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 2: Read Integer with Validation
# ==============================================================================
# Create a function called read_integer() that:
# - Takes a prompt string as parameter
# - Prompts user for input using input()
# - Converts input to integer and returns it
# - Catches ValueError if input is not a valid integer
# - Keeps prompting until valid integer is entered
# - For testing, accepts optional 'test_input' parameter
#
# Example: read_integer("Enter number: ")
# Prompts until user enters valid integer

def read_integer(prompt, test_input=None):
    """Read and validate integer input from user."""
    # TODO: Implement this function
    # Hint: Use a while loop until valid input is received
    # For testing: if test_input is provided, use it instead of input()
    pass


# ==============================================================================
# TODO 3: Safe File Reader
# ==============================================================================
# Create a function called safe_file_reader() that:
# - Takes a filename as parameter
# - Tries to open and read the file
# - Returns the file contents as a string
# - Catches FileNotFoundError and returns None
# - Catches PermissionError and returns None
# - Catches UnicodeDecodeError and returns None
# - Uses 'finally' block to ensure cleanup (print "Cleanup complete")
#
# Example: safe_file_reader("data.txt")
# Returns: File contents or None if error

def safe_file_reader(filename):
    """Read file with comprehensive error handling."""
    # TODO: Implement this function
    # Hint: Use try-except-finally structure
    pass


# ==============================================================================
# TODO 4: Validate Email Address
# ==============================================================================
# Create a function called validate_email() that:
# - Takes an email string as parameter
# - Checks if email contains exactly one '@' symbol
# - Checks if there's at least one '.' after the '@'
# - Raises ValueError with descriptive message if invalid
# - Returns True if valid
#
# Example: validate_email("user@example.com") → True
# Example: validate_email("invalid-email") → raises ValueError

def validate_email(email):
    """Validate email format and raise exception if invalid."""
    # TODO: Implement this function
    # Hint: Use raise ValueError("Message") for invalid emails
    pass


# ==============================================================================
# TODO 5: Process Data with Multiple Exceptions
# ==============================================================================
# Create a function called process_data_safely() that:
# - Takes a data dictionary as parameter
# - Tries to:
#   1. Access data['value'] (might raise KeyError)
#   2. Convert it to float (might raise ValueError)
#   3. Divide 100 by it (might raise ZeroDivisionError)
# - Returns the result if successful
# - Catches KeyError and returns "Missing key"
# - Catches ValueError and returns "Invalid value"
# - Catches ZeroDivisionError and returns "Division by zero"
#
# Example: process_data_safely({'value': '10'}) → 10.0
# Example: process_data_safely({'name': 'test'}) → "Missing key"

def process_data_safely(data):
    """Process data with multiple exception handlers."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 6: Custom Exception Class
# ==============================================================================
# Create a custom exception class called DataValidationError that:
# - Inherits from Exception
# - Takes a message and an optional error_code parameter
# - Stores both in instance variables
# - Overrides __str__ to return formatted message
#
# Then create a function called validate_age() that:
# - Takes an age parameter
# - Raises DataValidationError if age < 0 (error_code='NEGATIVE')
# - Raises DataValidationError if age > 150 (error_code='TOO_HIGH')
# - Returns True if valid
#
# Example: validate_age(25) → True
# Example: validate_age(-5) → raises DataValidationError

class DataValidationError(Exception):
    """Custom exception for data validation errors."""
    # TODO: Implement this class
    pass


def validate_age(age):
    """Validate age and raise custom exception if invalid."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 7: Retry Logic with Exceptions
# ==============================================================================
# Create a function called retry_operation() that:
# - Takes a function to call, max_attempts, and delay parameters
# - Tries to call the function up to max_attempts times
# - If function raises an exception, waits 'delay' seconds and retries
# - Returns the function result if successful
# - Raises the last exception if all attempts fail
# - Prints attempt number before each try
#
# Example: retry_operation(lambda: risky_function(), max_attempts=3, delay=1)
# Tries up to 3 times with 1 second delay between attempts

def retry_operation(func, max_attempts=3, delay=1):
    """Retry an operation with exponential backoff."""
    # TODO: Implement this function
    # Hint: Use a for loop and time.sleep(delay)
    pass


# ==============================================================================
# Main function for testing
# ==============================================================================
def main():
    """Main function to test all implementations."""
    print("Module 3 - Exercise 4: Exception Handling and Robust Programming")
    print("=" * 60)
    
    # Test TODO 1
    print("\nTODO 1: safe_divide")
    try:
        result1 = safe_divide(10, 2)
        result2 = safe_divide(10, 0)
        print(f"  10 / 2 = {result1}")
        print(f"  10 / 0 = {result2}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 4
    print("\nTODO 4: validate_email")
    try:
        validate_email("user@example.com")
        print("  ✓ Valid email accepted")
    except ValueError as e:
        print(f"  Error: {e}")
    
    try:
        validate_email("invalid-email")
        print("  ✗ Should have raised ValueError")
    except ValueError:
        print("  ✓ Invalid email rejected")
    
    # Test TODO 5
    print("\nTODO 5: process_data_safely")
    try:
        result1 = process_data_safely({'value': '10'})
        result2 = process_data_safely({'name': 'test'})
        print(f"  Valid data: {result1}")
        print(f"  Missing key: {result2}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n" + "=" * 60)
    print("Run './check_my_work.sh' to validate your solutions")


if __name__ == "__main__":
    main()
