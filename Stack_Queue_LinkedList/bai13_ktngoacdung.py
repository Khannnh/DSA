T=int(input())
pairs = {
    ')': '(',
    '}': '{',   
    ']': '['
}

for _ in range(T):
    s=input().strip()
    stack = []
    balanced = True
    for char in s:
        if char in pairs.values():  # Nếu là 1 trong dấu mở ngoặc
            stack.append(char)
        elif char in pairs.keys():  # Nếu là 1 trong 3 dấu đóng ngoặc
            if not stack or stack[-1]!= pairs[char]:
                balanced = False
                break
            else:
                stack.pop() # bỏ dấu mở ngoặc tương ứng khỏi stack
    
    #kiểm tra điều kiện để in 
    if balanced and not stack :
        print("YES")
    else:
        print("NO")
