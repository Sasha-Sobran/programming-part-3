from collections import deque


def is_gas_supply_possible(cities, storage, pipelines):
    graph = {node: [] for node in cities + storage}
    for pipe in pipelines:
        graph[pipe[0]].append(pipe[1])
    results = []
    count = 0
    for s in storage:
        count += 1
        unreachable_cities = set(cities)
        queue = deque([s])
        visited = set()

        while queue:
            current_node = queue.popleft()
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in storage:
                    count += 1
                    queue.append(neighbor)
                    unreachable_cities.discard(neighbor)

        if unreachable_cities:
            results.append([s, list(unreachable_cities)])
    print(count)
    return results


def write_to_file(result):
    with open("output.txt", "w", encoding="UTF-8") as file:
        if not result:
            file.write("[]")
        else:
            for res in result:
                file.write(f"{res[0]}: ")
                for str in res[1]:
                    file.write(f"\n\t{str}")
                file.write("\n\n ")


def read_from_file(file):
    with open(file, "r", encoding="UTF-8") as file:
        cities = list(map(str, file.readline().strip().split(",")))
        storage = list(map(str, file.readline().strip().split(",")))
        pipelines = [line.strip().split(",") for line in file.readlines()]
        return cities, storage, pipelines


if __name__ == "__main__":
    cities, storage, pipelines = read_from_file("input.txt")

    print("\nresult: \n")

    result = is_gas_supply_possible(cities, storage, pipelines)
    write_to_file(result)
    print(result)
