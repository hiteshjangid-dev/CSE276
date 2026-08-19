#!/usr/bin/env python3
"""
CSE276: ARTIFICIAL INTELLIGENCE FOUNDATIONS
Practical 1: Intelligent Route Planner using BFS and DFS
Real Indian Road Network (20 Cities, 24 Highways)
"""

import os
import sys
import time
from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

# Dynamic path resolution to run cleanly from ANY working directory
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR / "datasets"))
sys.path.insert(0, str(CURRENT_DIR.parent / "datasets"))

try:
    from india_roads import INDIA_ROADS, CITY_POSITIONS
except ImportError:
    # Embedded fallback for single-file copy-paste environments
    INDIA_ROADS = {
        "Delhi": {"Jaipur": 280, "Agra": 233, "Kanpur": 440},
        "Jaipur": {"Delhi": 280, "Ahmedabad": 660},
        "Agra": {"Delhi": 233, "Gwalior": 120, "Kanpur": 280},
        "Gwalior": {"Agra": 120, "Bhopal": 420},
        "Kanpur": {"Delhi": 440, "Agra": 280, "Lucknow": 80, "Varanasi": 320},
        "Lucknow": {"Kanpur": 80, "Varanasi": 300},
        "Varanasi": {"Kanpur": 320, "Lucknow": 300, "Patna": 250},
        "Patna": {"Varanasi": 250, "Kolkata": 580},
        "Kolkata": {"Patna": 580, "Raipur": 640},
        "Bhopal": {"Gwalior": 420, "Indore": 190, "Nagpur": 350},
        "Indore": {"Bhopal": 190, "Ahmedabad": 390, "Mumbai": 580},
        "Ahmedabad": {"Jaipur": 660, "Indore": 390, "Surat": 260},
        "Surat": {"Ahmedabad": 260, "Mumbai": 280},
        "Mumbai": {"Surat": 280, "Indore": 580, "Pune": 150},
        "Pune": {"Mumbai": 150, "Hyderabad": 560, "Bangalore": 840},
        "Nagpur": {"Bhopal": 350, "Raipur": 280, "Hyderabad": 500},
        "Raipur": {"Kolkata": 640, "Nagpur": 280},
        "Hyderabad": {"Nagpur": 500, "Pune": 560, "Bangalore": 570, "Chennai": 510},
        "Bangalore": {"Hyderabad": 570, "Pune": 840, "Chennai": 350},
        "Chennai": {"Hyderabad": 510, "Bangalore": 350}
    }
    CITY_POSITIONS = {
        "Delhi": (77.10, 28.70), "Jaipur": (75.78, 26.91), "Agra": (78.00, 27.17),
        "Gwalior": (78.18, 26.21), "Kanpur": (80.33, 26.44), "Lucknow": (80.94, 26.84),
        "Varanasi": (82.97, 25.31), "Patna": (85.13, 25.59), "Kolkata": (88.36, 22.57),
        "Bhopal": (77.41, 23.25), "Indore": (75.85, 22.71), "Ahmedabad": (72.57, 23.02),
        "Surat": (72.83, 21.17), "Mumbai": (72.87, 19.07), "Pune": (73.85, 18.52),
        "Nagpur": (79.08, 21.14), "Raipur": (81.62, 21.25), "Hyderabad": (78.48, 17.38),
        "Bangalore": (77.59, 12.97), "Chennai": (80.27, 13.08)
    }

# Create output images folder relative to script location
IMAGES_DIR = CURRENT_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def bfs(graph, start, goal):
    """
    Breadth First Search (BFS): explores level by level using a FIFO Queue.
    Guarantees finding the path with the fewest road segments (hops).
    """
    if start not in graph or goal not in graph:
        return None, 0

    visited = {start}
    queue = deque([[start]])
    explored = 0

    while queue:
        path = queue.popleft()
        city = path[-1]
        explored += 1

        if city == goal:
            return path, explored

        for neighbour in graph.get(city, {}):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None, explored


def dfs(graph, start, goal):
    """
    Depth First Search (DFS): dives deep along one road using a LIFO Stack.
    Finds a valid path using small memory, but does not guarantee the shortest route.
    """
    if start not in graph or goal not in graph:
        return None, 0

    visited = {start}
    stack = [[start]]
    explored = 0

    while stack:
        path = stack.pop()
        city = path[-1]
        explored += 1

        if city == goal:
            return path, explored

        for neighbour in graph.get(city, {}):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(path + [neighbour])

    return None, explored


def real_distance(graph, path):
    """Add up real road kilometers along a found path."""
    if not path or len(path) < 2:
        return 0
    return sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))


def draw_path(graph, positions, path, title, filename, color):
    """Draws the complete graph and highlights the searched path."""
    if not path:
        return

    G = nx.Graph()
    for city, neighbours in graph.items():
        for neighbour, dist in neighbours.items():
            G.add_edge(city, neighbour, weight=dist)

    plt.figure(figsize=(10, 9), facecolor="#FFFFFF")
    nx.draw_networkx_edges(G, positions, edge_color="#d1d5db", width=1.2)
    nx.draw_networkx_nodes(G, positions, node_color="#e5e7eb", node_size=750)
    nx.draw_networkx_labels(G, positions, font_size=8, font_weight="bold", font_color="#1F2937")

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, positions, edgelist=path_edges, edge_color=color, width=3.5)
    nx.draw_networkx_nodes(G, positions, nodelist=path, node_color=color, node_size=800, alpha=0.5)
    nx.draw_networkx_nodes(G, positions, nodelist=[path[0]], node_color="#16a34a", node_size=850)
    nx.draw_networkx_nodes(G, positions, nodelist=[path[-1]], node_color="#dc2626", node_size=850)

    plt.title(title, fontsize=12, fontweight="bold", pad=15)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    start_city, goal_city = "Delhi", "Chennai"
    print(f"Real road network: {len(INDIA_ROADS)} real Indian cities")
    print(f"Route requested: {start_city} -> {goal_city} (disaster response scenario)\n")

    t0 = time.perf_counter()
    bfs_path, bfs_explored = bfs(INDIA_ROADS, start_city, goal_city)
    bfs_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    dfs_path, dfs_explored = dfs(INDIA_ROADS, start_city, goal_city)
    dfs_time = time.perf_counter() - t0

    bfs_km = real_distance(INDIA_ROADS, bfs_path)
    dfs_km = real_distance(INDIA_ROADS, dfs_path)

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

    draw_path(INDIA_ROADS, CITY_POSITIONS, bfs_path,
              f"BFS Route: {start_city} to {goal_city} ({bfs_km} km, {bfs_explored} explored)",
              str(IMAGES_DIR / "01_bfs_route.png"), "#2563eb")
    draw_path(INDIA_ROADS, CITY_POSITIONS, dfs_path,
              f"DFS Route: {start_city} to {goal_city} ({dfs_km} km, {dfs_explored} explored)",
              str(IMAGES_DIR / "02_dfs_route.png"), "#f97316")

    print("\nDone. Charts saved in images/")
