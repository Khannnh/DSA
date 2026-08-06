#DSA06013
def demTanSuat(a:list,x:int):
    freq = {} #dùng dic để đếm
    for i in a : 
        freq[i] = freq.get(i , 0 ) + 1
    if freq.get(x,0) == 0 : 
        return -1 
    else : 
        return freq.get(x)
t=int(input())
for _ in range(t):
    n,x = map(int ,input().split())
    a = list(map(int , input().split()))
    print(demTanSuat(a,x))