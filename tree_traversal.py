class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')  # 자기자신 처리
    if node.left_node != None:  # 왼쪽 방문
        pre_order(tree[node.left_node])
    if node.right_node != None:  # 오른쪽 방문
        pre_order(tree[node.right_node])


# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])


# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')


n = int(input()) # 사이즈 입력
tree = {}

for i in range(n):
    data, left_node, right_node = input().split() # 부모노드 자식노드(왼쪽) 자식노드(오른쪽)
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print() # 전위 순회 결과 출력
in_order(tree['A'])
print() # 중위 순회 결과 출력
post_order(tree['A'])
print() # 후위 순회 결과 출력