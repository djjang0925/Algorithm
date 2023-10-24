def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(graph[root][0])
        preorder(graph[root][1])


def inorder(root):
    if root != '.':
        inorder(graph[root][0])
        print(root, end='')
        inorder(graph[root][1])


def postorder(root):
    if root != '.':
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root, end='')


n = int(input())
graph = {chr(i): [] for i in range(65, 65 + n)}

for i in range(n):
    a, b, c = input().split()
    graph[a] = (b, c)

preorder('A')
print('')
inorder('A')
print('')
postorder('A')