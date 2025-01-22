def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2  # 使用整除运算符

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    return 0

def solution(expression):
    nums = []  # 存储数字的栈
    ops = []   # 存储操作符的栈
    i = 0
    
    while i < len(expression):
        char = expression[i]
        
        # 如果是数字，解析完整的数字
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            nums.append(num)
            i -= 1
        
        # 如果是左括号，直接入栈
        elif char == '(':
            ops.append(char)
        
        # 如果是右括号，计算括号内的表达式
        elif char == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(calculate(num1, num2, op))
            ops.pop()  # 弹出左括号
        
        # 如果是运算符
        else:
            while (ops and ops[-1] != '(' and 
                   precedence(ops[-1]) >= precedence(char)):
                op = ops.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(calculate(num1, num2, op))
            ops.append(char)
        
        i += 1
    
    # 处理剩余的运算符
    while ops:
        op = ops.pop()
        num2 = nums.pop()
        num1 = nums.pop()
        nums.append(calculate(num1, num2, op))
    
    return nums[0]

if __name__ == "__main__":
    # 测试用例
    print(solution("1+1") == 2)
    print(solution("3+4*5/(3+2)") == 7)
    print(solution("4+2*5-2/1") == 12)
    print(solution("(1+(4+5+2)-3)+(6+8)") == 23)
    print(solution("2*(5+5*2)/3+(6+8*3)") == 40)