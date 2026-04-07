# Count Distinct Integers in a String

## Problem Description

Given a string `word` consisting of digits and lowercase English letters, the requirements are:
1. Replace all non-digit characters in the string with spaces
2. Count the number of distinct integers after the replacement
3. Note: Integers with the same decimal representation without leading zeros are considered identical

## Examples

**Example 1:**
```
Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The replaced string is " 123 34 8 34"
             The integers obtained are: "123", "34", "8", "34"
             The distinct integers are: "123", "34", "8", totaling 3
```

**Example 2:**
```
Input: word = "t1234c23456"
Output: 2
Explanation: The replaced string is " 1234 23456"
             The integers obtained are: "1234", "23456"
             There are 2 distinct integers in total
```

**Example 3:**
```
Input: word = "a1b01c001d4"
Output: 2
Explanation: The replaced string is " 1 01 001 4"
             After removing leading zeros: "1", "1", "1", "4"
             The distinct integers are: "1", "4", totaling 2
```

## Solution Approach

This problem can be solved in the following key steps:

1. **Handle non-digit characters**
   - Iterate through the string and replace all non-digit characters with spaces
   - Use the string's `isdigit()` method to determine whether a character is a digit

2. **Extract numeric parts**
   - Split the processed string by spaces to obtain all numeric strings
   - Be careful to filter out any empty strings that may result from splitting

3. **Handle leading zeros**
   - Convert each numeric string to an integer to automatically remove leading zeros
   - Convert the integer back to a string to maintain a consistent string format

4. **Count distinct integers**
   - Use a set to eliminate duplicates
   - Return the size of the set as the count of distinct integers

## Implementation

```python
def solution(word: str) -> int:
    # Replace all non-digit characters with spaces
    processed = ''.join(' ' if not c.isdigit() else c for c in word)
    
    # Split the string and filter out empty strings
    numbers = [num for num in processed.split() if num]
    
    # Remove leading zeros and use a set to count distinct numbers
    unique_numbers = set(str(int(num)) for num in numbers)
    
    return len(unique_numbers)
```

## Code Explanation

1. **Step 1: Handle non-digit characters**
   ```python
   processed = ''.join(' ' if not c.isdigit() else c for c in word)
   ```
   - Use a generator expression to iterate over each character of the original string
   - If the character is not a digit (`not c.isdigit()`), replace it with a space
   - If it is a digit, keep it unchanged
   - Use `join()` to concatenate the processed characters into a new string

2. **Step 2: Extract numeric parts**
   ```python
   numbers = [num for num in processed.split() if num]
   ```
   - Use the `split()` method to split the string by spaces
   - The `if num` in the list comprehension filters out empty strings
   - The resulting `numbers` list contains all numeric strings

3. **Step 3: Deduplicate and count**
   ```python
   unique_numbers = set(str(int(num)) for num in numbers)
   ```
   - For each numeric string:
     - First convert to an integer with `int()` to remove leading zeros
     - Then convert back to a string with `str()`
   - Use `set()` for automatic deduplication
   - Finally, return the size of the set, which is the count of distinct integers

## Complexity Analysis

- Time complexity: O(n), where n is the length of the input string
- Space complexity: O(n), needed for storing the processed string and the set

## Notes

1. Special attention must be paid to handling leading zeros; e.g., "01" and "1" should be considered the same integer
2. After splitting the string, be careful to handle any empty strings that may appear
3. The `isdigit()` method conveniently determines whether a character is a digit
