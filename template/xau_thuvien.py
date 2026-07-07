import itertools 
n=int(input())
tat_ca_xau = itertools.product([0,1] , repeat = n)
for xau in tat_ca_xau: 
    print(xau)#kiểu tuple , chỉ khác list ở chỗ ko thể crud các ptu 
