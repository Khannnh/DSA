F=[0]*93
F[1] = F[2] = 1
for i in range(3,93):
    F[i]= F[i-1]+ F[i-2]

def find_char(n,k):
    if n==1:
        return "0" 
    if n == 2 : 
        return "1"
    #độ dài xâu con phía trước 
    len_left= F[n-2]
    if k <= len_left:
        return find_char(n-2,k)
    else: 
        return find_char(n-1,k-len_left)
t=int(input())
for _ in range(t): 
    n,k= map(int,input().split())
    print(find_char(n,k))