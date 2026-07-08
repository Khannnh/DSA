import itertools 
t = int(input()) #nhập số bộ test 
for _ in range(t): 
    n , k = list(map(int , input().split()))
    so_luong_bit_0 = n-k
    for vi_tri_bit_0 in itertools.combinations(range(n) ,so_luong_bit_0 ): 
        res=[1] * n # khởi tạo mảng toàn 1 rồi điền bit 0 như vậy sẽ theo thứ tự tăng dần
        for idx in vi_tri_bit_0: 
            res[idx] = 0 
        print(*res , sep='')
        #nếu print bị đẩy vào trong thêm 1 ô thì sai vì nó sẽ in thừa rất nhiều xâu trung gian trc khi ĐỦ k bit 1
