#dãy con liên tiếp có tổng lớn nhất 
#vì đề bài iko yêu cầu liệt kê các dãy con thỏa mãn nên bài toán trở nên khá dễ dàng
def dayconlientieptonglon(a):
    n=len(a)
    tong_hien_tai , tong_lon_nhat = a[0] , a[0]
    #bỏ qua ptu đầu tiên luôn
    for i in range(1,n):
        tong_hien_tai = max(a[i] , tong_hien_tai+a[i])
        if tong_hien_tai > tong_lon_nhat : 
            tong_lon_nhat = tong_hien_tai
    return tong_lon_nhat
t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int ,input().split()))
    print(dayconlientieptonglon(a))



