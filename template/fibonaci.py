#thực ra số fibonacii tăng khá nhanh :)))) nên ta làm theo kiểu tìm kiếm trên set -> o(1)
#thậm chí fix cứng dãy fibonacci bên ngoài cũng đc luôn :))), số nguyên tố gọi = cụ 
#template tạo dãy fib ở ngoài kiểu set rồi check xem x có trong set ko 
fib = set()
a, b = 0 , 1
while a <= 10**9 : #hoặc thay = limit 
    fib.add(a)
    a,b= b,a+b 
fibonaci = sorted(fib)  #nếu cần thứ tự còn ko cần thì khỏi , mất công tạo list :))) 
print(len(fibonaci))
print(*fibonaci)

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


    