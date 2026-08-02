#cách 1 : Sinh tổ hợp nhanh hơn 
import itertools
def tapconcuaxau(s,n):
    res = []
    for k in range(1,n+1):
        cac_tap_con = itertools.combinations(s,k)
        for tap_con in cac_tap_con: #('a','b')
            res.append("".join(tap_con))
    return sorted(res)
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()  #k cần ép kiểu về list vì str cx truy cập đc theo chỉ số 
    print(*tapconcuaxau(s,n))

#Cách 2 :Sinh nhị phân bit 0 1 rồi quy ra tập con 
import itertools
def tapconcuaxau(s,n):
    res = []
    cac_np = itertools.product([0,1], repeat = n )
    for np in cac_np:
        tap_con = []
        for i in range(n):
            if np[i] == 1 :
                tap_con.append(s[i])
        #"".join(map(str,tap_con))
        res.append("".join(map(str,tap_con)))
    return sorted(res[1:])
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(*tapconcuaxau(s,n))
