#DSA06004
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 

    hop = []
    giao = []
    i = 0
    j = 0

    a.sort()
    b.sort()
    while i < n and j < m : 
        if a[i] < b[j] : 
            hop.append(a[i])
            i+= 1 
        elif a[i] > b[j]: 
            hop.append(b[j])
            j+= 1 
        else : 
            giao.append(a[i])
            hop.append(a[i])
            i+= 1
            j+= 1 
    while i < n : 
        hop.append(a[i])
        i+= 1 
    while j < m : 
        hop.append(b[j])
        j+= 1 
    
    print(*hop)
    print(*giao)