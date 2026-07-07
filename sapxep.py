def partition(arr, l , h):
    #chọn pivot cuối cùng
    x = arr[h]
    i = l-1 
    
    for j in range (l, h): 
        if arr[j] <= x:
            i += 1 
        
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[h] = arr[h] , arr[i+1]
    return i+1 
    
def quicksort(a, l, h): 
    if l < h : 
        pivot_idx = partition(a,l,h)
        quicksort(a, l , pivot_idx-1)
        quicksort(a,pivot_idx+1 ,h)
    
    return a
    
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    quicksort(a, 0 , len(a)-1)
    print(*a)