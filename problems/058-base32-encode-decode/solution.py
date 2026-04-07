def solution(rawStr, encodedStr):
    # Base32 character mapping table
    char_map = "9876543210mnbvcxzasdfghjklpoiuyt"

    def str_to_bits(s):
        # Convert a string to a binary bit string
        return ''.join(format(ord(c), '08b') for c in s)

    def bits_to_str(bits):
        # Convert a binary bit string back to a string
        # Ensure the number of bits is a multiple of 8
        if len(bits) % 8 != 0:
            bits = bits[:-(len(bits) % 8)]
        result = ""
        for i in range(0, len(bits), 8):
            if i + 8 <= len(bits):
                char = chr(int(bits[i:i+8], 2))
                if char != '\x00':  # Skip null characters
                    result += char
        return result

    def encode(s):
        if not s:
            return ""
        # Get the binary bit string
        bits = str_to_bits(s)
        # Calculate the number of zeros to pad
        padding = (5 - len(bits) % 5) % 5
        bits += '0' * padding

        # Convert every 5 bits to a character
        result = ""
        for i in range(0, len(bits), 5):
            chunk = bits[i:i+5]
            idx = int(chunk, 2)
            result += char_map[idx]

        # Determine the number of + padding symbols based on the original bit length
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
        # Remove padding symbols
        s = s.rstrip('+')

        # Convert Base32 characters back to a binary bit string
        bits = ""
        for c in s:
            idx = char_map.index(c)
            bits += format(idx, '05b')

        return bits_to_str(bits)

    # Encode rawStr and decode encodedStr
    encoded = encode(rawStr)
    # Handle multi-segment encoding
    decoded = ""
    for part in encodedStr.split('+' * 3):
        if part:
            decoded += decode(part + '+++')

    return f"{encoded}:{decoded}"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("foo", "b0zj5+++") == "bljhy+++:bar" )
    print(solution("The encoding process", "bljhy+++b0zj5+++") == "maf3m164vlahyl60vlds9i6svuahmiod:foobar" )
    print(solution("Base32 encoding and decoding", "bvchz+++v4j21+++cals9+++") == "10zj3l0d31z3mod6vus3sod258zhil89bash3oo5v4j3c+++:c]hintts " )
