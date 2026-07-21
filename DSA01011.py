#hoán vị tiếp theo của chuỗi số ( KO LỌC TRÙNG)
#type của a là list các int 
def hoanviketiep(a):
    n=len(a)
    pos = -1 
    for i in range(n-2,-1,-1):
        if a[i] < a[i+1]:
            pos = i 
            break #nhớ break (vì tìm vị trí đầu tiên )
    if pos == -1 : #cấu hình lớn nhất 
        return "BIGGEST"
    for j in range(n-1,pos,-1):
        if a[j] > a[pos]:
            a[j] , a[pos] = a[pos] , a[j]
            break 
    a[pos+1:] = a[pos+1:][::-1]
    return "".join(map(str, a))
t=int(input())
for _ in range(t): 
    s = input().split()
    stt=s[0]
    chuoi = s[1]
    chuoi_so = list(map(int,chuoi))
    result = hoanviketiep(chuoi_so)
    print(f"{stt} {result}")