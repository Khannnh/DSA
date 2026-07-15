import itertools 
def check(s):
    invalid = 'HH'
    if "H" not in s or "A" not in s : 
        return False 
    if invalid in s : 
        return False 
    if not s.startswith("H") or not s.endswith('A'): 
        return False 
    return True 
t= int(input())
for _ in range(t): 
    n= int(input())
    tat_ca_xau = itertools.product (['A','H'] , repeat = n)
    for xau in tat_ca_xau: #('H' ,'A' ,'A')
        s = ''.join(xau)
        if check(s):
            print(s)
