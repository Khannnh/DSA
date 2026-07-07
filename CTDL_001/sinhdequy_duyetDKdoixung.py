def kiem_tra_doi_xung(a): 
    left= 0 
    right= len(a)-1
    while left < right : 
        if a[left] != a[right]:
            return False 
        left+= 1 
        right-= 1 
    return True 

def sinh_xau_thuan_nghich(n): 
    a = [0]*n 
    def backtrack(i): 
        #basecase 
        if i == n : 
            if a == a[::-1]: 
                print(*a)
            return # phải ngắt ngay 
        for j in [0,1]: 
            a[i] = j 
            backtrack(i+1)
    backtrack(0)

n=int(input())
sinh_xau_thuan_nghich(n)
