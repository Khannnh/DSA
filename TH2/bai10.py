def backtrack(start, current_sum, group):
    if group == K - 1:
        return True

    if current_sum == target:
        return backtrack(0, 0, group + 1)

    for i in range(start, N):
        if not used[i] and current_sum + A[i] <= target:
            used[i] = True

            if backtrack(i + 1, current_sum + A[i], group):
                return True

            used[i] = False

    return False


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)

    if total % K != 0:
        print(0)
        continue

    target = total // K

    # Nếu có phần tử lớn hơn target thì chắc chắn không được
    if max(A) > target:
        print(0)
        continue

    # Sắp xếp giảm dần giúp chạy nhanh hơn
    A.sort(reverse=True)

    used = [False] * N

    if backtrack(0, 0, 0):
        print(1)
    else:
        print(0)