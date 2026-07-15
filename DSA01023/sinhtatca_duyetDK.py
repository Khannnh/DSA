#in ra số thứ tự của 1 tổ hợp 
def to_hop(n,k): 
    a= [0]*(k+1) #index từ 1 
    cac_to_hop = []
    def backtrack(i): 
        #basecase 
        if i > k : # sinh hết 1 cấu hình 
            cac_to_hop.append(a[1:])
            return 
        for j in range(a[i-1]+1 , n-k+i+1):
            a[i] = j 
            backtrack(i+1)
    backtrack(1)
    return cac_to_hop

t= int(input())
for _ in range(t): 
    n,k = list(map(int,input().split()))
    cau_hinh = list(map(int , input().split()))
    res = (to_hop(n,k))
    for i in range(len(res)): 
        if res[i] == cau_hinh: 
            print(i+1)