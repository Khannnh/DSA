# đếm số dấu ngoặc đổi chiều 
t = int(input())
for _ in range(t): 
    stack = [] #stack dạng list nên dùng các method của list được 
    s= input().strip()
    for char in s : 
        if char == "(": 
            stack.append(char)
        else : # nếu gặp ngoặc đóng 
            if stack and stack[-1] == "(":  #nếu cặp được với ngoặc mở
                stack.pop() 
            else :
                stack.append(char)
    open = stack.count("(")
    close = stack.count(")")
    
    result = (open+1)//2 + (close+1)//2 #chia lấy phần nguyên cho 2 
    print(result)
