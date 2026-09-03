#máy atm 
def mayAtm(t:list , s:int) -> int: 
    n = len(t)
    t.sort(reverse=True)
    min_bill = 10**9 

    def dfs (i:int , rem : int , count:int)-> int: 
       #cho phép sửa giá trị của hàm cha
        nonlocal min_bill
       #basecase 1 : nếu đổi đc tiền 
       #chỉ cập nhật biến kỉ lục chứ ko return để nhánh tỉa khác còn dùng 
        if rem == 0 : 
            min_bill=  min(min_bill , count)
            return 
        #basecase 2 : hết ptu hoặc chạm cận min_bills
        if i == n : 
            return 
        #nếu số tờ hiện tại chạm kỉ lục => dừng luôn
        if count >= min_bill : 
            return 
       #nhánh 1 : chọn t[i]
        if rem >= t[i] and count+1 < min_bill: 
           dfs(i+1, rem - t[i], count+1)
        #nhánh 2 : ko chọn t[i]
        dfs(i+1,rem ,count)
    dfs(0,s,0)
    if min_bill != 10**9 : 
        return min_bill
    else : return -1 

botest=int(input())
for _ in range(botest):
    n,s = map(int , input().split())
    t = list(map(int ,input().split()))
    print(mayAtm(t , s))
