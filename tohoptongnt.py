from itertools import combinations
import time

n, k = 29, 14

st = time.perf_counter()
cnt = 0

for _ in combinations(range(1, n + 1), k):
    cnt += 1

print(cnt)
print(time.perf_counter() - st)