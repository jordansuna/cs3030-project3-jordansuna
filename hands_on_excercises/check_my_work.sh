#!/bin/bash
#
# Module 3 - Automated Testing Script
# CS 3030 - Scripting Languages
#
# This script validates student solutions for all Module 3 exercises
# and provides comprehensive feedback with scoring.
#
# Usage: ./check_my_work.sh [exercise_number]
#   - No argument: Run all exercises
#   - exercise_number: Run specific exercise (1-4)
#

set -euo pipefail

# Color codes for output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Scoring variables
total_score=0
max_score=400
exercises_completed=0

# ==============================================================================
# Helper Functions
# ==============================================================================

print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# ==============================================================================
# Test Exercise Functions
# ==============================================================================

test_exercise_1() {
    print_header "Exercise 1: Python Fundamentals"
    local score=0
    local max=100
    
    if [ ! -f "$SCRIPT_DIR/python_fundamentals.py" ]; then
        print_error "File not found: python_fundamentals.py"
        return 0
    fi
    
    # Check if Python 3 is available
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        return 0
    fi
    
    # Run the test suite
    print_info "Running tests for Exercise 1..."
    if python3 "$SCRIPT_DIR/tests/test_01_fundamentals.py" > /tmp/test1_output.txt 2>&1; then
        score=100
        print_success "All tests passed!"
        exercises_completed=$((exercises_completed + 1))
    else
        # Parse output for partial credit
        local passed=$(grep -c "✓" /tmp/test1_output.txt || true)
        local total_tests=7
        score=$((passed * 100 / total_tests))
        print_warning "Some tests failed. Passed: $passed/$total_tests"
        
        echo ""
        echo "Test output:"
        cat /tmp/test1_output.txt
    fi
    
    echo ""
    print_info "Score: $score/$max points"
    total_score=$((total_score + score))
    
    return 0
}

test_exercise_2() {
    print_header "Exercise 2: File Operations"
    local score=0
    local max=100
    
    if [ ! -f "$SCRIPT_DIR/file_operations.py" ]; then
        print_error "File not found: file_operations.py"
        return 0
    fi
    
    # Run the test suite
    print_info "Running tests for Exercise 2..."
    if python3 "$SCRIPT_DIR/tests/test_file_operations.py" > /tmp/test2_output.txt 2>&1; then
        score=100
        print_success "All tests passed!"
        exercises_completed=$((exercises_completed + 1))
    else
        local passed=$(grep -c "✓" /tmp/test2_output.txt || true)
        local total_tests=7
        score=$((passed * 100 / total_tests))
        print_warning "Some tests failed. Passed: $passed/$total_tests"
        
        echo ""
        echo "Test output:"
        cat /tmp/test2_output.txt
    fi
    
    echo ""
    print_info "Score: $score/$max points"
    total_score=$((total_score + score))
    
    return 0
}

test_exercise_3() {
    print_header "Exercise 3: System Tasks"
    local score=0
    local max=100
    
    if [ ! -f "$SCRIPT_DIR/system_tasks.py" ]; then
        print_error "File not found: system_tasks.py"
        return 0
    fi
    
    # Run the test suite
    print_info "Running tests for Exercise 3..."
    if python3 "$SCRIPT_DIR/tests/test_system_tasks.py" > /tmp/test3_output.txt 2>&1; then
        score=100
        print_success "All tests passed!"
        exercises_completed=$((exercises_completed + 1))
    else
        local passed=$(grep -c "✓" /tmp/test3_output.txt || true)
        local total_tests=7
        score=$((passed * 100 / total_tests))
        print_warning "Some tests failed. Passed: $passed/$total_tests"
        
        echo ""
        echo "Test output:"
        cat /tmp/test3_output.txt
    fi
    
    echo ""
    print_info "Score: $score/$max points"
    total_score=$((total_score + score))
    
    return 0
}

test_exercise_4() {
    print_header "Exercise 4: Exception Handling"
    local score=0
    local max=100
    
    if [ ! -f "$SCRIPT_DIR/exception_handling.py" ]; then
        print_error "File not found: exception_handling.py"
        return 0
    fi
    
    # Run the test suite
    print_info "Running tests for Exercise 4..."
    if python3 "$SCRIPT_DIR/tests/test_exception_handling.py" > /tmp/test4_output.txt 2>&1; then
        score=100
        print_success "All tests passed!"
        exercises_completed=$((exercises_completed + 1))
    else
        local passed=$(grep -c "✓" /tmp/test4_output.txt || true)
        local total_tests=8
        score=$((passed * 100 / total_tests))
        print_warning "Some tests failed. Passed: $passed/$total_tests"
        
        echo ""
        echo "Test output:"
        cat /tmp/test4_output.txt
    fi
    
    echo ""
    print_info "Score: $score/$max points"
    total_score=$((total_score + score))
    
    return 0
}

# ==============================================================================
# Main Script Logic
# ==============================================================================

main() {
    clear
    
    print_header "Module 3 - Python Scripting Exercises"
    echo "Automated Testing and Grading System"
    echo ""
    
    # Check for specific exercise or run all
    if [ $# -eq 1 ]; then
        case $1 in
            1) test_exercise_1 ;;
            2) test_exercise_2 ;;
            3) test_exercise_3 ;;
            4) test_exercise_4 ;;
            *)
                print_error "Invalid exercise number. Use 1-4."
                exit 1
                ;;
        esac
    else
        # Run all exercises
        test_exercise_1
        echo ""
        test_exercise_2
        echo ""
        test_exercise_3
        echo ""
        test_exercise_4
    fi
    
    # Print final summary
    echo ""
    print_header "Final Results"
    echo ""
    echo "Exercises Completed: $exercises_completed/4"
    echo "Total Score: $total_score/$max_score points"
    
    # Calculate percentage
    local percentage=$((total_score * 100 / max_score))
    echo "Percentage: $percentage%"
    echo ""
    
    # Grade interpretation
    if [ $percentage -ge 90 ]; then
        print_success "Excellent work! Grade: A"
    elif [ $percentage -ge 80 ]; then
        print_success "Great job! Grade: B"
    elif [ $percentage -ge 70 ]; then
        print_warning "Good effort! Grade: C"
    elif [ $percentage -ge 60 ]; then
        print_warning "Passing. Grade: D"
    else
        print_error "Needs improvement. Grade: F"
    fi
    
    echo ""
    print_info "Review your code and test output above for areas to improve."
    echo ""
    
    # Clean up temp files
    rm -f /tmp/test{1,2,3,4}_output.txt
}

# Run main function
main "$@"
