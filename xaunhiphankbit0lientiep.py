import itertools 
# sinh xâu nhị phân k bit 1 theo thứ tự tăng dần 
t=int(input())
for _ in range(t): 
    n,k = list(map(int , input().split()))
    slbit0 = n-k 
    vi_tri_bit_0 = itertools.combinations(range(n) , n-k)
    for vt in vi_tri_bit_0: # vt (0,1,2,3)
        a = [1]*n
        for i in vt : 
            a[i] = 0 
        print(''.join(map(str,a)))   