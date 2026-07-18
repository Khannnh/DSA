def uu_tien(op): #Kiểu dữ liệu op là str
    if op =="^": return 3
    if op in "*/": return 2 
    if op in "+-":return 1 
    return 0 
def trungto_hauto(arr):
    output=[]
    stack=[]
    
    for char in arr : 
        #khối toán hạng
        if char.isalnum(): 
            output.append(char)
            
        #khối ngoặc
        elif char == "(" :
            stack.append(char)
        elif char == ")": 
            #xả kho cho tới khi gặp dấu mở ngoặc 
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack :
                stack.pop()
        
        #khối toán tử 
        else:
            while stack and uu_tien(stack[-1])>= uu_tien(char):
                # Nếu top "mạnh" hơn hoặc "bằng" char thì pop ra Output
                output.append(stack.pop())
            # Sau khi đẩy hết kẻ mạnh hơn ra, char mới được vào Stack
            stack.append(char)
        
    while stack :
            #lấy nốt những gì còn trong stack vào Output nếu stack ko rỗng 
            output.append(stack.pop())
    print("".join(output))
            
T=int(input())
for _ in range(T):
    s=input().strip()
    trungto_hauto(s)

