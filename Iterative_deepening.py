
def dls(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return None

    for child in graph.get(node, []):
        if child not in path:
            result = dls(child, goal, graph, limit - 1, path + [node])

            if result is not None:
                return result

    return None


def ids(initial, goal, graph, max_depth):
    for depth in range(max_depth + 1):
        result = dls(initial, goal, graph, depth, [])

        if result is not None:
            print("Solution Path:", " -> ".join(result))
            print("Depth:", len(result) - 1)
            return

    print("Goal not found within maximum depth")


# Input
initial = input("Initial State: ")
goal = input("Goal State: ")
max_depth = int(input("Maximum Depth: "))

n = int(input("Number of nodes: "))
graph = {}

print("Enter each node and its children (use - if none):")

for i in range(n):
    line = input().split(":")
    node = line[0].strip()
    children = line[1].strip()

    if children == "-":
        graph[node] = []
    else:
        graph[node] = children.split()

ids(initial, goal, graph, max_depth)
