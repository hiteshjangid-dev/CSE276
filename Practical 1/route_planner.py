"""
Practical 1 - Find a route between two real cities using BFS and DFS,
then compare them honestly: path quality, states explored, and time taken.
Data: real Romania road network (Russell & Norvig AIMA textbook, Fig 3.2)
Run: python route_planner.py
"""
import os
import sys
import time
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

sys.path.insert(0, "../datasets")
from romania_roads import ROMANIA_ROADS, CITY_POSITIONS

os.makedirs("images", exist_ok=True)


def bfs(graph, start, goal):
    """Breadth First Search: explore level by level. Guarantees the FEWEST
    number of roads (hops), not necessarily the shortest real distance."""
    visited = {start}
    queue = deque([[start]])
    explored = 0
    while queue:
        path = queue.popleft()
        city = path[-1]
        explored += 1
        if city == goal:
            return path, explored
        for neighbour in graph[city]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])
    return None, explored


def dfs(graph, start, goal):
    """Depth First Search: explore as deep as possible before backtracking.
    Finds A path, with no guarantee it is short in hops or in real distance."""
    visited = {start}
    stack = [[start]]
    explored = 0
    while stack:
        path = stack.pop()
        city = path[-1]
        explored += 1
        if city == goal:
            return path, explored
        for neighbour in graph[city]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(path + [neighbour])
    return None, explored


def real_distance(graph, path):
    """Add up the real road kilometers along a found path."""
    return sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))


def draw_path(graph, positions, path, title, filename, color):
    G = nx.Graph()
    for city, neighbours in graph.items():
        for neighbour, dist in neighbours.items():
            G.add_edge(city, neighbour, weight=dist)

    plt.figure(figsize=(11, 7))
    nx.draw_networkx_edges(G, positions, edge_color="#d1d5db", width=1.2)
    nx.draw_networkx_nodes(G, positions, node_color="#e5e7eb", node_size=700)
    nx.draw_networkx_labels(G, positions, font_size=8)

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, positions, edgelist=path_edges, edge_color=color, width=3)
    nx.draw_networkx_nodes(G, positions, nodelist=path, node_color=color, node_size=750, alpha=0.5)
    nx.draw_networkx_nodes(G, positions, nodelist=[path[0]], node_color="#16a34a", node_size=800)
    nx.draw_networkx_nodes(G, positions, nodelist=[path[-1]], node_color="#dc2626", node_size=800)

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    start_city, goal_city = "Arad", "Bucharest"
    print(f"Real road network: {len(ROMANIA_ROADS)} real Romanian cities")
    print(f"Route requested: {start_city} -> {goal_city} (emergency response scenario)\n")

    t0 = time.perf_counter()
    bfs_path, bfs_explored = bfs(ROMANIA_ROADS, start_city, goal_city)
    bfs_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    dfs_path, dfs_explored = dfs(ROMANIA_ROADS, start_city, goal_city)
    dfs_time = time.perf_counter() - t0

    bfs_km = real_distance(ROMANIA_ROADS, bfs_path)
    dfs_km = real_distance(ROMANIA_ROADS, dfs_path)

    print("BFS path: ", " -> ".join(bfs_path))
    print("BFS hops:", len(bfs_path) - 1, "| real distance:", bfs_km, "km",
          "| cities explored:", bfs_explored, "| time:", f"{bfs_time*1000:.3f} ms")

    print("\nDFS path: ", " -> ".join(dfs_path))
    print("DFS hops:", len(dfs_path) - 1, "| real distance:", dfs_km, "km",
          "| cities explored:", dfs_explored, "| time:", f"{dfs_time*1000:.3f} ms")

    print(f"\nBFS found a route with {bfs_km} real km using {bfs_explored} explored cities.")
    print(f"DFS found a route with {dfs_km} real km using {dfs_explored} explored cities.")
    if bfs_km < dfs_km:
        print("BFS found the shorter real route here.")
    elif dfs_km < bfs_km:
        print("DFS found the shorter real route here.")
    else:
        print("Both found equally short real routes here.")

    draw_path(ROMANIA_ROADS, CITY_POSITIONS, bfs_path,
              f"BFS Route: {start_city} to {goal_city} ({bfs_km} km, {bfs_explored} explored)",
              "images/01_bfs_route.png", "#2563eb")
    draw_path(ROMANIA_ROADS, CITY_POSITIONS, dfs_path,
              f"DFS Route: {start_city} to {goal_city} ({dfs_km} km, {dfs_explored} explored)",
              "images/02_dfs_route.png", "#f97316")

    print("\nDone. Charts saved in images/")
