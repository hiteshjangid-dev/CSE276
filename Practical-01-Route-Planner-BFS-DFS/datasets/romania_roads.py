"""
Classic Romania Road Network (AIMA Textbook Dataset)
20 Cities with straight-line heuristics and actual road distances in kilometers.
"""

ROMANIA_ROADS = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

ROMANIA_POSITIONS = {
    "Arad": (91, 492), "Zerind": (108, 531), "Oradea": (131, 571), "Sibiu": (207, 457),
    "Timisoara": (94, 410), "Lugoj": (165, 379), "Mehadia": (168, 339), "Drobeta": (165, 298),
    "Craiova": (253, 288), "Rimnicu Vilcea": (233, 410), "Fagaras": (305, 449),
    "Pitesti": (320, 368), "Bucharest": (400, 327), "Giurgiu": (375, 270),
    "Urziceni": (456, 350), "Hirsova": (534, 350), "Eforie": (562, 293),
    "Vaslui": (509, 444), "Iasi": (473, 506), "Neamt": (406, 537)
}
