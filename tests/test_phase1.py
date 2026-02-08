"""
Tests for Phase 1: Foundation
=============================

This module contains unit tests for the Phase 1 components.

These tests verify that our AST parser and utilities work correctly.
"""

import sys
import os

# Add parent directory to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from phase1_foundation.ast_parser import ASTParser, parse_code
from phase1_foundation.utils import (
    count_lines_of_code,
    count_non_empty_lines,
    count_comment_lines,
    get_average_line_length
)

def test_basic_parsing():
    """Test basic code parsing."""
    code = "x = 5"
    parser = ASTParser(code)
    assert parser.is_valid(), "Valid code should parse successfully"
    print("✓ test_basic_parsing passed")

def test_invalid_code():
    """Test handling of invalid code."""
    code = "if x = 5"  # Missing colon
    parser = ASTParser(code)
    assert not parser.is_valid(), "Invalid code should fail parsing"
    assert parser.error is not None, "Error should be captured"
    print("✓ test_invalid_code passed")

def test_variable_extraction():
    """Test extracting variables."""
    code = "x = 5\ny = 10"
    parser = ASTParser(code)
    variables = parser.get_variables()
    assert len(variables) == 2, "Should find 2 variables"
    assert variables[0]['name'] == 'x', "First variable should be 'x'"
    print("✓ test_variable_extraction passed")

def test_function_extraction():
    """Test extracting functions."""
    code = """
def greet(name):
    print(f"Hello {name}")
"""
    parser = ASTParser(code)
    functions = parser.get_functions()
    assert len(functions) == 1, "Should find 1 function"
    assert functions[0]['name'] == 'greet', "Function name should be 'greet'"
    assert 'name' in functions[0]['args'], "Should have 'name' argument"
    print("✓ test_function_extraction passed")

def test_count_lines():
    """Test counting lines of code."""
    code = "x = 5\ny = 10\nz = 15"
    lines = count_lines_of_code(code)
    assert lines == 3, "Should count 3 lines"
    print("✓ test_count_lines passed")

def test_count_non_empty_lines():
    """Test counting non-empty lines."""
    code = "x = 5\n\ny = 10"
    non_empty = count_non_empty_lines(code)
    assert non_empty == 2, "Should count 2 non-empty lines"
    print("✓ test_count_non_empty_lines passed")

def test_count_comments():
    """Test counting comment lines."""
    code = "# Comment\nx = 5"
    comments = count_comment_lines(code)
    assert comments == 1, "Should count 1 comment line"
    print("✓ test_count_comments passed")

def test_average_line_length():
    """Test calculating average line length."""
    code = "abc\ndefgh"  # 3 chars + 5 chars = 8 / 2 = 4
    avg = get_average_line_length(code)
    assert avg == 4.0, "Average should be 4.0"
    print("✓ test_average_line_length passed")

def run_all_tests():
    """Run all tests."""
    print("\n" + "="*50)
    print("RUNNING PHASE 1 TESTS")
    print("="*50 + "\n")
    
    tests = [
        test_basic_parsing,
        test_invalid_code,
        test_variable_extraction,
        test_function_extraction,
        test_count_lines,
        test_count_non_empty_lines,
        test_count_comments,
        test_average_line_length
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
    
    print("\n" + "="*50)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("="*50 + "\n")


if __name__ == "__main__":
    run_all_tests()