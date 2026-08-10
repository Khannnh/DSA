#sắp xếp chọn và in ra từng bước 
#bản chất là sắp xếp n-1 ptu đầu tiên thì mảng tự động sắp xếp hết
n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    min_idx = i 
    for j in range(i+1,n):
        if a[j] < a[min_idx]:
            min_idx = j 
    a[i] , a[min_idx] = a[min_idx] , a[i]
    print(f"Buoc {i+1}:", *a) #k đc phép unpack a trong f-string 