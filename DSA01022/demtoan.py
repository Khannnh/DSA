#tìm thứ tự 1 hoán vị thì tính xem có bao nhiêu hoán vị được sinh ra trước nó
#đầu vào là 1 hoán vị , trả về 1 con số là thứ tự của nó 
import math
def thutu(a): 
    n=len(a)
    rank = 1
    used = [False]*(n+1)
    for i in range(n): #index base 0 
        cnt = 0 
        for j in range(1,a[i]):
            if not used[j]: 
                cnt += 1 
        rank += cnt*math.factorial(n-i-1)
        used[a[i]] = True 
    return rank 
t=int(input())
for _ in range(t): 
    n=int(input())
    a= list(map(int , input().split()))
    print(thutu(a))
