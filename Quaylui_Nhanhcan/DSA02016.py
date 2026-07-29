#sắp xếp quân hậu 1 
def solve(n): 
    ans = 0 

    colum = [False]*n 
    cheochinh = [False]*(2*n)
    cheophu = [False]*(2*n)

    def backtrack(row):
        nonlocal ans #nếu ko có dòng này thì ko thể sửa giá trị ở hàm def cha 
        #basecase 
        if row == n : 
            ans += 1 
            return 
        #duyệt các cột 
        for cot in range(n):
            if not colum[cot] and not cheochinh[row-cot+n] and not cheophu[row+cot]:
                colum[cot] = True 
                cheochinh[row-cot+n] = True 
                cheophu[row+cot] = True 
                backtrack(row+1)

                #hoàn tác 
                colum[cot] = False
                cheochinh[row-cot+n] = False
                cheophu[row+cot] = False
    backtrack(0)
    return ans 
t=int(input())
for _ in range(t):
    n=int(input())
    print(solve(n))
