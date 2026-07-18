#BAI 8 
t = int(input())
for _ in range(t): 
    stack = []
    s = input().strip()
    for char in s:
        if char.isdigit(): 
            # ÉP KIỂU NGAY TẠI ĐÂY: Lưu vào stack là số luôn
            stack.append(int(char)) 
        else: 
            # Lấy ra là có số dùng luôn, không cần int() nữa
            phai = stack.pop()
            trai = stack.pop()
            
            if char == "+":
                stack.append(trai + phai)
            elif char == "-":
                stack.append(trai - phai)
            elif char == "*":
                stack.append(trai * phai)
            elif char == "/":
                # đề yêu cầu lấy nguyên nhưng // thì làm tròn xuống 
                stack.append(int(trai / phai)) 
    
    print(stack[0])
