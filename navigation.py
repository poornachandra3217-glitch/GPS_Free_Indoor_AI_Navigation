import heapq

CAMPUS_GRAPH = {
    "entrance": {"corridor_a": 12, "admin": 18},
    "corridor_a": {"entrance": 12, "lab_1": 10, "library": 15},
    "admin": {"entrance": 18, "corridor_b": 14},
    "lab_1": {"corridor_a": 10, "corridor_b": 9},
    "corridor_b": {"admin": 14, "lab_1": 9, "library": 11, "block_b": 16},
    "library": {"corridor_a": 15, "corridor_b": 11, "block_b": 12},
    "block_b": {"corridor_b": 16, "library": 12}
}

def shortest_path(graph, start, goal):
    pq = [(0, start)]
    distance = {node: float("inf") for node in graph}
    previous = {}
    distance[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if cost != distance[node]:
            continue
        if node == goal:
            break
        for nxt, weight in graph[node].items():
            new_cost = cost + weight
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                previous[nxt] = node
                heapq.heappush(pq, (new_cost, nxt))

    if distance[goal] == float("inf"):
        return {"found": False, "path": [], "distance": None}

    path, current = [], goal
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return {
        "found": True,
        "path": path,
        "distance": distance[goal],
        "message": "Route found: " + " → ".join(path)
    }
