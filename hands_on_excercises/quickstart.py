#!/usr/bin/env python3
"""
Module 3 Quick Win Exercise: Your First Python Automation Script
Duration: 20-30 minutes | Points: 50 | Difficulty: ⭐ Easy

This is your confidence-builder exercise! Complete 3 simple TODOs to get
familiar with Python scripting for automation. If you can do this easily,
you're ready for the main exercises.
"""

import sys
from datetime import datetime


# ==============================================================================
# TODO 1: System Information Function (10 minutes)
# ==============================================================================
# Create a function called get_system_info() that:
#   1. Takes no parameters
#   2. Returns a dictionary with:
#      - 'python_version': the Python version (use sys.version)
#      - 'platform': the operating system (use sys.platform)
#      - 'timestamp': current timestamp (use datetime.now())
#   3. Simply return a dict with these 3 keys
#
# HINT: You already have the imports at the top!
#
# EXAMPLE OUTPUT:
#   {
#     'python_version': '3.11.2 (main...)',
#     'platform': 'linux',
#     'timestamp': datetime.datetime(2026, 2, 3, 14, 30, 45)
#   }
#
# TRY THIS FIRST: Can you create an empty dictionary like this?
#   info = {}
#   info['key'] = 'value'

def get_system_info():
    """Get basic system information."""
    # TODO: Your code here (5-8 lines)
    pass


# ==============================================================================
# TODO 2: Greeting with Time of Day (10 minutes)
# ==============================================================================
# Create a function called greet_with_time() that:
#   1. Takes a name (str) as parameter
#   2. Gets the current hour using datetime.now().hour
#   3. Returns different greetings based on time:
#      - Hour 5-11: "Good morning, {name}!"
#      - Hour 12-16: "Good afternoon, {name}!"
#      - Hour 17-21: "Good evening, {name}!"
#      - Otherwise: "Hello, {name}!"
#   4. Use f-strings for formatting
#
# HINT: Use if-elif-else to check the hour
#
# EXAMPLE:
#   greet_with_time("Alice")  # at 9 AM → "Good morning, Alice!"
#   greet_with_time("Bob")    # at 3 PM → "Good afternoon, Bob!"
#
# TRY THIS FIRST: Can you get the current hour?
#   hour = datetime.now().hour
#   print(hour)  # Should print 0-23

def greet_with_time(name):
    """Greet user based on current time of day."""
    # TODO: Your code here (8-12 lines)
    pass


# ==============================================================================
# TODO 3: Simple File Logger (10 minutes)
# ==============================================================================
# Create a function called log_message() that:
#   1. Takes two parameters: filename (str) and message (str)
#   2. Opens the file in APPEND mode ('a')
#   3. Writes the message with a timestamp
#   4. Format: "[YYYY-MM-DD HH:MM:SS] message\n"
#   5. Returns True on success, False on any error
#   6. Use a try-except block to catch errors
#
# HINT: Use 'with open()' so the file closes automatically
# HINT: datetime.now().strftime("%Y-%m-%d %H:%M:%S") formats timestamps
#
# EXAMPLE:
#   log_message("app.log", "Server started")
#   # Appends to app.log: "[2026-02-03 14:30:45] Server started\n"
#
# TRY THIS FIRST: Can you open a file in append mode?
#   with open("test.txt", "a") as f:
#       f.write("Hello!\n")

def log_message(filename, message):
    """Append a timestamped message to a log file."""
    # TODO: Your code here (8-12 lines)
    pass


# ==============================================================================
# Testing Your Code
# ==============================================================================
def main():
    """Test all your implementations."""
    print("=" * 60)
    print("Module 3 Quick Win Exercise - Testing Your Code")
    print("=" * 60)
    
    # Test TODO 1
    print("\n🧪 Testing TODO 1: get_system_info()")
    try:
        info = get_system_info()
        if info and 'python_version' in info and 'platform' in info:
            print(f"✅ PASS - System info: {info['platform']}")
            print(f"   Python: {info['python_version'][:20]}...")
        else:
            print("❌ FAIL - Missing keys or returned None")
            print("   HINT: Make sure you return a dictionary with all 3 keys")
    except Exception as e:
        print(f"❌ ERROR - {e}")
        print("   HINT: Did you return a dictionary?")
    
    # Test TODO 2
    print("\n🧪 Testing TODO 2: greet_with_time()")
    try:
        greeting = greet_with_time("Alice")
        hour = datetime.now().hour
        if greeting and "Alice" in greeting:
            print(f"✅ PASS - Greeting: {greeting}")
            print(f"   Current hour: {hour}")
        else:
            print("❌ FAIL - Greeting doesn't include the name")
            print("   HINT: Use f-strings like f'Hello, {name}!'")
    except Exception as e:
        print(f"❌ ERROR - {e}")
        print("   HINT: Did you return a string with an f-string?")
    
    # Test TODO 3
    print("\n🧪 Testing TODO 3: log_message()")
    try:
        result = log_message("quickstart_test.log", "Test message")
        if result == True:
            print("✅ PASS - Log written successfully")
            # Try to read it back
            try:
                with open("quickstart_test.log", "r") as f:
                    last_line = f.readlines()[-1]
                    print(f"   Log entry: {last_line.strip()[:50]}...")
            except:
                pass
        else:
            print("❌ FAIL - Function should return True on success")
            print("   HINT: Return True after successfully writing")
    except Exception as e:
        print(f"❌ ERROR - {e}")
        print("   HINT: Did you use try-except to catch file errors?")
    
    # Final message
    print("\n" + "=" * 60)
    print("Testing complete!")
    print("\nNext steps:")
    print("  1. Fix any ❌ failures above")
    print("  2. Run this script again to verify")
    print("  3. When all tests pass, move to file_operations.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
