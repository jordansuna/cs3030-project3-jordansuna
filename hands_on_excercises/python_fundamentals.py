#!/usr/bin/env python3
"""
Module 3 Exercise 1: Python Fundamentals
Topics: Variables, functions, lists, dictionaries, string formatting
Duration: 45-60 minutes
"""

# ==============================================================================
# EXERCISE OVERVIEW
# ==============================================================================
# This exercise reinforces Python fundamentals from Lecture 3.1:
# - Function definition and calling
# - Working with different data types
# - Lists and dictionaries
# - String formatting with f-strings
# - List comprehensions
# - Return values
# ==============================================================================

# ==============================================================================
# TODO 1: Basic Function with String Formatting
# ==============================================================================
# Create a function called greet_user() that:
# - Takes a name (str) as parameter
# - Returns a greeting string using f-string formatting
# - Format: "Hello, {name}! Welcome to Python scripting."
#
# Example: greet_user("Alice")
# Returns: "Hello, Alice! Welcome to Python scripting."

def greet_user(name):
    """Greet a user with their name."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 2: Calculate Statistics from a List
# ==============================================================================
# Create a function called calculate_statistics() that:
# - Takes a list of numbers as a parameter
# - Returns a dictionary with:
#   - 'count': number of elements
#   - 'sum': sum of all numbers
#   - 'average': average of the numbers (sum/count)
#   - 'min': minimum value
#   - 'max': maximum value
# - Handle empty list (return None)
#
# Example: calculate_statistics([10, 20, 30, 40])
# Returns: {'count': 4, 'sum': 100, 'average': 25.0, 'min': 10, 'max': 40}

def calculate_statistics(numbers):
    """Calculate statistics for a list of numbers."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 3: Manage Inventory with Dictionary
# ==============================================================================
# Create a function called manage_inventory() that:
# - Takes two parameters:
#   - inventory: a dictionary of item names and quantities
#   - operation: a string ('add' or 'remove')
#   - item: item name (str)
#   - quantity: amount (int)
# - For 'add': Add quantity to existing or create new entry
# - For 'remove': Subtract quantity (don't go below 0)
# - Return the updated inventory dictionary
#
# Example: manage_inventory({'apples': 5, 'oranges': 3}, 'add', 'apples', 2)
# Returns: {'apples': 7, 'oranges': 3}

def manage_inventory(inventory, operation, item, quantity):
    """Manage inventory by adding or removing items."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 4: Format User Information
# ==============================================================================
# Create a function called format_user_info() that:
# - Takes a dictionary with user information:
#   - 'first_name', 'last_name', 'email', 'age'
# - Returns a formatted string using f-strings:
#   "Name: {first_name} {last_name}, Email: {email}, Age: {age}"
# - All fields should be present (assume valid input)
#
# Example: format_user_info({'first_name': 'John', 'last_name': 'Doe', 
#                            'email': 'john@example.com', 'age': 30})
# Returns: "Name: John Doe, Email: john@example.com, Age: 30"

def format_user_info(user):
    """Format user information as a string."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 5: Filter Even Numbers Using List Comprehension
# ==============================================================================
# Create a function called filter_even_numbers() that:
# - Takes a list of integers as a parameter
# - Uses list comprehension to return a new list with only even numbers
# - Even numbers are divisible by 2 (num % 2 == 0)
#
# Example: filter_even_numbers([1, 2, 3, 4, 5, 6])
# Returns: [2, 4, 6]

def filter_even_numbers(numbers):
    """Filter and return only even numbers from a list."""
    # TODO: Implement this function using list comprehension
    pass


# ==============================================================================
# TODO 6: Find Longest Word in a List
# ==============================================================================
# Create a function called find_longest_word() that:
# - Takes a list of words (strings) as a parameter
# - Returns the longest word
# - If multiple words have same length, return the first one
# - Handle empty list (return None)
#
# Example: find_longest_word(['cat', 'elephant', 'dog', 'bird'])
# Returns: 'elephant'
#
# Hint: Use the len() function and max() or a loop

def find_longest_word(words):
    """Find and return the longest word in a list."""
    # TODO: Implement this function
    pass


# ==============================================================================
# TODO 7: Merge Two Dictionaries
# ==============================================================================
# Create a function called merge_dictionaries() that:
# - Takes two dictionaries as parameters
# - Returns a new dictionary that merges both
# - If keys overlap, values from dict2 should overwrite dict1
# - Use the dictionary unpacking operator (**) or update()
#
# Example: merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# Returns: {'a': 1, 'b': 3, 'c': 4}

def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries, with dict2 taking precedence."""
    # TODO: Implement this function
    pass


# ==============================================================================
# Main function for testing
# ==============================================================================
def main():
    """Main function to test all implementations."""
    print("Module 3 - Exercise 1: Python Fundamentals")
    print("=" * 60)
    
    # Test TODO 1
    print("\nTODO 1: greet_user")
    try:
        result = greet_user("Alice", 25)
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 2
    print("\nTODO 2: calculate_statistics")
    try:
        result = calculate_statistics([10, 20, 30, 40])
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 3
    print("\nTODO 3: manage_inventory")
    try:
        inventory = {'apples': 5, 'oranges': 3}
        result = manage_inventory(inventory, 'add', 'apples', 2)
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 4
    print("\nTODO 4: format_user_info")
    try:
        user = {'first_name': 'John', 'last_name': 'Doe', 
                'email': 'john@example.com', 'age': 30}
        result = format_user_info(user)
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 5
    print("\nTODO 5: filter_even_numbers")
    try:
        result = filter_even_numbers([1, 2, 3, 4, 5, 6])
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 6
    print("\nTODO 6: find_longest_word")
    try:
        result = find_longest_word(['cat', 'elephant', 'dog', 'bird'])
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Test TODO 7
    print("\nTODO 7: merge_dictionaries")
    try:
        result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n" + "=" * 60)
    print("Run './check_my_work.sh' to validate your solutions")


if __name__ == "__main__":
    main()
