import itertools 
n=int(input())
cac_hoan_vi = itertools.permutations(range(1,n+1))
stt = 0 
for hoan_vi in cac_hoan_vi: #(1,2,3)
    s=' '.join(map(str ,hoan_vi)) #"1 2 3"
    stt += 1 
    print(f"{stt}: {s}")

# import itertools 
# n=int(input())
# cac_hoan_vi = itertools.permutations(range(1 , n+1))
# stt=1 
# result = []
# for hoan_vi in cac_hoan_vi: 
#     # print(f"{stt}:", *hoan_vi) 
#     #mỗi vòng for in 1 lần làm tốn bộ nhớ hơn => tạo mảng rồi in ds mỗi ptu của mảng trên 1 dòng
#     chuoi_hoan_vi = ' '.join(map(str , hoan_vi))
#     result.append(f"{stt}: {chuoi_hoan_vi}")
#     stt+= 1
# print('\n'.join(result))