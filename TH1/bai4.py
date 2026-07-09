# cho mang a 
#in ra VI TRI  cua phan tu trong mang do ma tong trai , phai = nhau 
#index bat dau tu 1 

def vitricanbang(a): 
    total_sum = sum(a)
    left_sum = 0 
    for i in range(len(a)):
        # left_sum += a[i]
        right_sum = total_sum-left_sum-a[i]
        if left_sum== right_sum: 
            return i+1 
        left_sum+= a[i] # chuyen xuong duoi de no ko cong thua chinh no?????
    return -1 
t= int(input())
for _ in range(t): 
    n= int(input())
    a = list(map(int , input().split()))
    print(vitricanbang(a))