#tìm bội số 
from collections import deque

def solve(n):
    if n == 1:
        return "9"

    visited = [False] * n
    parent = [-1] * n
    digit = [''] * n

    start = 9 % n

    q = deque([start])
    visited[start] = True
    digit[start] = '9'

    while q:
        r = q.popleft()

        if r == 0:
            break

        # thêm chữ số 0
        nr = (r * 10) % n
        if not visited[nr]:
            visited[nr] = True
            parent[nr] = r
            digit[nr] = '0'
            q.append(nr)

        # thêm chữ số 9
        nr = (r * 10 + 9) % n
        if not visited[nr]:
            visited[nr] = True
            parent[nr] = r
            digit[nr] = '9'
            q.append(nr)

    # truy vết
    ans = []
    cur = 0
    while cur != -1:
        ans.append(digit[cur])
        cur = parent[cur]

    return ''.join(ans[::-1])


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))