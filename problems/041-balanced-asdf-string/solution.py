def get_min_changes(freq):
    length = sum(freq.values())
    target = length // 4

    # Calculate the total number of characters that need to be changed
    total_changes = 0
    for f in freq.values():
        if f > target:
            total_changes += f - target

    # Each replacement handles two characters, so divide by 2
    # When total_changes is odd, round up
    return (total_changes + 1) // 2

def check_substring(s):
    # Count character frequencies in the substring
    freq = {'A': 0, 'S': 0, 'D': 0, 'F': 0}
    for c in s:
        freq[c] += 1
    return get_min_changes(freq)

def solution(input):
    n = len(input)
    if n % 4 != 0:
        return -1

    min_changes = n  # Initialize to the maximum possible value

    # Iterate over all possible substrings
    for i in range(len(input)):
        for j in range(i + 3, len(input)):
            # Only check substrings whose length is a multiple of 4
            if (j - i + 1) % 4 == 0:
                curr_changes = check_substring(input[i:j+1])
                if curr_changes < min_changes:
                    min_changes = curr_changes

                # If a perfectly balanced substring is found
                if min_changes == 0:
                    return 0

    return min_changes

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("ADDF", 1),
        ("ASAFASAFADDD", 3),
        ("SSDDFFFFAAAS", 1),
        ("AAAASSSSDDDDFFFF", 0),
        ("AAAADDDDAAAASSSS", 4)
    ]

    for test_input, expected in test_cases:
        result = solution(test_input)
        print(f"Input: {test_input}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 30)
