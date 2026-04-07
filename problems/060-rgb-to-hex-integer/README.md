# RGB to Hex Integer

## Problem Description

Given an RGB color value as a string, such as `"rgb(192, 192, 192)"`, write a function to convert it to the corresponding hexadecimal integer value.

### Requirements
- Input: A string in the format `"rgb(R, G, B)"`
- R, G, B represent the red, green, and blue color channel values respectively
- Each color channel value ranges from 0 to 255

### Constraints
- The output is an integer representing the converted hexadecimal value

## Examples

```python
Input: rgb = "rgb(192, 192, 192)"
Output: 12632256

Input: rgb = "rgb(100, 0, 252)"
Output: 6553852

Input: rgb = "rgb(33, 44, 55)"
Output: 2174007
```

## Solution Approach

1. **String Processing**
   - Extract the three R, G, B values from the input string
   - Use string replacement to remove `"rgb("` and `")"`
   - Split by `','` to get the three value strings
   - Use `map(int, ...)` to convert the strings to integers

2. **Color Value Conversion Principle**
   - In computers, RGB colors are typically represented with 24 bits
   - R occupies the upper 8 bits (left shift by 16)
   - G occupies the middle 8 bits (left shift by 8)
   - B occupies the lower 8 bits (no shift needed)
   - Final result = (R << 16) + (G << 8) + B

## Implementation

```python
def solution(rgb):
    # Extract numbers from the rgb string
    rgb = rgb.replace('rgb(', '').replace(')', '')
    r, g, b = map(int, rgb.split(','))

    # Calculate the hexadecimal integer value
    return (r << 16) + (g << 8) + b
```

## Code Explanation

1. `rgb.replace('rgb(', '').replace(')', '')`
   - Uses the `replace()` method to remove `"rgb("` and `")"` from the string
   - Example: `"rgb(192, 192, 192)"` becomes `"192, 192, 192"`

2. `rgb.split(',')`
   - Splits the string by commas to get a list of three color values
   - Example: `"192, 192, 192"` becomes `["192", " 192", " 192"]`

3. `map(int, ...)`
   - Converts each element in the string list to an integer
   - Example: `["192", " 192", " 192"]` becomes `[192, 192, 192]`

4. `(r << 16) + (g << 8) + b`
   - `r << 16`: Left-shifts R by 16 bits, occupying the upper 8 bits
   - `g << 8`: Left-shifts G by 8 bits, occupying the middle 8 bits
   - `b`: B remains unchanged, occupying the lower 8 bits
   - Adding the three values gives the final hexadecimal integer

### Example Calculation

Using `"rgb(192, 192, 192)"` as an example:
1. Binary representation of 192: `11000000`
2. R left-shifted by 16: `11000000 00000000 00000000`
3. G left-shifted by 8: `00000000 11000000 00000000`
4. B unshifted: `00000000 00000000 11000000`
5. Sum of all three: `12632256`

## Complexity Analysis

- **Time Complexity**: O(1), the input string has a fixed format and bounded length
- **Space Complexity**: O(1), only constant extra space is used

## Summary

This problem covers several key concepts:

1. **String Processing**: `replace()`, `split()`, and `map()` functions
2. **Bit Operations**: Left shift operator (`<<`) and binary computation
3. **RGB Color Encoding**: The 24-bit color representation and color channel concepts

The solution is concise and efficient, leveraging bit operations to combine three 8-bit color channels into a single 24-bit integer.
