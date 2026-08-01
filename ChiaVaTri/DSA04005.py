fib = [0] *93

fib[1] = 1  #len(G(1)) = 1 (A)
fib[2] = 1  #len(G(2)) = 1 (B)

for i in range(3,93):
    fib[i] = fib[i-2] + fib[i-1]

def find_char(n,pos):
    #basecase
    if n == 1 : 
        return "A"
    if n == 2 : 
        return "B"
    
    if pos <= fib[n-2]:
        return find_char(n-2 , pos)
    else: 
        return find_char(n-1, pos-fib[n-2])
t=int(input())
for _ in range(t):
    n,i = list(map(int,input().split()))
    print(find_char(n,i))
