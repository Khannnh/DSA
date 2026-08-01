#fibonaci
MOD = 10**9 + 7

# nhân 2 ma trận 2x2
def mul(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]

# lũy thừa nhị phân ma trận
def power(A, n):
    if n == 1:
        return A

    half = power(A, n // 2)

    if n % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), A)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    A = [
        [1, 1],
        [1, 0]
    ]

    res = power(A, n - 1)

    return res[0][0]


T = int(input())

for _ in range(T):
    n = int(input())
    print(fibonacci(n))