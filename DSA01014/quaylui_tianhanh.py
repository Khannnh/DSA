def soluongthtongs(n,k,s):
    if k> n or (k*(k+1)//2 > s): 
        return 0
    state = {
        'ans':0
    }
    def backtrack(i ,start,current_sum):
        if current_sum > s :
            return
        if i == k+1 :
            if current_sum == s : 
                state['ans'] += 1 
            return 
        for j in range(start , n-k+i+1): 
            # i + 1: Tiến sang điền ô tiếp theo
            # j + 1: Số ở ô sau phải lớn hơn số ở ô trước (tránh trùng hoán vị)
            # current_sum + j: Cộng dồn số j vừa chọn vào tổng
            if current_sum + j > s : 
                break 
            backtrack(i+1, j+1 , current_sum+j)
    # Kích hoạt đệ quy: Điền từ ô thứ 1, các số được chọn từ 1 trở đi, tổng ban đầu là 0
    backtrack(1, 1, 0)
    return state['ans']
while True : 
    n,k,s = list(map(int,input().split()))
    if n==k==s==0:
        break 
    print(soluongthtongs(n,k,s))