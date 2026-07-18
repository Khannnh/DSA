def hoanvitrc(a:list,n:int): 
    pos = -1 
    for i in range(n-2, -1 , -1): 
        if a[i] > a[i+1] : 
            pos = i 
            break 
    if pos == -1 : 
        return list(range(n,0,-1))
    for j in range(n-1,pos,-1): 
        if a[j]<a[pos]: 
            a[j] , a[pos] = a[pos] , a[j]
            break 
    a[pos+1:] = a[pos+1:][::-1]
    return a 
t= int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int,input().split()))
    print(*(hoanvitrc(a,n)))