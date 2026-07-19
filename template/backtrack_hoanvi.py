#nhập số n , sinh các hoán vị của n 
def hoanvi(n):
    a = [0]*n
    visited = [False]*(n+1)
    def backtrack(i):
        #basecase
        if i == n : 
            print(*a)
            return 
        for j in range(1,n+1):
            if visited[j]== False : 
                a[i] = j 
                visited[j] = True 
                backtrack(i+1)
                visited[j] = False 
    backtrack(0)
n= int(input())
hoanvi(n)
        