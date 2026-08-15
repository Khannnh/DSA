import itertools 
def check(s , k):
    if s.count("01") == k : 
        return True 
    return False 
res = []
n , k = list(map(int , input().split()))
tat_ca_xau = itertools.product(['0','1'] , repeat = n )
for xau in tat_ca_xau:
    s = "".join(xau)
    if check(s,k):
        res.append(s)
print("\n".join(res))
