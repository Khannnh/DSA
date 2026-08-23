def uu_tien(op:str):
    if op in "^" : return 3
    if op in "*/":return 2
    if op in "+-":return 1
    return 0


def infix_to_postfix(exp:str):
    output , stack = [] , []
    for c in exp :
        #khối toán hạng
        if c.isalpha() or c.isdigit():
            output.append(c)


        #khối đóng mở ngoặc
        if c == "(":
            stack.append(c)
        if c == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop() #xóa nốt cái dấu (


        #khối toán tử :
        if c in "^*/+-":
            while stack and uu_tien(c) <= uu_tien(stack[-1]):
                output.append(stack.pop())
            stack.append(c)


    #dọn dẹp sau khi duyệt hết exp
    while stack :
        output.append(stack.pop())
    return output


t=int(input())
for _ in range(t):
    exp = input().strip()#xóa khoảng trắng thừa
    r = infix_to_postfix(exp)
    print("".join(map(str,r)))
