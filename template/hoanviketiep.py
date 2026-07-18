def hoanviketiep(a,n): 
    pos = -1 
    #b1: tìm điểm gãy dãy tăng 
    #cấu hình cuối là dãy giảm 5,4,3,2,1-> duyệt từ cuối về phải tăng
    for i in range(n-2,-1 ,-1): 
        if a[i]<a[i+1]:
            pos = i 
            break # DÙNG FOR THÌ PHẢI BREAK TAY 
    #b2 : nếu là cấu hình cuối => cấu hình đầu 
    if pos == -1 : 
        return list(range(1,n+1))
    
    #b3:chạy từ cuối mảng lại pos+1, tìm ptu đầu tiên > a[i]
    for j in range(n-1 ,pos,-1):
        if a[j] > a[i]:
            a[j] , a[i] = a[i] ,a[j]
            break 
    #b4 lật ngược đoạn từ pos+1 => cuối 
    a[pos+1:] = a[pos+1:][::-1]
    return a

t= int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int,input().split()))
    print(*(hoanviketiep(a,n)))
