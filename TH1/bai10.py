# #cho so tien money 
# # bo tien san [1 ,2 ,5 ,10 , 20 , 50 , 100 , 200 ,500 ,1000]
# #in ra so luong to tien it nhat co the doi dc so tien money ban dau 

# bo_tien = [1000 ,500 ,200 ,100 , 50 , 20 , 10 , 5 ,2 ,1]
# # SAP XEP BO TIEN THEO THU TU GIAM DAN

# def doi_tien(money): 
#     count = 0 
#     for menh_gia in bo_tien: 
#         while money >= menh_gia: 
#             count += money //menh_gia
#             money %= menh_gia # lay phan du so tien cho menh gia roi gan lai vao money 
#     return count 
# t = int(input())
# for _ in range(t): 
#     money = int(input())
#     print(doi_tien(money))
    
menhgia = [1000,500,200,100,50,20,10,5,2,1]
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for tien in menhgia:
        cnt += n // tien
        n %= tien
        if n == 0:
            break
    print(cnt)