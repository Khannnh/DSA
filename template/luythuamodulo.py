import math 
mod = 10**9+7 
t= int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    print(pow(n, k, mod))