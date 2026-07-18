t = int(input())

for _ in range(t):

    s = input().replace(" ", "")

    st = [False]      # False: không đảo dấu

    ans = []

    for i in range(len(s)):

        if s[i] == '(':

            if i > 0 and s[i-1] == '-':
                st.append(not st[-1])
            else:
                st.append(st[-1])

        elif s[i] == ')':
            st.pop()

        elif s[i] == '+':

            if st[-1]:
                ans.append('-')
            else:
                ans.append('+')

        elif s[i] == '-':

            if st[-1]:
                ans.append('+')
            else:
                ans.append('-')

        else:
            ans.append(s[i])

    print("".join(ans))