#🥲🙄 bài này có quá nhiều note ‼️‼️‼️
#tổ hợp số có tổng bằng x 
def dfs(rem_x:int , a:list , start_ids:int ,path:list, result:list):
    n=len(a)
    #basecase: nếu tổng rem_x lùi về 0 => sinh hết 1 tổ hợp 
    if rem_x==0 : 
        result.append(list(path))  # FIX: Tạo bản sao list(path) thay vì dùng path gốc
        return 
    for i in range(start_ids,n):
        #cắt nhánh sớm a[i]>rem_x : dừng luôn vì dãy a sắp xếp bé-> lớn
        if a[i]> rem_x:
            break 
        path.append(a[i])
        dfs(rem_x-a[i] ,a, i , path,result) #vẫn chọn i tiếp vì có thể chọn trùng 
        path.pop()  #khôi phục trạng thái , lui lại 1 tầng đệ quy 
t=int(input())
for _ in range(t):
    N, X = map(int , input().split())
    a= list(map(int , input().split()))
    a.sort()
    result = []
    path=[]
    dfs(X, a, 0 , path, result)
    if not result : 
        print(-1)
    else : 
        # Format lại kết quả đúng chuẩn [2 2 2 2][2 2 4]...
        out=[] # nếu in luôn result thì ko đúng format 🙄
        for p in result: 
            path= ' '.join(map(str,p))
            out.append("[" + path + "]")
        print("".join(map(str,out))) 
        #bài này dùng *out thì ko đc vì giữa ] và [ có dấu cách :))))
        #thế là phải dùng join 🙄
#https://share.gemini.google/qjgg1uNJISjs

