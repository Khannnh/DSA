import itertools 
n=int(input())
tat_ca_xau = itertools.product([0,1] , repeat = n)
for xau in tat_ca_xau: 
    if xau == xau[::-1] : 
        print(*xau)