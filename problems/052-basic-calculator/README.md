# Basic Calculator

## Problem Description

Implement a basic calculator to evaluate a simple string expression.

### Requirements
- The input string expression is valid and may contain digits (0-9), arithmetic operators (+, -, *, /), and parentheses ()
- The string does not contain spaces
- Division retains only the integer result
- The built-in `eval` function is not allowed

### Constraints
- The expression is always valid
- Integer division is used for the `/` operator

## Examples

```python
Input: expression = "1+1"
Output: 2

Input: expression = "3+4*5/(3+2)"
Output: 7

Input: expression = "4+2*5-2/1"
Output: 12

Input: expression = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Input: expression = "2*(5+5*2)/3+(6+8*3)"
Output: 40
```

## Solution Approach

### 1. Core Idea
This is a classic expression evaluation problem that can be solved using stacks. The key challenges to address are:
- Operator precedence handling
- Parentheses handling
- Multi-digit number parsing
- Executing operations in the correct order

### 2. Detailed Implementation Steps

#### 2.1 Data Structure Design
Two stacks are used:
- `nums` stack: for storing numbers
- `ops` stack: for storing operators

#### 2.2 Operator Precedence
Define a precedence function:
- Multiplication and division (*, /) have precedence 2
- Addition and subtraction (+, -) have precedence 1
- Left parenthesis has precedence 0

#### 2.3 Main Algorithm Flow
1. Traverse the expression string and handle each character type:

   a. When encountering a digit:
   - Parse the complete multi-digit number
   - Push the number onto the `nums` stack

   b. When encountering a left parenthesis:
   - Push it directly onto the `ops` stack

   c. When encountering a right parenthesis:
   - Evaluate all expressions inside the parentheses until a left parenthesis is found
   - Pop the left parenthesis

   d. When encountering an operator:
   - Compare the current operator's precedence with the top of the `ops` stack
   - If the top operator has higher or equal precedence, perform the calculation
   - Push the current operator onto the `ops` stack

2. After traversing the expression, process the remaining operators in the `ops` stack

### 3. Key Implementation Details

#### 3.1 Basic Calculation Function
```python
def calculate(num1, num2, operator):
    if operator == '+': return num1 + num2
    elif operator == '-': return num1 - num2
    elif operator == '*': return num1 * num2
    elif operator == '/': return num1 // num2  # Use integer division operator
```

#### 3.2 Precedence Function
```python
def precedence(operator):
    if operator in ['+', '-']: return 1
    if operator in ['*', '/']: return 2
    return 0
```

## Code Explanation

1. Division uses the integer division operator `//` to ensure the result is an integer
2. When parsing multi-digit numbers, each digit must be accumulated correctly
3. Correct handling of operator precedence is critical
4. Parentheses matching requires special attention
5. Stack operation order must be correct, especially the order of popping numbers for calculations

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the expression
- **Space Complexity**: O(n), two stacks are needed to store numbers and operators

## Summary

This problem is a classic algorithm interview question. Understanding and mastering it is very helpful for improving programming skills. Through this problem, we can learn about stack applications and the fundamental principles of expression parsing.
