def sinh_xau_ke_tiep(n): 
    if n%2 == 0 : 
        k = n//2
    else: 
        k = (n+1)//2 
    a=[0]*n 
    while True : 
        for i in range(k): 
            a[n-i-1] = a[i]
        print(*a) 
        #phải print luôn vì cấu hình toàn 0 đầu tiên luôn đúng 
        idx = k-1 
        while idx >= 0 and a[idx] == 1 : 
            a[idx] = 0 
            idx -= 1 
        if idx < 0 : 
            break 
        a[idx] = 1 # nhất định phải đúng vị trí vì a[-1] có nghĩa =)))
n= int(input())
sinh_xau_ke_tiep(n)