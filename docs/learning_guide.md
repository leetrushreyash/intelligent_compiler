# Phase 1: Foundation Learning Guide

## Overview

Welcome to the Intelligent Compiler project! This guide will help you understand Phase 1: Foundation.

## What is an AST?

An **Abstract Syntax Tree (AST)** is a tree representation of the structure of source code.

### Simple Example

**Code:**
```python
x = 5
```

**AST Structure:**
```
Module
└── body
    └── Assign
        ├── targets: [Name(id='x')]
        └── value: Constant(value=5)
```

### Why is AST Important?

1. **Parsing**: Convert text to tree (computers understand this better)
2. **Analysis**: Walk the tree to find patterns
3. **Transformation**: Modify the tree to optimize code
4. **Detection**: Find code smells and issues

## How the Parser Works

### Step 1: Input Code
```python
def hello(name):
    print(f"Hello {name}")
```

### Step 2: Parsing
- Python's `ast.parse()` reads the code
- Builds a tree structure
- Validates syntax

### Step 3: Tree Structure
```
Module
└── body
    └── FunctionDef(name='hello', args=['name'])
        └── body
            └── Expr
                └── Call(func=Name('print'), args=['...'])
```

### Step 4: Analysis
- Walk the tree with `ast.walk()`
- Look for specific node types
- Extract information

## Key Concepts

### ast.walk()

Visits every node in the tree.

```python
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(node.name)  # Found a function!
```

### Node Types

Common AST node types:

- **Module**: The entire program
- **FunctionDef**: A function definition
- **ClassDef**: A class definition
- **Assign**: An assignment (x = 5)
- **Call**: A function call
- **Import**: An import statement
- **Return**: A return statement

## Running Examples

### Run the Learning Examples

```bash
cd phase1_foundation
python examples.py
```

This will show you:
1. Basic parsing
2. Variable extraction
3. Function extraction
4. Code metrics
5. Utility functions
6. Error handling
7. Complete walkthrough

### Run the Tests

```bash
cd tests
python test_phase1.py
```

This verifies everything works correctly.

## Practice Exercises

### Exercise 1: Parse and Count Functions

```python
from phase1_foundation.ast_parser import ASTParser

code = '''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
'''```

parser = ASTParser(code)
functions = parser.get_functions()
print(f"Found {len(functions)} functions")
```

**Expected Output:**
```
Found 2 functions
```

### Exercise 2: Extract and Display Variables

```python
code = '''
x = 5
y = 10
z = x + y
'''```

parser = ASTParser(code)
variables = parser.get_variables()
for var in variables:
    print(f"Variable: {var['name']} at line {var['lineno']}")
```

**Expected Output:**
```
Variable: x at line 2
Variable: y at line 3
Variable: z at line 4
```

### Exercise 3: Analyze Code Metrics

```python
code = '''
import os
import sys

def process(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result

x = process([1, 2, 3])
'''```

parser = ASTParser(code)
metrics = parser.get_code_metrics()
print(metrics)
```

## Common Questions

### Q: What's the difference between ast.walk() and ast.iter_child_nodes()?

**A:** 
- `ast.walk()`: Returns ALL nodes in the tree (recursively)
- `ast.iter_child_nodes()`: Returns only direct children (not recursive)

```python
# ast.walk() - gets everything
for node in ast.walk(tree):
    # Visits: Module, Assign, Name, Constant, etc.

# ast.iter_child_nodes() - only direct children
for node in ast.iter_child_nodes(tree):
    # Visits: Only the statements in Module.body
```

### Q: How do I find a specific type of node?

**A:** Use `isinstance()` to check node type:

```python
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Found function: {node.name}")
    elif isinstance(node, ast.ClassDef):
        print(f"Found class: {node.name}")
```

### Q: Can I modify the AST and generate code from it?

**A:** Yes! You can use `ast.unparse()` (Python 3.9+):

```python
tree = ast.parse("x = 5")
# Modify tree...
code = ast.unparse(tree)  # Convert back to code
```

## Next Steps

1. ✓ Understand AST basics
2. ✓ Run the examples
3. ✓ Complete the exercises
4. → Move to Phase 2: Code Smell Detection

## Resources

- [Python ast module documentation](https://docs.python.org/3/library/ast.html)
- [AST visualization tools](https://astuetz.github.io/ast-explorer/)
- [Building a Python compiler tutorial](https://www.craftinginterpreters.com/)