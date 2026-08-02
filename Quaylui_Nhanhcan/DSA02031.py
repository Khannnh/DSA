import itertools
def check(s):
    n=len(s)
    for i in range(1,n-1):
        if s[i] in "AE": # ptu là nguyên âm
            if s[i-1] not in "AE" and s[i+1] not in "AE": #đằng trc đằng sau là phụ âm
                return False 
    return True 

c=input()
tap = []
for i in range(ord(c)-ord("A")+1):
    tap.append(chr(65+i))
for xau in itertools.permutations(tap):
    if check(xau):
        print("".join(xau))
