def xuat_hien_nhieu_nhat(a:list):
    freq = {}
    max_freq = 0
    ans = None

    for x in a:
        freq[x] = freq.get(x, 0) + 1

        if freq[x] > max_freq:
            max_freq = freq[x]
            ans = x

    if max_freq > len(a) // 2:
        return ans
    else:
        return "NO"
t=int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int , input().split()))
    print(xuat_hien_nhieu_nhat(a))