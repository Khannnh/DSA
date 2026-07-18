t = int(input())

for _ in range(t):
    s = input()
    stack = []
    ok = False

    for c in s:
        if c != ')':
            stack.append(c)
        else:
            hasOp = False

            while stack and stack[-1] != '(':
                x = stack.pop()
                if x in "+-*/":
                    hasOp = True

            stack.pop()      # bỏ '('

            if not hasOp:
                ok = True
                break

    print("Yes" if ok else "No")