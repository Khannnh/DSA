import itertools 
def sangnguyento(limit): 
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1]= False
    for i in range(2,int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i , limit+1 , i):
                is_prime[j] = False 
    return is_prime

sang = sangnguyento(200000) #ds gồm toàn giá trị True/False 
n,k = list(map(int, input().split()))
cac_to_hop = itertools.combinations(range(1,n+1) , k)
stt = 0 
for to_hop in cac_to_hop:
    stt +=1 
    if sang[stt] :
        s = " ".join(map(str , to_hop))
        print(f"{stt}: {s}")