import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out_lines = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Đếm trực tiếp
        count = [0] * 10000
        for _ in range(n):
            count[int(data[idx])] += 1
            idx += 1
        
        # Tạo output
        line_parts = []
        for val in range(10000):
            c = count[val]
            if c:
                # Thêm val lặp c lần
                line_parts.append(' '.join([str(val)] * c))
        
        out_lines.append(' '.join(line_parts))
    
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()

def counting_sort(arr):
    count = [0] * 10000
    for x in arr:
        count[x] += 1
    
    res = []
    for i in range(10000):
        if count[i] > 0:
            res.extend([i] * count[i])
    return res