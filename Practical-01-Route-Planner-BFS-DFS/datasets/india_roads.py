"""
Real Indian Road Network Dataset
20 Real Indian Cities connected by National Highways with approximate road distances in kilometers.
Used for AI Search Practicals (BFS, DFS, Uniform Cost Search, A* Search).
"""

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

# 2D Approximate geographical coordinates (Longitude, Latitude for plotting on India map)
CITY_POSITIONS = {
    "Delhi": (77.10, 28.70),
    "Jaipur": (75.78, 26.91),
    "Agra": (78.00, 27.17),
    "Gwalior": (78.18, 26.21),
    "Kanpur": (80.33, 26.44),
    "Lucknow": (80.94, 26.84),
    "Varanasi": (82.97, 25.31),
    "Patna": (85.13, 25.59),
    "Kolkata": (88.36, 22.57),
    "Bhopal": (77.41, 23.25),
    "Indore": (75.85, 22.71),
    "Ahmedabad": (72.57, 23.02),
    "Surat": (72.83, 21.17),
    "Mumbai": (72.87, 19.07),
    "Pune": (73.85, 18.52),
    "Nagpur": (79.08, 21.14),
    "Raipur": (81.62, 21.25),
    "Hyderabad": (78.48, 17.38),
    "Bangalore": (77.59, 12.97),
    "Chennai": (80.27, 13.08)
}
