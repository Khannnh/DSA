def solve(s,d):
    #điều kiện vô nghiệm 
    if s > d*9 or s == 0 : 
        print(-1) 
        return 
    res = [0]*d
    s-= 1 # để số đó ko thể bắt đầu = 0 
    for i in range(d-1,0,-1):
        if s >= 9 :
            res[i] = 9 
            s-= 9 
        else: 
            res[i] = s 
            s = 0 
    res[0]= 1+s 
    print(''.join(map(str,res)))
t=int(input())
for _ in range(t): 
    S , D = map(int , input().split())
    solve(S,D)

    