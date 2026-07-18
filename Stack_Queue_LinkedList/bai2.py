stack = []

while True:
    try:
        s = input().split()

        if s[0] == "push":
            stack.append(int(s[1]))

        elif s[0] == "pop":
            if stack:
                stack.pop()

        else:  # show
            if stack:
                print(*stack)
            else:
                print("empty")

    except EOFError:
        break