import itertools 
n,k = list(map(int,input().split()))
chuoi = set(input().split()) #nhập chuỗi , cắt nhỏ ptu , lọc trùng
x = sorted(chuoi) # sắp xếp ( tạo mảng mới để sắp xếp)
cac_to_hop = itertools.combinations(x , k)
for th in cac_to_hop: 
    s=' '.join(th)
    print(s)
