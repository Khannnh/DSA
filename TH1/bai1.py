def dem(a,x): 
    count = a.count(x)
    if count == 0 : 
        return -1 
    return count 
t=int(input())
for _ in range(t): 
    n , x = list(map(int , input().split()))
    arr = list(map(int , input().split()))
    print(dem(arr , x))