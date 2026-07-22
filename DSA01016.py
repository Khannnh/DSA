# bài toán phân tích 1 số n thành tổng của n số nhỏ hơn 
#dùng đệ quy backtrack
def dfs(tong_con_lai:int, last:int , path:list):
    #basecase
    if tong_con_lai==0 : 
        p=" ".join(map(str,path))
        print("(" + p + ")" , end = " ") # in tiếp theo cách 1 khoảng trống 
        return 
    for x in range(min(tong_con_lai,last),0,-1):
        path.append(x)
        dfs(tong_con_lai-x ,x ,path)
        path.pop()
t=int(input())
for _ in range(t):
    n=int(input())
    dfs(n,n,[]) #trong hàm dfs có print rồi
    print() #print này để xuống dòng sau mỗi bộ test

