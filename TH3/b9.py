#bài quy hoạch động
#tìm dãy con chung dài nhất 
import sys 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data : 
        return 
    t=int(input_data[0])
    idx = 1
    out =[]
    for _ in range(t):
        s1=input_data[idx]
        s2= input_data[idx+1]
        idx += 2

        n,m = len(s1) , len(s2)

        dp = [0]*(m+1)

        for c1 in s1 : 
            prev = 0 
            for j in range(1 , m+1):
                temp = dp[j]
                if c1 == s2[j-1]:
                    dp[j] = prev +1 
                else : 
                    if dp[j-1] > dp[j]:
                        dp[j] = dp[j-1]
                prev= temp 
        out.append(str(dp[m]))
    print('\n'.join(out))
if __name__ == '__main__':
    solve()
# def dayconchungdainhat(s1,s2):
#     n=len(s1)
#     m=len(s2)

#     #tạo bảng dp kích thước (n+1) x (m+1) toàn số 0 
#     dp = [[0]*(m+1) for _ in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if s1[i-1] == s2[j-1]:
#                 #nếu 2 kq giống nhau +1 vào kq trc đó 
#                 dp[i][j] = dp[i-1][j-1] +1
#             else :
#                 dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
#     return dp[n][m]
# t=int(input())
# for _ in range(t):
#     s1=input()
#     s2=input()
#     print(dayconchungdainhat(s1,s2))