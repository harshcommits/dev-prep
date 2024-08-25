def dfs(graph, source):
    stack = []
    visited = set() # set to mark visited values

    stack.append(source)

    while stack:
        current = stack.pop()
        print(current)
        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)

    return f"visited:{visited}"


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print(dfs(graph, 'F'))