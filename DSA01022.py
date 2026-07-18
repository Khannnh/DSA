#số thứ tự của hoán vị
#sinh quay lui tới khi sinh tới target , trả về số thứ tự của target 
def thutuhoanvi(n,target): 
    a= [0]*n #1 hoán vị hoàn chỉnh
    visited= [False]*(n+1)
    state = {
        "found": False ,
        "cnt": 0 ,# để đếm thứ tự 
        "ans" : -1 #để trả về thứ tự của target 
    }
    def backtrack(i):
        #basecase nếu tìm thấy thì ko đệ quy nữa  
        if state["found"]: 
            return 
        #khi sinh đủ n thì cập nhật cnt 
        if i == n : 
            state["cnt"] += 1 
            #nếu tìm đc target 
            if a == target : 
                state["ans"] = state["cnt"]
                state["found"] = True 
                return 
        for j in range(1,n+1): 
            if visited[j] == False : 
                a[i] = j 
                visited[j] = True 
                backtrack(i+1)
                visited[j] = False 
    backtrack(0)
    return state["ans"]
t= int(input())
for _ in range(t):
    n= int(input())
    hoanvi = list(map(int,input().split()))
    print(thutuhoanvi(n,hoanvi))

    