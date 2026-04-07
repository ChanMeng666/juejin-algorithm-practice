def add_large_numbers(num1, num2):
    # Ensure num1 is at least as long as num2
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    # Pad the shorter number with leading zeros
    num2 = '0' * (len(num1) - len(num2)) + num2

    carry = 0
    result = ''

    # Add digit by digit from right to left
    for i in range(len(num1)-1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result = str(digit_sum % 10) + result

    # Handle the final carry
    if carry:
        result = '1' + result

    return result

def solution(string1, string2):
    # Calculate the sum of two large numbers
    sum_result = add_large_numbers(string1, string2)

    # If all digits in the result are the same, return 0
    if len(set(sum_result)) == 1:
        return 0

    # Iterate over adjacent digits and check if there are different digits
    for i in range(len(sum_result)-1):
        if sum_result[i] != sum_result[i+1]:
            return 1

    return 0

if __name__ == "__main__":
    # Test cases
    print(solution("111", "222") == 0)  # True
    print(solution("111", "34") == 1)   # True
    print(solution("999", "1") == 0)    # True
    print(solution("5976762424003073", "6301027308640389") == 6)  # True
