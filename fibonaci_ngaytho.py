modulo = 100000007
result = [0]*modulo 
result[1] = 1 
for i in range(2, 100000000):
    result[i] = (result[i-1] + result[i-2]) % modulo
t=int(input())
for _ in range(t):
    n=int(input())
    print(result[n])


