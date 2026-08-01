import itertools
n,k=list(map(int,input().split()))
a= list(map(int,input().split()))
cnt = 0 
cac_th = itertools.combinations(a , k)
for th in cac_th:
    if list(th) == sorted(th):
        #th là kiểu tuple nên ko có th.sort()
        #sorted của tuple trả về list nên chỉ cần ép kiểu 1 bên
        cnt += 1 
print(cnt)