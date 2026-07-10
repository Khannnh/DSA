# #xâu AB độ dài n , nhập số bộ test , nhập độ dài n , in theo thứ tự từ điển 
# import itertools 
# t= int(input())
# for _ in range(t): 
#     n= int(input())
#     result = []
#     tat_ca_xau = itertools.product(['A','B'] , repeat = n)
#     for xau in tat_ca_xau: 
#         s=''.join(xau)
#         result.append(s)
#     print(*result)


#nhập số n _ sinh ra xau độ dài n 
def sinh_nhi_phan(n):
    result = []
    a=['']*n 
    def backtrack(i):
        #basecase 
        if i == n :
            result.append("".join(a)) # ko hiểu sao nếu ko có join thì chỉ in xâu cuối toàn B???
            return 
        for j in ['A','B']:
            a[i] = j 
            backtrack(i+1)
    backtrack(0)
    return result

t= int(input())
for _ in range(t):  
    n= int(input())
    print(*sinh_nhi_phan(n))
