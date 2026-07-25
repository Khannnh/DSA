# #tính lũy thừa 
# import math
# mod = 1000000007
# t=int(input())
# for _ in range(t):
#     n,k = list(map(int , input().split()))
#     a=math.pow(n,k//2)
#     if k %2 ==0 : 
#         print((a*a)%mod)
#     else : 
#         print((n%mod)*(a*a))
MOD = 1000000007

while True:
    n, k = map(int, input().split())
    if n== k == 0 : 
        break 
    else: 
        print(pow(n, k, MOD))