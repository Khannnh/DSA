#tìm k ptu lớn nhất 
t=int(input())
for _ in range(t):
    n,k=list(map(int ,input().split()))
    a= list(map(int ,input().split()))
    a.sort(reverse=True)
    for i in range(0,k):
        print(a[i] , end = ' ')
    print()