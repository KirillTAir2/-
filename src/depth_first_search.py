def depth_first_search(graph, start_node, end_node):
    visited = set()  # множество посещенных вершин
    stack = [(start_node, 0, [])]  # стэк с текущей вершиной, длиной пути до нее и путем
    path_len = 0  # длина пройденного пути
    path_nodes = []  # список пройденных вершин

    while len(stack) > 0:
        node, length, path = stack.pop()  # извлекаем вершину, ее длину и текущий путь из стека

        if node == end_node:  # если достигли целевой вершины
            path_len = length  # сохраняем длину пути до нее
            path_nodes = path + [node]  # сохраняем путь до нее
            return (path_nodes, path_len, len(path_nodes))

        if node not in visited:  # если вершина еще не посещена
            visited.add(node)  # добавляем ее в множество посещенных
            for neighbor, weight in graph[node].items():  # перебираем соседние вершины
                if neighbor not in visited:  # если соседняя вершина еще не посещена
                    stack.append(
                        (neighbor, length + weight, path + [node]))  # добавляем ее в стек с учетом длины пути и пути

    return None


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

    result = depth_first_search(graph, start_node, end_node)
    if result:
        path_nodes, path_len, node_count = result
        print(f"Путь: {' -> '.join(path_nodes)}")
        print('Длина пути (L):', path_len)
        print('Количество посещенных вершин (K):', node_count)
    else:
        print("Целевая вершина не найдна.")
