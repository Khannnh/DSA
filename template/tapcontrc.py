#đầu vào là mảng a , return cái tập con liền trước của a
#  k là tổ hợp k của n 
def tapcontruoc(n,k,a): 
    pos = -1 
    for i in range(k-1 , -1 , -1): 
        if i > 0 and a[i]>a[i-1]+1 : 
            pos = i 
            a[pos] -= 1 
            break 
        if i == 0 and a[i] > 1 :
            pos = 0 
            a[pos]-= 1
            break 
    if pos == -1 : 
        return list(range(n-k+1 ,n+1))
    for j in range(pos+1,k): 
        a[j] = n-k+j+1
    return a 
t= int(input())
for _ in range(t): 
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print(*(tapcontruoc(n,k,x))) 
    
            

