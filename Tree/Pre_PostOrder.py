#cây nhị phân tìm kiếm nên inorder(giữa) luôn là dãy tăng dần 
def bst_to_postorder(preorder:list):
    #basecase
    if not preorder:
        return []
        #trả về mảng rỗng cho đồng bộ 
    root = preorder[0]
    left_root , right_root = [] ,[]
    for x in preorder[1:]: #chạy bỏ root ở đầu
        if x< root:
            left_root.append(x)
        else:
            right_root.append(x)
    #cần tìm postorder(sau): trái + phải + root 
    return (bst_to_postorder(left_root) + bst_to_postorder(right_root)+[root] )
    #phép cộng list , ép root vào list :))
t=int(input())
for _ in range(t): 
    n=int(input())
    preorder = list(map(int , input().split()))
    print(*bst_to_postorder(preorder))

    