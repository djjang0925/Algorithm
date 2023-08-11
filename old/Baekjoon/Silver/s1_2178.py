from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input()[:])))


def Bfs(graph, root, y, x):
    visited = []
    queue = deque([root])
    result = [[0]*x for _ in range(y)]
    # result[0][0] = 1

    while queue:
        n = queue.popleft()
        
        move_x = [0, 0, -1, 1]
        move_y = [-1, 1, 0, 0]

        if n not in visited:
            visited.append(n)

            for i in range(4):
                n_y = n[0] + move_y[i]
                n_x = n[1] + move_x[i]

                if y > n_y >= 0 and x > n_x >= 0:
                    if graph[n_y][n_x] == 1:
                        queue.append([n_y, n_x])
                        result[n_y][n_x] = result[n[0]][n[1]] + 1

    # return result[-1][-1]
    return result

# print(Bfs(maze, [0, 0], n, m))

res = Bfs(maze, [0, 0], n, m)

for i in range(len(res)):
    print(*res[i])