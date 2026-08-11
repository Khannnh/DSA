n=int(input())
a=list(map(int,input().split()))
step = 1 #biến step để in ra số bước , bắt đầu từ 1
for i in range(n-1):
    swapped = False #thêm biến step vì output chỉ in khi có đổi chỗ
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j] , a[j+1] = a[j+1],a[j]
            swapped = True 
    if swapped : 
        print(f"Buoc {step}:",*a)
        step += 1 
    else: 
        break 