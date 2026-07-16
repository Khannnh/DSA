import math , itertools 
import math
# Dùng sàng Eratosthenes để tìm tất cả số nguyên tố từ 2 đến limit.
# Đầu vào : limit
# Đầu ra  : mảng boolean nguyento[]
#           nguyento[i] = True  nếu i là số nguyên tố
#           nguyento[i] = False nếu i không phải số nguyên tố

def sangnguyento(limit):
    nguyento = [True] * (limit + 1)
    nguyento[0] = nguyento[1] = False

    # Chỉ cần xét tới căn(limit)
    for i in range(2, int(math.sqrt(limit)) + 1):
        if nguyento[i]:
            # Gạch các bội của i, bắt đầu từ i*i
            # vì các bội nhỏ hơn đã bị các số nhỏ hơn i gạch rồi.
            for j in range(i * i, limit + 1, i):
                nguyento[j] = False

    return nguyento

n,k = list(map(int , input().split()))
limit = math.comb(n, k)
is_prime = sangnguyento(limit)
cac_to_hop = itertools.combinations(range(1,n+1) , r = k)
stt = 0 
res = []
for to_hop in cac_to_hop: 
    stt+= 1 
    s = ' '.join(map(str , to_hop))
    if is_prime[stt]: 
        # print(f"{stt}: {s}")
        res.append(f"{stt}: {s}")
print('\n'.join(res))

