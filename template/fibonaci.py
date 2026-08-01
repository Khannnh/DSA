# kiểm tra 1 số có phải là số Fibonacci không khi n khá nhỏ
def is_fibonacci(n):
    if n < 0: #xử lý như này để công nhận số 0 là số fibonaci 
        return False
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        # phải gán đồng thời:
        # nếu tách 2 dòng thì a đã thay đổi trước khi tính b
        a, b = b, a + b
    return False
n = int(input())
if is_fibonacci(n):
    print(f"{n} là số Fibonacci")
else:
    print(f"{n} không là số Fibonacci")