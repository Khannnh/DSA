def mergeSort(a:list):
    #basecase đệ quy 
    if len(a) <= 1 :
        return a 
    mid = len(a)//2
    left , right = a[:mid] , a[mid:]
    #gọi đệ quy chính nó
    sort_left = mergeSort(left)
    sort_right = mergeSort(right)

    #gộp từng stack đệ quy sau khi return
    return merge(sort_left,sort_right)

def merge(l:list , r:list):
    res = []
    i , j = 0,0 
    while i<len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else : 
            res.append(r[j])
            j+= 1
    res.extend(l[i:])
    res.extend(r[j:])
    return res 

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(' '.join(map(str, mergeSort(a))))
