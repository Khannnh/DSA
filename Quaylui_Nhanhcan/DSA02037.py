#dãy con có tổng nguyên tố 
import itertools
def is_prime(limit):
    sang = [True]*(limit+1)
    sang[0] , sang[1] = False , False 
    for i in range(2, int(limit**0.5)+1):
        if sang[i]: 
            for j in range(i*i , limit+1 , i):
                sang[j] = False 
    return sang 

limit = 1500
sangNguyenTo = is_prime(1500)

def solve(a:list):
    n=len(a)
    a.sort(reverse=True) #sắp xếp ngược thế mà lại hay :))), nhị phân sinh nó bit 1 sau cùng lại thành bé
    res = [] #mảng in kết quả 
    cac_xau = itertools.product([0,1], repeat = n )
    for nhiphan in cac_xau: 
        tong = 0 
        for i in range(n):
            if nhiphan[i] == 1 : 
                tong+= a[i]

        if sangNguyenTo[tong]:
            path= [a[i] for i in range(n) if nhiphan[i]==1]
            res.append(" ".join(map(str,path)))
    return res 

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res = solve(a)
    print("\n".join(res))


