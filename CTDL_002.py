import itertools 
n,k = list(map(int , input().split()))
a= list(map(int , input ().split()))
result = []
tat_ca_xau = itertools.product([0,1] , repeat = n )
for xau in tat_ca_xau: # 1 xâu là 1 tập con có tổng riêng => tổng trong for xau 
    tong= 0 
    for i in range(n): 
        if xau[i] == 1 : #vị trí đó đc chọn => cộng vào tổng 
            tong+= a[i]

    if tong == k : 
        tap_con = [a[i] for i in range(n) if xau[i]== 1]
        result.append(" ".join(map(str , tap_con)))

print('\n'.join(result)) # in các ptu cách dòng 
print(len(result ))