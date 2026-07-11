#tối đa 20 bộ test , input dừng khi nhập a=b=0 
def power(a,b): 
    #base case 
    if b==0 : 
        return 1 
    
    t=power(a,b//2)
    t_sq = (t*t)%1000000007

    if b%2 == 0 : 
        return t_sq
    else: 
        return (a*t_sq)%1000000007 

for _ in range(20): 
    a,b= list(map(int , input().split()))
    if a== 0 and b ==0 : 
        break 
    else: 
        print(power(a%1000000007,b))