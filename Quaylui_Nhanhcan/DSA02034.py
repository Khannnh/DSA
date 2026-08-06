#cách 1 : Đệ quy cắt nhánh 
def hoanvi(n):
    res = [] 
    a = [0]*n 
    visited = [False]*(n+1)
    def backtrack(i):
        #basecase 
        if i == n : 
            res.append("".join(map(str,a)))
            return 
        for j in range(1,n+1): #tập lựa chọn 
            if visited[j] : 
                continue 
            if i>0 and abs(a[i-1] - j) == 1 : 
                continue 
            a[i] = j 
            visited[j] = True 
            backtrack(i+1)
            visited[j] = False 
    backtrack(0)
    return res 

t=int(input())
for _ in range(t):
    n=int(input())
    r = hoanvi(n)
    print("\n".join(r))

#cách 2 : Sinh tất rồi lọc điều kiện 
#bài này cần kt điều kiện 2 ký tự trong s đều hơn kém nhau >1 đv 
#thuần xử lý cộng trừ nên có thể dùng mảng các số nguyên 
import itertools 
def check(s): #check tuple đc :)))
    n= len(s)
    dieu_kien  = True 
    for i in range(n-1):
        if abs(s[i] - s[i+1]) == 1 : 
            dieu_kien = False 
            break 
    if dieu_kien : 
        return True 
    else: 
        return False 
t=int(input())
for _ in range(t):
    res = []
    n=int(input())
    for x in itertools.permutations(range(1,n+1)):
        if check(x): 
            res.append("".join(map(str,x)))
    print("\n".join(res))