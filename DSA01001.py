def sinh_xau_ke_tiep(a):
    n= len(a)
    idx = n-1 
    while idx >= 0 and a[idx] == 1 : 
        a[idx]= 0 
        idx -= 1 
    if idx < 0 : 
        return [0]*n
    a[idx] =1 
    return a 
t=int(input())
for _ in range(t): 
    a = input() # nhập string bình thường
    arr = list(map(int , a)) #xé lẻ các ký tự bé trong chuỗi lớn thành int 
    print("".join(list(map(str , sinh_xau_ke_tiep(arr)))))