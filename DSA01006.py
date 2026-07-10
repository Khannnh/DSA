#nhập số bộ test , mỗi test nhập số n rồi sinh các hoán vị của n nhưng in theo thứ tự cuối lội lại 
import itertools 
t= int(input())
for _ in range(t): 
    n= int(input())
    result = []
    #vì đề cho in dãy ngược nên nhập luôn range ngược =)))
    cac_hoan_vi = itertools.permutations(range(n ,0,-1))
    for hv in cac_hoan_vi: #hv : (1,2,3) cần kiểu 123
        hoan_vi = "".join(map(str , hv))
        result.append(hoan_vi)
    print(*result)

