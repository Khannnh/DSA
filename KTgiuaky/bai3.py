#tính biểu thức trung tố
def priority(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0


def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    return a // b


t = int(input())
for _ in range(t):
    s = input().replace(" ", "")
    nums = []
    ops = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i]) #ép kiểu nguyên 
                i += 1
            nums.append(num)
            continue
        elif s[i] == '(':
            ops.append('(')
        elif s[i] == ')':
            while ops[-1] != '(':
                op = ops.pop()
                b = nums.pop()
                a = nums.pop()
                nums.append(calc(a, b, op))

            ops.pop()
        else:
            while ops and priority(ops[-1]) >= priority(s[i]):
                op = ops.pop()
                b = nums.pop()
                a = nums.pop()
                nums.append(calc(a, b, op))

            ops.append(s[i])

        i += 1

    while ops:
        op = ops.pop()
        b = nums.pop()
        a = nums.pop()
        nums.append(calc(a, b, op))

    print(nums[-1])