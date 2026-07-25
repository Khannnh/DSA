# Hàm đệ quy tìm Postorder từ Inorder và Preorder
def get_post_order(inorder, preorder):
    # Dừng đệ quy nếu mảng rỗng
    if not inorder:
        return []

    # 1. Phần tử đầu tiên của Preorder luôn là Gốc
    root = preorder[0]

    # 2. Tìm vị trí của Gốc trong mảng Inorder
    root_idx = inorder.index(root)

    # 3. Chia mảng Inorder thành 2 phần:
    # - Bên trái root_idx là cây con Trái
    # - Bên phải root_idx là cây con Phải
    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx + 1:]

    # Kích thước cây con Trái giúp cắt đúng phần tương ứng trong Preorder
    left_size = len(left_inorder)
    left_preorder = preorder[1 : 1 + left_size]
    right_preorder = preorder[1 + left_size :]

    # 4. Đệ quy Postorder = Trái + Phải + Gốc
    left_postorder = get_post_order(left_inorder, left_preorder)
    right_postorder = get_post_order(right_inorder, right_preorder)

    return left_postorder + right_postorder + [root]


# --- Nhập / Xuất dữ liệu cơ bản ---
T = int(input())

for _ in range(T):
    N = int(input())
    inorder = list(map(int, input().split()))
    preorder = list(map(int, input().split()))
    # Gọi hàm và nhận mảng kết quả
    postorder = get_post_order(inorder, preorder)
    # In kết quả cách nhau bởi khoảng trắng
    print(*postorder)