def gradual_depth_first_search(graph, start, end):
    visited = set()  # создаем пустое множество для отслеживания посещенных вершин
    stack = [(start, 0, [start])]  # создаем стек для хранения вершин, которые нужно посетить
    # каждый элемент стека будет представлять собой кортеж (вершина, длина пути до вершины, список вершин на пути)
    while stack:
        stack.sort(reverse=True, key=lambda x: x[0])  # сортируем стек в порядке возрастания длин пути
        vertex, length, path = stack.pop()  # извлекаем вершину, длину пути до нее и список посещенных вершин из стека
        if vertex == end:  # если мы достигли целевой вершины, то возвращаем длину пути, количество вершин на пути и сам путь
            visited.add(vertex)
            return (path, length, len(visited))
        if vertex not in visited:  # если вершина еще не посещена, то добавляем ее в множество посещенных
            visited.add(vertex)
            for neighbor, weight in sorted(graph.get(vertex, {}).items()):  # итерируемся по соседям текущей вершины, сортируя их по номерам в порядке возрастания
                stack.append((neighbor, length+weight, path+[neighbor]))  # добавляем соседа в стек с новой длиной пути и списком вершин на пути
    return None, 0, []  # если целевая вершина не найдена, то возвращаем None, 0 и пустой список вершин на пути

if __name__ == "__main__":
    graph = {
        '1': {'2': 5, '3': 3, '4': 6, '5': 9},
        '2': {'1': 5, '3': 4},
        '3': {'1': 3, '2': 4, '5': 6, '6': 7, '4': 3},
        '4': {'1': 6, '3': 3, '6': 9},
        '5': {'1': 9, '3': 6, '6': 5},
        '6': {'4': 9, '3': 7, '5': 5}
    }

    start_node = '1'
    end_node = '6'

    path, length, num_vertices = gradual_depth_first_search(graph, start_node, end_node)

    print(f"Путь: {' -> '.join(path)}")
    print("Длина пути:", length)
    print("Количество посещенных вершин (K):", num_vertices)