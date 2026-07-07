#sinh xau nhị phân có k bit 1
import itertools
def kiemtra(n,k):
    tat_ca_xau = itertools.product([0,1] , repeat = n )
    for xau in tat_ca_xau:
        count = 0
        for j in range(n):
            if xau[j] == 1 :
               count += 1
        if count == k :
            print(*xau , sep = '')
        # ban đầu mình ko print mà return luôn xau type tuple rồi dự định xử lý
        # output ở ngoài nhưng ko thể return hay break trong vòng lặp nếu ko vòng lặp
        # sẽ dừng luôn nên mình in luôn trong hàm

t = int(input()) #nhập số bộ test
for _ in range(t):
    a= list(map(int, input().split()))
    kiemtra(a[0],a[1])
