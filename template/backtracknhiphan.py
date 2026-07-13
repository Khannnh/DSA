#sinh nhị phân = quay lui đệ quy
def nhi_phan(n):
    a= [0]*n
    def backtrack(i):
        #basecase
        if i == n : #index base 0 nên i = n là vượt quá index cuối (n-1) rồi =))))
            print(*a)
            return

        for j in [0,1]: 
            a[i] = j 
            backtrack(i+1)
    backtrack(0)

n= int(input())
nhi_phan(n)