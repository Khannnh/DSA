#tập con liền kề phía trước
# trong tổ hợp chập k của n , giá trị của index sau luôn lớn hơn giá trị của index trước
def tap_con_truoc(n,k,a):
    pos = -1 
    #b1: tìm vị trí cần giảm 
    for i in range(k-1,-1,-1):
        if i > 0 and a[i] > a[i-1] +1 : 
            pos = i 
            a[pos] -= 1 
            break
        if i == 0 and a[i]> 1 : 
            pos = 0
            a[pos]-= 1
            break 
    #b2:xử lý biên cấu hình đầu thì trc nó là cấu hình cuối 
    if pos == -1 : 
        return list(range(n-k+1,n+1))
    #b3 : xử lý vị trí sau pos => tăng nó thành max
    for j in range(pos+1 ,k):
        a[j] = n-k+j+1 
    return a 
t= int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    x = list(map(int, input().split()))
    print(*tap_con_truoc(n,k,x))
