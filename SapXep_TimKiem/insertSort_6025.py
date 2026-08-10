n = int(input())
a = list(map(int, input().split()))

print("Buoc 0:", a[0])

for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j] #shift ( đẩy sang bên phải để trống chỗ thích hợp cho key)
        j -= 1
    a[j + 1] = key
    print(f"Buoc {i}:", *a[:i+1])