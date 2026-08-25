#bài đổi tiền 
menh_gia = [1000,500,200,100,50,20,10,5,2,1]
t=int(input())
for _ in range(t):
    n=int(input())
    to_tien = 0
    for x in menh_gia:
        #phải chia tờ tiền trc :)))
        to_tien += n//x #chia lấy phần nguyên
        #sau đó mới trừ đi
        n%= x 
    print(to_tien)
