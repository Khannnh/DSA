#nhập n , k m in ra các cấu hình tổ hợp chập k của n = đệ quy 
def sinh_to_hop(n,k): 
    a=[0]*(k+1) #index từ 1 
    res = []
    def backtrack(i):
        #basecase 
        if i == k+1 : #index base 1 nên phải vượt quá k 
            tohop = ''.join(map(str ,a[1:]))
            res.append(tohop)
            return 
        for j in range(a[i-1]+1 , n-k+i+1) : 
            a[i] = j 
            backtrack(i+1)
    backtrack(1)
    return res 

t = int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    # print(sinh_to_hop(n,k)) để như này output sẽ có None sau khi in hết tổ hợp
    # vì print ngay trong basecase rồi còn hàm sinh_to_hop thực chất ko return về gì cuối cùng 
    print(*sinh_to_hop(n,k))
