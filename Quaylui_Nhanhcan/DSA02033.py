import itertools , math
def check(s ,n):
    ok = True 
    for i in range(0,n-1):
        if abs(s[i]-s[i+1]) == 1 : 
            ok = False 
            break 
    if ok:
        return True 
    else: 
        return False 
    
t=int(input())
for _ in range(t):
    n=int(input())
    for th in itertools.permutations(range(1,n+1)):
        if check(th ,n ):
            print("".join(map(str,th)))
    