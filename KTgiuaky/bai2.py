def TongLienTiepLonNhat(a:list):
    n=len(a)
    tong_hien_tai , tong_lon_nhat = a[0] , a[0]
    #duyệt các ptu từ trừ ptu đầu tiên-> hết 
    for i in range(1,n):
        #tạo dãy mới hoặc cộng a[i] vào dãy cũ 
        tong_hien_tai = max(a[i], tong_hien_tai+a[i])
        #cập nhật kỷ lục nếu tìm thấy tổng lớn hơn
        if tong_hien_tai>tong_lon_nhat: 
            tong_lon_nhat = tong_hien_tai
    return tong_lon_nhat
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int , input().split()))
    print(TongLienTiepLonNhat(a))