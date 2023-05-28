from collections import deque


def bfs_1(graph, start, target):
    # Создаем очередь для поиска в ширину и добавляем стартовую вершину
    queue = deque([start])
    # Создаем словарь для хранения расстояний от стартовой вершины и количество пройденных вершин
    distance = {start: 0}
    visited = set([start])
    length = 0
    path = []

    while queue:
        # Извлекаем вершину из очереди
        vertex = queue.popleft()
        visited.add(vertex)
        path.append(vertex)
        # Обрабатываем вершину
        if vertex == target:
            return (path, distance[vertex], len(visited))  # Возвращаем дистанцию и количество пройденных вершин
        # Добавляем в очередь все соседние (непосещенные) вершины и обновляем расстояние
        for neighbor, weight in graph[vertex].items():
            print(distance)
            if neighbor not in distance:
                queue.append(neighbor)
                distance[neighbor] = distance[vertex] + weight

    return None


def breadth_first_search(graph, start, target):
    visited = [start]  # множество для хранения посещенных вершин
    queue = deque([(start, [start], 0)])  # очередь с кортежем (вершина, путь, вес)
    layer, prev_layer = 0, None
    arr_dist = []
    path_all = []
    sum_res = 0
    str_path = ''
    while queue:
        vertex, path, distance = queue.popleft()

        arr_dist.append(distance)
        str_path = str_path + f'{path[-2:]} {sum(arr_dist)} ; '
        if prev_layer is not None and prev_layer != layer:
            sum_res += sum(arr_dist)
            arr_dist = []
            path_all.extend(path[-2:])

        if vertex == target:
            return str_path, sum_res, len(sorted(list(set(path_all))))
        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append((neighbor, path + [neighbor], weight))
        layer, prev_layer = layer + 1, layer
    return None, None

if __name__ == "__main__":
    graph = {
        '1': {'2': 5, '3': 7},
        '2': {'1': 5, '3': 9, '4': 15},
        '3': {'1': 7, '2': 9, '4': 10, '5': 4, '6': 9},
        '4': {'2': 15, '3': 10, '6': 9, '5': 7},
        '5': {'4': 7, '3': 4, '6': 8},
        '6': {'3': 9, '4': 9, '5': 8}
    }

    start_node = '1'
    end_node = '6'

    result = breadth_first_search(graph, start_node, end_node)
    print(result)
    if result:
        path, distance, visited = result
        print(f"Путь: {path}")
        print("Длина пути (L): ", distance)
        print("Количество посещенных вершин (K): ", visited)
    else:
        print("Целевая вершина не найдена.")
