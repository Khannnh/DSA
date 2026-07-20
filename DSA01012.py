#mã gray 1 
def sinhmagray(n):
    res= ['0','1']
    for _ in range(2,n+1):
        trong_guong = res[::-1]

        #nửa thật thêm 0 vào đầu 
        nua_dau = []
        for i in res : 
            nua_dau.append("0"+ i)
        
        #nửa sau thêm 1 vào đầu
        nua_sau = []
        for i in trong_guong:
            nua_sau.append("1"+i)
        
        res = nua_dau+nua_sau
    return res 
t=int(input())
for _ in range(t):
    n= int(input())
    print(*sinhmagray(n))
