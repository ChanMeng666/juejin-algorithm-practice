def solution(binary1, binary2):
    # Convert a binary string to a decimal number
    def bin_to_dec(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal

    # Convert the two binary numbers and add them
    num1 = bin_to_dec(binary1)
    num2 = bin_to_dec(binary2)

    # Return the sum as a string
    return str(num1 + num2)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("101", "110") == "11")
    print(solution("111111", "10100") == "83")
    print(solution("111010101001001011", "100010101001") == "242420")
    print(solution("111010101001011", "10010101001") == "31220")
