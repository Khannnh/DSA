# tìm xem tổ hợp kế tiếp có bao nhiêu ptu thay đổi so vs th cũ
def tohopketiep(n,k,th):
    pos = -1 
    a=th.copy()
    for i in range (k-1,-1 ,-1): #chạy từ cuối tìm ptu tại index i chưa đạt max
        if a[i] < n-k+i+1 :
            a[i] += 1
            pos = i 
            break # chỉ tìm 1 vị trí đầu tiên thôi nên phải break
    if pos == -1 : #nếu tổ hợp cuối cùng => in k
        return k 
    for j in range(pos+1 ,k): 
        a[j] = a[j-1] +1   
    #đếm số ptu moi
    count = 0
    th_set= set(th) #đổi kiểu dữ liệu set để tìm kiếm nhanh hơn O(1) so với O(k)
    for i in a:
        if not i in th_set:
            count+= 1 
    return count     

t = int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    th = list(map(int , input().split()))
    print(tohopketiep(n,k,th))
     