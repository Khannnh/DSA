import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

prefix = [0] * (N + 1)

for i, x in enumerate(A, 1):
    prefix[i] = prefix[i - 1] + (x if x > 0 else 0)

ans = []

for _ in range(Q):
    L, R = map(int, input().split())
    ans.append(str(prefix[R] - prefix[L - 1]))

sys.stdout.write("\n".join(ans))