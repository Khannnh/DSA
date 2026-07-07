T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    pos = [0] * K
    res = []

    def backtrack(i, start):
        if i == K:
            s = ['0'] * N
            for p in pos:
                s[p] = '1'
            res.append(''.join(s))
            return

        for p in range(start, N):
            pos[i] = p
            backtrack(i + 1, p + 1)

    backtrack(0, 0)

    # in ngược để ra thứ tự từ điển tăng
    for s in reversed(res):
        print(s)
