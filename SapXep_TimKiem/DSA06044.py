def sapxepchanle(arr):
    chan = []
    le = []
    a=[0]+ arr #thêm ptu cho đúng vị trí từ 1
    for i in range(1,len(a)+1):
        if i %2 == 0 : 
            chan.append(a[i])
        else:
            le.append(a[i])
    chan.sort(reverse=True) #chẵn giảm 
    le.sort() #tăng 

    i = 0 #duyệt chẵn 
    j = 0 #duyệt lẻ 

    for pos in range(1,len(a)+1):
        if pos %2 == 0 : #vị trí chẵn 
            a[pos] = chan[i]
            i+= 1
        else: #vị trí lẻ 
            a[pos] = le[j]
            j+= 1 
    return a[1:]
n=int(input())
x = list(map(int , input().split()))
print(*(sapxepchanle(x)))




