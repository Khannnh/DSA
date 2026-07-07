#sinh nhị phân = quay lui đệ quy
def nhi_phan(n):
    a= [0]*n
    def backtrack(i):
        #basecase
        if i == n :
            print(*a)
            return

        for j in [0,1]: 
            a[i] = j 
            backtrack(i+1)
    backtrack(0)

n= int(input())
nhi_phan(n)