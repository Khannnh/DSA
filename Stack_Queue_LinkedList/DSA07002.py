#ngăn xếp 2 
#in theo thứ tự LIFO 
q=int(input())
stack = []
for _ in range(q):
    while True : 
        query = input().split()
        if query[0]== "PUSH":
            stack.append(query[1])
        elif query[0] == "POP":
            if stack: #nhớ kiểm tra stack có phần tử để xóa ko
                stack.pop()
        elif query[0] == "PRINT":
            if stack:
                print(stack[-1])
            else: 
                print("NONE")
        break 
