def tapconketiep(n,k,a): 
    pos = -1 
    #duyệt từ cuối mảng về tìm giá trị đầu tiên chưa đạt max của nó 
    for i in range(k-1, -1 , -1): 
        if a[i] < n-k+i+1 :
            pos = i 
            break 
    #nếu ko tìm thấy giá trị nào ko đạt max=> cấu hình cuối quay về cấu hình đầu
    if pos == -1 : 
        return list(range(1,k+1))
    #tăng vị trí cần tăng lên 1 
    a[pos] += 1 
    #tăng đoạn sau post lên bắt đầu từ pos+1
    for j in range(pos+1 , k): 
        a[j] = a[j-1]+1 
    return a

t= int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    a = list (map(int , input().split()))
    print(*tapconketiep(n,k,a))
    



        