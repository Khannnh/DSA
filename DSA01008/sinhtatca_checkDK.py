#sinh xau nhị phân có k bit 1
import itertools
def kiemtra(n,k):
    tat_ca_xau = itertools.product([0,1] , repeat = n )
    for xau in tat_ca_xau:
        if xau.count(1) == k : 
            print(*xau , sep = '')
t = int(input()) #nhập số bộ test
for _ in range(t):
    a= list(map(int, input().split()))
    kiemtra(a[0],a[1])
