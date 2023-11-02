from collections import deque

with open('input.txt', "r") as file:
    N = int(file.readline())
    source = tuple(map(int, file.readline().split(',')))
    destination = tuple(map(int, file.readline().split(',')))

print(f"N = {N}, source = {source}, destination = {destination}")

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def find_min_moves(N, source, destination):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(source[0], source[1], 0, [(source[0], source[1])])])
    iteration = 0
    while queue:
        iteration += 1

        x, y, moves, path = queue.popleft()
        if (x, y) == destination:
            print(iteration)
            return moves, path

        for k in range(7):
            iteration += 1

            new_x = x + row[k]
            new_y = y + col[k]
            if is_valid(new_x, new_y, N) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1, path + [(new_x, new_y)]))


with open('output.txt', 'w') as file:
    moves, path = find_min_moves(N, source, destination)
    file.write(str(moves) + "\n")
    file.write(str(path))


def build_adjacency_list(N):
    adjacency_list = {}
    for x in range(N):
        for y in range(N):
            moves = []
            for k in range(8):
                new_x = x + row[k]
                new_y = y + col[k]
                if is_valid(new_x, new_y, N):
                    moves.append((new_x, new_y))
            adjacency_list[(x, y)] = moves
    return adjacency_list


def find_min_moves2(N, source, destination):
    adjacency_list = build_adjacency_list(N)
    print(adjacency_list)
    visited = [[False] * N for _ in range(N)]
    queue = deque([(source[0], source[1], 0, [(source[0], source[1])])])
    iterations = 0
    while queue:
        iterations += 1
        x, y, moves, path = queue.popleft()
        if (x, y) == destination:
            print(iterations)
            return moves, path

        for new_x, new_y in adjacency_list[(x, y)]:
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1, path + [(new_x, new_y)]))


with open('output2.txt', 'w') as file:
    moves, path = find_min_moves2(N, source, destination)
    file.write(str(moves) + "\n")
    file.write(str(path))
