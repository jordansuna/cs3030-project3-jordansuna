#!/usr/bin/env python3
"""Different file reading methods."""

def demonstrate_reading(filename):
    """Show different ways to read files."""
    
    # read() - Read entire file as single string
    with open(filename, 'r') as f:
        content = f.read()
        print(f"Full content length: {len(content)}")
    
    # read(size) - Read specific number of bytes
    with open(filename, 'r') as f:
        chunk = f.read(100)  # Read first 100 characters
        print(f"First 100 chars: {chunk}")
    
    # readline() - Read one line at a time
    with open(filename, 'r') as f:
        first_line = f.readline()
        second_line = f.readline()
        print(f"First line: {first_line.strip()}")
        
     # readlines() - Read all lines into a list
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(f"Total lines: {len(lines)}")
    
    # Iterate directly (most memory efficient)
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")

if __name__ == "__main__":
    demonstrate_reading('sample.txt')    