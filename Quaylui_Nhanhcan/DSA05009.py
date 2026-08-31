def tapconbangnhau(a:list):
    n = len(a)
    tong = sum(a) 
    if tong % 2 != 0 : return "NO"
    else : target = tong / 2

    #sắp xếp tổng theo thứ tự giảm dần để dễ đáp ứng cắt nhánh
    a.sort(reverse= True)
    
    def dfs(i:int , total:int)-> bool:
        # Base case: đạt mục tiêu
        if total == target:
            return True
        
        # Base case & Tỉa nhánh: hết phần tử hoặc vượt quá target
        if i == n or total > target:
            return False

        #nhánh chọn a[i]
        if dfs(i+1 , total + a[i]) : return True
        #nhánh ko chọn a[i]
        if dfs(i+1 , total):return True
        return False 
    
    #trạng thái đầu tiên từ index 0 , tổng = 0 
    if dfs(0,0): return "YES"
    else : return "NO"
t= int(input())
for _ in range(t):
    n = int(input())
    a= list(map(int , input().split()))
    print(tapconbangnhau(a))