import itertools 
while True : 
    n,k,s = list(map(int,input().split()))
    if n==k==s==0 :
        break
    cac_th = itertools.combinations(range(1,n+1),k)
    count = 0 
    for th in cac_th: #dạng(1,2,3)
        tong = 0 
        for i in range(k): 
            tong += th[i]
        if tong == s : 
            count += 1 
    print(count)
        





