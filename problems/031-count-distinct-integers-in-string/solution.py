def solution(word: str) -> int:
    # Replace all non-digit characters with spaces
    processed = ''.join(' ' if not c.isdigit() else c for c in word)

    # Split the string and filter out empty strings
    numbers = [num for num in processed.split() if num]

    # Remove leading zeros and use a set to count distinct numbers
    unique_numbers = set(str(int(num)) for num in numbers)

    return len(unique_numbers)

if __name__ == '__main__':
    print(solution("a123bc34d8ef34") == 3)
    print(solution("t1234c23456") == 2)
    print(solution("a1b01c001d4") == 2)
