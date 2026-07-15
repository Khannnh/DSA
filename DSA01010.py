# sinh tổ hợp chập k của n phần tử theo thứ tự từ điển
# tìm tập con tiếp theo , so sánh xem số nào ko lặp lại ở tập con tiếp theo 
def tohoptieptheo(n,k,a): 
    pos = -1 
    next_a = a.copy()
    for i in range(k-1 ,-1 ,-1):
        if next_a[i] < n-k+i+1 : 
            pos = i 
            next_a[i] += 1 
            break
    # nếu là cấu hình cuối cùng 
    if pos == -1 :
        return k
    #xử lý đằng sau pos tăng lên tối thiểu(min)
    for j in range(pos+1,k):
        next_a[j] = next_a[j-1]+1
    
    cnt = 0 
    for x in a: 
        if x not in next_a:
           cnt += 1
    return cnt  
t= int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    x = list(map(int, input().split()))
    print(tohoptieptheo(n,k,x))