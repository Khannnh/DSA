# tim xau AB do dai n chua duy nhat day k bit A lien tiep
#DSA01009
import itertools 
def check(s , k): 
    target = 'A'*k
    invalid = 'A'*(k+1)

    if target not in s: 
        return False 
    if invalid in s : 
        return False 
    if s.count(target) > 1 : 
        return False 
    return True 

n , k = list(map(int , input().split()))
result = []
tat_ca_xau = itertools.product(['A' , 'B'] , repeat = n)
for xau in tat_ca_xau: 
    s = ''.join(xau)
    if check(s,k) : 
        result.append(s)

#in ket qua 
print(len(result))
print("\n".join(result))
