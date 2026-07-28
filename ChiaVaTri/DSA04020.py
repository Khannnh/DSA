#tìm kiếm nhị phân 
def binarysearch(k:int,a:list):
    l= 0 
    h = len(a)-1 
    while l <= h : 
        mid = (l+h)//2
        if k== a[mid] : 
            return mid + 1 
        elif k < a[mid] : 
            h= mid - 1
        elif k > a[mid]:
            l = mid + 1
    return "NO"
t=int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a= list(map(int,input().split()))
    print(binarysearch(k,a))

#tìm kiếm nhị phân 
# def binarysearch(k:int,a:list):
#     n=len(a)
#     def dfs(l,h):
#         mid = (l+h) // 2
#         #basecase 
#         if l <= h : 
#             if a[mid] == k : 
#                 return mid + 1 
#             elif k > a[mid] : #tìm nửa phải , bỏ trái  
#                 return dfs(mid+1 , h)
#             elif k < a[mid]:
#                 return dfs(l,mid-1)
#         return "NO"
#     return dfs(0,n-1) #return kết quả của dfs đầu tiên 

# t=int(input())
# for _ in range(t):
#     n,k = list(map(int,input().split()))
#     a= list(map(int,input().split()))
#     print(binarysearch(k,a))