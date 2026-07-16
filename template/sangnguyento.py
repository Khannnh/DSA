#sàng nguyên tố có giới hạn trên , trả về list boolean 
#phần tử tại vị trí i nào có giá trị True thì i là số nguyên tố , ngược lại False thì i là hợp số 
def sangnguyento(limit): 
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1]= False
    for i in range(2,int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i , limit+1 , i):
                is_prime[j] = False 
    return is_prime

limit = 10**6 
sangngto = sangnguyento(limit) #list
n=int(input())
if sangngto[n] : 
    print(f"{n} là số nguyên tố")
else: 
    print(f"{n} ko là số nguyên tố")

#có thể tối ưu bài này bằng cách loại trước bội chẵn của 2 rồi cắt mảng gì gì đấy nữa 
