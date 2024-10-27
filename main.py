# Ввод данных о графе от пользователя
n = int(input("Введите количество вершин графа: "))
m = int(input("Введите количество рёбер графа: "))

# Инициализация списка смежности
V = [[] for _ in range(n + 1)]

print("Введите рёбра в формате 'u v', где u и v — соединённые вершины:")
for _ in range(m):
    u, v = map(int, input().split())
    V[u].append(v)
    V[v].append(u)  # Для неориентированного графа

# Ввод стартовой вершины
start = int(input("Введите стартовую вершину: "))

# Поиск кратчайшего пути методом поиска в ширину
D = [None] * (n + 1)
D[start] = 0
Q = [start]
Qstart = 0

while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1
    for v in V[u]:
        if D[v] is None:
            D[v] = D[u] + 1
            Q.append(v)

# Вывод расстояний до каждой вершины
print("Минимальные расстояния от вершины", start, ":")
for i in range(1, n + 1):
    if D[i] is not None:
        print(f"До вершины {i}: {D[i]} шагов")
    else:
        print(f"До вершины {i}: недостижима")

