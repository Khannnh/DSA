#kiểm tra 2 biểu thức có tương đương nhau ko
#biến đổi 2 biểu thức về dạng rút gọn : bỏ hết ngoặc rồi so sánh 
def rutgon(s):
    res= []
    stack= [False]

    for i , char in enumerate(s):
        if char == '(':
            is_minus_before = (i>0 and s[i-1] == "-")
            stack.append(stack[-1]^is_minus_before) #dùng xor đảo trạng thái 
        elif char == ')':
            stack.pop()
        elif char in '+-':
            if stack[-1]:
                res.append('-' if char =='+' else '+')
            else:
                res.append(char)
        else:
            #là chữ cái a,b,c thì giữ nguyên 
            res.append(char)
    return "".join(res)
t=int(input())
for _ in range(t):
    p1=input()
    p2 = input()

    if rutgon(p1) == rutgon(p2):
        print("YES")
    else:
        print("NO")