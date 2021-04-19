import collections

# funcion en donde vamos a agregar el grafo y la raiz
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        elemento = queue.popleft()
        print(str(elemento) + " ", end="")

        # si no esta visitada entonces la agregamos a la cola
        for neighbour in graph[elemento]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)



graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("Lo que sigue es el Ancho ")
bfs(graph, 0)


