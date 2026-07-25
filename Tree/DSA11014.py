#cái bài này vẫn ko ac nổi luôn 🥲
class Node:
    def __init__(self, val):
        self.val = int(val)
        self.left = None
        self.right = None

t = int(input())

for _ in range(t):
    n = int(input())
    data = input().split()

    nodes = {}
    child = set()

    for i in range(0, len(data), 3):
        u, v, c = data[i], data[i + 1], data[i + 2]

        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)

        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]

        child.add(v)

    root = None
    for x in nodes:
        if x not in child:
            root = nodes[x]
            break

    ans = 0
    stack = [root]

    while stack:
        node = stack.pop()

        if node is None:
            continue

        if (node.right is not None and
            node.right.left is None and
            node.right.right is None):
            ans += node.right.val

        stack.append(node.left)
        stack.append(node.right)

    print(ans)