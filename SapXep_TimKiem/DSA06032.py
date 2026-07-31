#tìm bộ 3 số trong list a có tổng < k 
import math , sys 
def tong3sonhohonk(a:list ,k:int):
    ans = 0 
    n=len(a)
    for i in range(n-2):
        ai = a[i]
        #cắt nhánh 1 : 3 số nhỏ nhất >=k thì break luôn 
        if ai + a[i+1]+a[i+2] >= k : 
            break 
        #cắt nhánh 2 : nếu 2 số l , r max thỏa mãn . mọi cặp i+1->n đều thỏa mãn 
        if ai + a[n-2] + a[n-1] < k : 
            solg = n-i-1 #số ptu sau i (i+1 -> n-1 - index)
            # ans += math.comb(solg,2)
            ans += solg * (solg - 1) // 2
            continue
        l = i+1 
        r = n-1 #index 
        while l < r:
            if ai + a[l] + a[r] < k:
                ans += r - l
                l += 1
            else:
                r -= 1
    return ans 

input_data = sys.stdin.read().split()
iterator = iter(input_data)
t=int(next(iterator))
for _ in range(t):
    n=int(next(iterator))
    k=int(next(iterator))
    a=[int(next(iterator)) for _ in range(n)]
    a.sort() #NHẤT ĐỊNH PHẢI SORT
    print(tong3sonhohonk(a,k))