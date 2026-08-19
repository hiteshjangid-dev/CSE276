"""
Real road-network data: Romania map, Russell & Norvig "Artificial Intelligence:
A Modern Approach" (the official textbook for this course), Figure 3.2.
Distances are real published road distances in kilometers between real Romanian
cities, used worldwide as the standard search-algorithm teaching example.
"""

ROMANIA_ROADS = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "RimnicuVilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "RimnicuVilcea": 146, "Pitesti": 138},
    "RimnicuVilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"RimnicuVilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
}

# Approximate real (longitude, latitude)-style map layout, used only for drawing
# the graph in roughly the same shape as the real map (not used in any search math).
CITY_POSITIONS = {
    "Arad": (0, 4), "Zerind": (1, 5.5), "Oradea": (2, 6.5), "Sibiu": (2.5, 3.5),
    "Timisoara": (0.5, 1.5), "Lugoj": (2, 1), "Mehadia": (2.5, -0.2), "Drobeta": (2.3, -1.5),
    "Craiova": (4, -1.5), "RimnicuVilcea": (4, 2.5), "Fagaras": (5, 4),
    "Pitesti": (5.5, 1), "Bucharest": (7, 0), "Giurgiu": (7, -1.5),
    "Urziceni": (8.5, 1), "Hirsova": (10, 1), "Eforie": (10.5, -0.3),
    "Vaslui": (9, 3), "Iasi": (9, 5), "Neamt": (8, 6.2),
}
