def dfs(graph, start, end, path, visited):
    path.append(start)       # Добавляем текущую вершину в путь
    visited.add(start)        # Отмечаем вершину как посещенную

    # Если мы достигли конечной вершины, возвращаем True
    if start == end:
        return True

    # Проходим по всем соседним вершинам текущей вершины
    for neighbor in graph[start]:
        if neighbor not in visited:  # Если соседняя вершина не посещена
            if dfs(graph, neighbor, end, path, visited):  # Рекурсивно вызываем dfs для соседа
                return True  # Если путь найден, возвращаемся

    # Если все соседи уже проверены и путь не найден, удаляем вершину из пути
    path.pop()
    return False

def find_path(graph, start, end):
    path = []            # Список для хранения пути
    visited = set()      # Множество для отслеживания посещенных вершин

    if dfs(graph, start, end, path, visited):
        return path
    else:
        return "Путь не существует"

# Пример графа
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [],
    6: []
}

# Стартовая и конечная вершины
start = 1
end = 6

# Поиск пути
path = find_path(graph, start, end)
print("Путь:", path)
