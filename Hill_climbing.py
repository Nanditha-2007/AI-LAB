def hill_climbing(graph, values, initial_state):
    current = initial_state

    while graph[current]:
        best_neighbour = current

        for neighbour in graph[current]:
            if values[neighbour] > values[best_neighbour]:
                best_neighbour = neighbour

        if best_neighbour == current:
            break

        current = best_neighbour

    print("Final state:", current)
    print("Value:", values[current])
    return current, values[current]


try:
    node_count = int(input("Enter the number of states: "))
    if node_count <= 0:
        raise ValueError("The number of states must be positive.")

    graph = {}
    values = {}

    print("For each state, enter: state value neighbor1 neighbor2 ...")
    print("Enter - when a state has no neighbours.")

    for _ in range(node_count):
        parts = input("State details: ").split()
        if len(parts) < 3:
            raise ValueError("Enter a state, its value, and at least '-' for neighbours.")

        state = parts[0]
        if state in graph:
            raise ValueError(f"Duplicate state: {state}")

        values[state] = float(parts[1])
        graph[state] = [] if parts[2] == "-" else parts[2:]

    for state, neighbours in graph.items():
        for neighbour in neighbours:
            if neighbour not in graph:
                raise ValueError(f"Unknown neighbour '{neighbour}' listed for state '{state}'.")

    start = input("Enter the initial state: ").strip()
    if start not in graph:
        raise ValueError(f"Unknown initial state: {start}")

    hill_climbing(graph, values, start)
except ValueError as error:
    print("Input error:", error)