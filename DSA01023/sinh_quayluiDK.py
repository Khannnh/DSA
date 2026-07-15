#hàm nhận đầu vào n , k , xau mục tiêu 
#sinh đệ quy xâu , vừa sinh vừa đếm thứ tự , tới khi gặp xâu mục tiêu thì dừng
#cần biến count để đếm thứ tự , biến cờ found để biết khi nào dừng ? 
#cân thêm biến ans để trả về vị trí nữa , ans chỉ bằng found khi tìm đc xau mục tiêu 
# vẫn cần mảng a k + 1 ptu để sinh đệ quy ,mấy biến trên để quay lui sớm:)))
def thu_tu_to_hop(n,k,target):
    a= [0]*(k+1)
    state = {
        'count': 0,
        'found' : False,
        'ans' : -1
    }
    def backtrack(i):
        #nhánh cắt sớm nếu tìm thấy rồi thì ko đệ quy nữa
        if state['found'] : 
            return 
        if i >k : # khi sinh xong đủ bit của 1 tổ hợp
            state['count']  += 1
            if a[1:] == target : # vậy là target phải dạng list các số nguyên à?
                state['found'] = True
                state['ans'] = state['count']
            return 
        for j in range(a[i-1]+1 , n-k+i+1):
            a[i] = j
            backtrack(i+1)
    backtrack(1)
    return state['ans']
t= int(input())
for _ in range(t):
    n, k = list(map(int,input().split()))
    to_hop = list(map(int,input().split()))
    print(thu_tu_to_hop(n,k,to_hop))

        
        