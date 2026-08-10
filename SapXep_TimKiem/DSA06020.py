def timkiem(a:list, x : int):
    #phải sắp xếp mảng a thì mới tìm kiếm nhị phân được
    a.sort() 
    n= len(a)
    l , r = 0 , n-1 
    while l <= r : 
        mid = (l+r) // 2
        if a[mid] == x : 
            return 1 
        elif x> a[mid]:
            l=mid +1 
        else: 
            r = mid -1 
    return -1 
t=int(input())
for _ in range(t): 
    n, x = list(map(int,input().split()))
    a= list(map(int,input().split()))
    print(timkiem(a,x))