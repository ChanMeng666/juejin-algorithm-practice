# Base32 Encode Decode

## Problem Description

Implement a Base32 encoding and decoding function. The function must:
1. Encode an input string using Base32
2. Decode a Base32-encoded string

### Requirements

Base32 is an encoding scheme that converts binary data into printable characters, similar to the more common Base64. Key characteristics:

- Encodes in groups of 5 bits (Base64 uses 6-bit groups)
- Uses 32 printable characters to represent encoded output (Base64 uses 64 characters)
- Requires appending a specific number of `+` symbols as padding at the end

### Constraints

- The character mapping table is: `"9876543210mnbvcxzasdfghjklpoiuyt"`
- Padding uses `+` symbols instead of the standard `=`

## Examples

```python
Input: rawStr = "foo", encodedStr = "b0zj5+++"
Output: "bljhy+++:bar"

Input: rawStr = "The encoding process", encodedStr = "bljhy+++b0zj5+++"
Output: "maf3m164vlahyl60vlds9i6svuahmiod:foobar"
```

## Solution Approach

### Encoding Steps

1. **String to binary**
   - Convert each character in the input string to 8-bit binary
   - Concatenate all characters' binary representations

2. **5-bit grouping**
   - Group the binary string into chunks of 5 bits each
   - If the last group has fewer than 5 bits, pad with zeros

3. **Table lookup conversion**
   - Convert each 5-bit group to a decimal number (0-31)
   - Map the number to the corresponding character using the mapping table

4. **Add padding**
   - Determine the number of `+` symbols based on the original string length (in bits)
   - The remainder of bits divided by 40 determines the padding count:
     - Remainder 8: append 6 `+` symbols
     - Remainder 16: append 4 `+` symbols
     - Remainder 24: append 3 `+` symbols
     - Remainder 32: append 1 `+` symbol
     - Remainder 0: no padding needed

### Decoding Steps

1. **Preprocessing**
   - Remove trailing `+` padding symbols
   - Split the encoded string by `+++` (to handle multi-segment encoding)

2. **Characters to binary**
   - Look up each character's index (0-31) in the mapping table
   - Convert the index to a 5-bit binary representation

3. **Binary to string**
   - Convert the binary string back to characters in 8-bit groups
   - Handle potential padding bits at the end
   - Skip null characters (\x00)

## Implementation

```python
def solution(rawStr, encodedStr):
    char_map = "9876543210mnbvcxzasdfghjklpoiuyt"

    def str_to_bits(s):
        return ''.join(format(ord(c), '08b') for c in s)

    def bits_to_str(bits):
        if len(bits) % 8 != 0:
            bits = bits[:-(len(bits) % 8)]
        result = ""
        for i in range(0, len(bits), 8):
            if i + 8 <= len(bits):
                char = chr(int(bits[i:i+8], 2))
                if char != '\x00':
                    result += char
        return result

    def encode(s):
        if not s:
            return ""
        bits = str_to_bits(s)
        padding = (5 - len(bits) % 5) % 5
        bits += '0' * padding
        result = ""
        for i in range(0, len(bits), 5):
            chunk = bits[i:i+5]
            idx = int(chunk, 2)
            result += char_map[idx]
        orig_bits_len = len(s) * 8
        if orig_bits_len % 40 == 8:
            result += "+" * 6
        elif orig_bits_len % 40 == 16:
            result += "+" * 4
        elif orig_bits_len % 40 == 24:
            result += "+" * 3
        elif orig_bits_len % 40 == 32:
            result += "+" * 1
        return result

    def decode(s):
        if not s:
            return ""
        s = s.rstrip('+')
        bits = ""
        for c in s:
            idx = char_map.index(c)
            bits += format(idx, '05b')
        return bits_to_str(bits)

    encoded = encode(rawStr)
    decoded = ""
    for part in encodedStr.split('+' * 3):
        if part:
            decoded += decode(part + '+++')
    return f"{encoded}:{decoded}"
```

## Code Explanation

1. When encoding, correctly handle cases where the number of bits is not sufficient by padding with appropriate zeros
2. When decoding, correctly handle padding symbols
3. Skip null characters in the decoded result
4. When handling multi-segment encoding, correctly split and merge results

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the input strings
- **Space Complexity**: O(n), for storing intermediate binary strings and results

## Summary

By understanding the above implementation process and important considerations, one can better grasp the principles and implementation details of Base32 encoding and decoding. The key challenges are correctly handling bit-level operations, padding, and multi-segment encoding.
