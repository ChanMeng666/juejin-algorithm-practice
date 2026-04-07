def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2  # Use integer division operator

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    return 0

def solution(expression):
    nums = []  # Stack for storing numbers
    ops = []   # Stack for storing operators
    i = 0

    while i < len(expression):
        char = expression[i]

        # If it is a digit, parse the complete number
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            nums.append(num)
            i -= 1

        # If it is a left parenthesis, push it directly onto the stack
        elif char == '(':
            ops.append(char)

        # If it is a right parenthesis, evaluate the expression inside the parentheses
        elif char == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(calculate(num1, num2, op))
            ops.pop()  # Pop the left parenthesis

        # If it is an operator
        else:
            while (ops and ops[-1] != '(' and
                   precedence(ops[-1]) >= precedence(char)):
                op = ops.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(calculate(num1, num2, op))
            ops.append(char)

        i += 1

    # Process remaining operators
    while ops:
        op = ops.pop()
        num2 = nums.pop()
        num1 = nums.pop()
        nums.append(calculate(num1, num2, op))

    return nums[0]

if __name__ == "__main__":
    # Test cases
    print(solution("1+1") == 2)
    print(solution("3+4*5/(3+2)") == 7)
    print(solution("4+2*5-2/1") == 12)
    print(solution("(1+(4+5+2)-3)+(6+8)") == 23)
    print(solution("2*(5+5*2)/3+(6+8*3)") == 40)
