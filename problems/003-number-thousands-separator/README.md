# Number Thousands Separator Formatting

## Problem Description
Given a string representing a number, convert it to a format with thousands separator commas, while handling the following special cases:
1. Preserve the decimal part (if any)
2. Remove leading zeros from the integer part

## Examples
```python
Input: s = "1294512.12412"
Output: '1,294,512.12412'

Input: s = "0000123456789.99"
Output: '123,456,789.99'

Input: s = "987654321"
Output: '987,654,321'
```

## Solution Approach
1. First, split the number into the integer part and decimal part
2. Process the integer part:
   - Remove leading zeros
   - Add a comma every three digits
3. If there is a decimal part, keep it unchanged and append it to the result

## Implementation
```python
def solution(s: str) -> str:
    # Split the integer part and decimal part
    parts = s.split('.')
    
    # Process the integer part: remove leading zeros and add thousands separators
    integer_part = parts[0].lstrip('0')
    if not integer_part:  # If the integer part is empty (i.e., original number starts with 0)
        integer_part = '0'
        
    # Add commas from right to left every three digits
    formatted_int = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and i % 3 == 0:
            formatted_int = ',' + formatted_int
        formatted_int = digit + formatted_int
    
    # If there is a decimal part, append it
    if len(parts) > 1:
        return formatted_int + '.' + parts[1]
    
    return formatted_int
```

## Code Explanation

### 1. Splitting the Integer and Decimal Parts
```python
parts = s.split('.')
```
Using the `split('.')` method to split the string by the decimal point:
- If there is a decimal point, parts will contain two elements: the integer part and the decimal part
- If there is no decimal point, parts will contain only one element: the integer part

### 2. Handling Leading Zeros
```python
integer_part = parts[0].lstrip('0')
if not integer_part:  # If the integer part is empty (i.e., original number starts with 0)
    integer_part = '0'
```
- The `lstrip('0')` method removes all leading zeros from the left side of the string
- If the result is an empty string (meaning the original number was 0), set the integer part to '0'

### 3. Adding Thousands Separator Commas
```python
formatted_int = ''
for i, digit in enumerate(integer_part[::-1]):
    if i > 0 and i % 3 == 0:
        formatted_int = ',' + formatted_int
    formatted_int = digit + formatted_int
```
- `integer_part[::-1]` reverses the string to process from right to left
- `enumerate()` gets both the index and value of each digit
- A comma is added whenever the index is a multiple of 3 (and not the first digit)
- String concatenation is used to build the final result

### 4. Handling the Decimal Part
```python
if len(parts) > 1:
    return formatted_int + '.' + parts[1]
return formatted_int
```
- Check if there is a decimal part (parts length greater than 1)
- If so, append the decimal point and decimal part to the result
- If not, return the processed integer part directly

## Complexity Analysis
- Time complexity: O(n), where n is the length of the input string
- Space complexity: O(n), needed to store the processed string

## Related Topics
- Number formatting
- String manipulation
- Thousands separator

## Summary
This problem primarily tests basic string operations:
1. String splitting
2. String traversal and concatenation
3. Handling special cases (leading zeros, decimal parts)

The key to solving this problem is to clearly define the processing steps, handle the integer and decimal parts separately, and pay attention to edge cases.
