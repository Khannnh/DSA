import itertools 
n,k= list(map(int,input().split()))
a=list(map(int,input().split()))
arr = set(a) #phải lọc trùng xong mới sort , nếu ko phá hết thứ tự 
x = sorted(arr)
for tohop in itertools.combinations(x,k):
    s=' '.join(map(str,tohop))
    print(s)