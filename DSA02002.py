#dãy số 2 
def dfs (a):
    #basecase
    if len(a) == 1 : 
        print('['+ " ".join(map(str,a)) + ']' , end = " ")
        return 
    #xử lý 
    next_a=[]
    for i in range(0,len(a)-1):
        two_sum = a[i] + a[i+1]
        next_a.append(two_sum)
    dfs(next_a)
    #[48] [20 28] [8 12 16] [3 5 7 9 ] [1 2 3 4 5 ]
    #vì mỗi lần gọi đệ quy là đang xử lý chính nó nên in chính nó
    #nhưng khi chạm tới basecase thì lui về hàm trc nó nên ko kịp in => in luôn ở basecase 
    print('['+ " ".join(map(str,a)) + ']' , end = " ")
t=int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int , input().split()))
    dfs(a)
    print() #output mẫu ko có nhiều test nhưng t quên xuống dòng sau mỗi test (╬▔皿▔)╯
