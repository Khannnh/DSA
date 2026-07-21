#Mã gray 3:biến xâu nhị phân thành xâu gray
t=int(input())
for _ in range(t):
    xau=input()
    s=list(map(int,xau))#chặt ra thành list các số nguyên
    #bit đầu giữ nguyên
    res = [s[0]]
    #bit sau xor với thằng trc nó
    for i in range(1,len(s)):
        res.append(s[i]^s[i-1])
    gray= "".join(map(str ,res))
    print(gray)