from collections import deque


def is_gas_supply_possible(cities, storage, pipelines):
    graph = {node: [] for node in cities + storage}
    for pipe in pipelines:
        graph[pipe[0]].append(pipe[1])
    results = []
    for s in storage:
        unreachable_cities = set(cities)
        queue = deque([s])
        visited = set()

        while queue:
            current_node = queue.popleft()
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    unreachable_cities.discard(neighbor)

        if unreachable_cities:
            results.append([s, list(unreachable_cities)])
    return results


if __name__ == '__main__':
    cities = ['Львів', 'Стрий', 'Долина']
    storage = ['Сховище_1', 'Сховище_2']
    pipelines = [['Львів', 'Стрий'], ['Львів', 'Долина'], ['Львів', 'Сховище_2']]

    result = is_gas_supply_possible(cities, storage, pipelines)
    print(result)
    for res in result:
        print(res)
