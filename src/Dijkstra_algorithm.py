def Dijkstra_algorithm(graph, start, end):
    """
    Реализация алгоритма Дейкстры для поиска кратчайшего пути до указанной целевой вершины в взвешенном графе
    """

    # Инициализация начальных значений
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0
    visited = set()
    path = {}

    while len(visited) != len(graph):
        # Найти не посещенную вершину с минимальным расстоянием
        current_vertex = min(set(dist.keys()) - visited, key=dist.get)
        visited.add(current_vertex)

        # Проверить расстояния до смежных вершин и обновить их если необходимо
        for neighbour, weight in graph[current_vertex].items():
            new_distance = dist[current_vertex] + weight
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                path[neighbour] = current_vertex  # обновляем путь до вершины

    # Восстановить кратчайший путь до целевой вершины
    shortest_path = [end]
    vertex = end
    while vertex != start:
        vertex = path[vertex]
        shortest_path.append(vertex)
    shortest_path.reverse()

    return (shortest_path, dist[end], len(shortest_path))

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

    path, distance, len_distance = Dijkstra_algorithm(graph, start_node, end_node)

    print(f"Кратчайший путь: {' -> '.join(path)}")
    print(f"Кратчайшее расстояние от вершины {start_node} до {end_node} (L): {distance}")
    print('Количество пройденных вершин (K):', len_distance)