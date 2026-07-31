# Nếu làm kiểu trâu bò thì ý tưởng sẽ là dùng 3 vong for: 
# for i in (n-2) : 
# 	for j in (i+1,n-1)
# 		for k in (j+1,n) 
# Nhưng với n = 5000 thì thời gian chạy 5000^3 là bất khả thi 
# -> Si nghĩ cố định vòng for i ở ngoài cùng thôi , j và k thì biến thành 2 con trỏ left , right thu gọn đoạn từ i+1 tới n . Điều kiện để áp dụng đc 2 con trỏ là phải SORT cái mảng đã :))) 
# for i in (n-2) 	
# 	l = i+1 
# 	r = n-1 (index) 
# 	while l<r : 
# 	tong = a[i] + a[l] + a[r] 
# 	Nếu tong < k : 
# 		đoạn từ l+1 -> r-1 đều thỏa mãn => ans += (r-l-1) +1 = r-l
# 		l +=1 
# 	Nếu tong >= k : 
# 		r -= 1 

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