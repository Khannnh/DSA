#số xa cách mà dùng itertools bị TLE =)))
#nhìn input 3 ko có output tức là đề nó gợi ý đệ quy cắt nhánh để khỏi xử lý khi ko có đáp án đó =)))))
#:D 
def solve(n):
    a=[0]*n
    visited= [False]*(n+1)
    def backtrack(i):
        #basecase 
        if i ==n : 
            print("".join(map(str,a)) , sep=" ")
            return #cx suýt gãy do quên return :)))
        for j in range(1,n+1):
            if visited[j] :
                continue 
            if i>0 and abs(a[i-1]-j) == 1 :  #suýt gãy do quên i>0 =)))
                continue 
            a[i] = j 
            visited[j] = True 
            backtrack(i+1)
            visited[j] = False 
    backtrack(0)
t=int(input())
for _ in range(t):
    n=int(input())
    solve(n)
