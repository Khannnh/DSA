#in tất cả các xâu rồi lọc điều kiện do n khá nhỏ 
import itertools
def phatloc(s):
    n= len(s)
    if n< 5 or n > 16 : return False 
    if not s.startswith('8') or not s.endswith('6'): return False 
    if '88' in s : return False
    if '6666' in s : return False 
    return True 

n= int(input())
result = []
tat_ca_xau = itertools.product(['6','8'] , repeat = n) # xếp theo thứ tự 
for xau in tat_ca_xau: 
    s= ''.join(xau)
    if phatloc(s):
        result.append(s)
for i in result:
    print(i)