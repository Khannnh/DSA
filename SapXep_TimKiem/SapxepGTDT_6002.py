def mergeSort(a:list , x:int):
    #basecase
    if len(a) <= 1 : 
        return a 
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    #đệ quy 
    sort_left = mergeSort(left,x)
    sort_right = mergeSort(right,x)
    #phải return kết quả của hàm merge :))), nếu ko chỉ gọi làm thôi 
    return merge(sort_left,sort_right ,x )

def merge(l:list,r:list , x):
    res , i , j = [] , 0 , 0 
    while i<len(l) and j < len(r):
        #lấy dấu = ở đây để ưu tiên index nếu giá trị = nhau 
        if abs(x-l[i]) <= abs(x-r[j]):
            res.append(l[i])
            i+= 1
        else : 
            res.append(r[j])
            j+= 1 
    res.extend(l[i:])
    res.extend(r[j:])
    return res 
t=int(input())
for _ in range(t):
    n , x = map(int , input().split())
    a= list(map(int , input().split()))
    result = mergeSort(a,x)
    print(" ".join(map(str,result)))
