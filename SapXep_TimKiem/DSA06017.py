#trộn 2 dãy 
def merge(a,b):
    a.sort() 
    b.sort()
    n,m = len(a) , len(b)
    i,j = 0,0 
    hop = []

    while i < n and j <m : 
        if a[i] < b[j] : 
            hop.append(a[i])
            i+= 1 
        elif a[i] > b[j]:
            hop.append(b[j])
            j+= 1 
        else: 
            hop.append(a[i]) #hợp nhất là thêm cả các ptu trùng nhau 
            hop.append(b[j])
            i+=1 
            j+= 1 
    hop.extend(a[i:])
    hop.extend(b[j:])

    return hop
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 
    print(*merge(a,b))