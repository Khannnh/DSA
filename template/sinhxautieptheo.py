#nhập xâu độ dài n , in ra 1 xâu kế tiếp của xâu n 
def sinh_xau_ke_tiep(a):
    n= len(a)
    arr = a.copy()

    idx = n-1
    while idx >= 0 and arr[idx]==1:
        arr[idx] = 0 
        idx -= 1 
    if idx < 0 : 
        print("đây là xâu cuối cùng , ko có xâu kế tiếp")
        return 
    arr[idx] = 1  
    print("xâu ban đầu: " , *a)
    print("xâu kế tiếp : " , *arr)

a = list(map(int , input().split()))
sinh_xau_ke_tiep(a)
