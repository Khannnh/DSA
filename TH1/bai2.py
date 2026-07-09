#cho so tu nhien n 
# tim 2 so nguyen to dau tien co tong = n 
# neu ko tim dc in -1 

#dau vao la limit , tra ve mang boolean danh dau so nguyen tu 0 -> limit 
def sangnguyento(limit):
    is_prime = [True] * (limit + 1) 
    is_prime[0] = is_prime[1] = False 

    for p in range(2, int(limit**0.5)+ 1):
        if is_prime[p]:
            for i in range(p*p , limit +1 , p): 
                is_prime[i] = False 
    return is_prime

max = 1000000
prime_check = sangnguyento(max)
t = int(input()) #nhap so bo test 
for _ in range(t): 
    n= int(input())
    found = False 
    for i in range(2 , n//2+1): 
        if prime_check[i] and prime_check[n-i]: 
            found = True 
            print(i , n-i)
            break # tim nho nhat nen break 
    if not found : 
        print (-1)
