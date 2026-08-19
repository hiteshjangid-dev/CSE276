#!/usr/bin/env python3
"""
Unit Tests for Practical 1 Route Planner
Verifies BFS and DFS algorithms, datasets, distances, and edge cases.
"""

import unittest
from datasets.india_roads import INDIA_ROADS, CITY_POSITIONS
from datasets.romania_roads import ROMANIA_ROADS, ROMANIA_POSITIONS
from route_planner import bfs, dfs, real_distance


class TestRoutePlanner(unittest.TestCase):

    def test_datasets_integrity(self):
        """Verify graph datasets are non-empty and have bidirectional symmetric edge distances."""
        self.assertEqual(len(INDIA_ROADS), 20)
        self.assertEqual(len(CITY_POSITIONS), 20)
        
        # Check symmetry in India roads
        for u, neighbors in INDIA_ROADS.items():
            for v, dist in neighbors.items():
                self.assertIn(v, INDIA_ROADS, f"City {v} missing from graph nodes")
                self.assertIn(u, INDIA_ROADS[v], f"Edge {u} -> {v} is not bidirectional")
                self.assertEqual(dist, INDIA_ROADS[v][u], f"Distance {u}-{v} is asymmetric")
                self.assertGreater(dist, 0, "Distance must be positive")

        # Check symmetry in Romania roads
        for u, neighbors in ROMANIA_ROADS.items():
            for v, dist in neighbors.items():
                self.assertIn(v, ROMANIA_ROADS, f"City {v} missing from Romania graph")
                self.assertIn(u, ROMANIA_ROADS[v], f"Romania edge {u} -> {v} not bidirectional")
                self.assertEqual(dist, ROMANIA_ROADS[v][u], f"Romania distance {u}-{v} asymmetric")

    def test_bfs_delhi_to_chennai(self):
        """Test BFS finds the optimal 6-hop route from Delhi to Chennai."""
        path, explored = bfs(INDIA_ROADS, "Delhi", "Chennai")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "Delhi")
        self.assertEqual(path[-1], "Chennai")
        self.assertEqual(len(path) - 1, 6) # Exactly 6 hops
        self.assertGreater(explored, 0)
        
        dist = real_distance(INDIA_ROADS, path)
        self.assertEqual(dist, 2133)

    def test_dfs_delhi_to_chennai(self):
        """Test DFS finds a valid path from Delhi to Chennai."""
        path, explored = dfs(INDIA_ROADS, "Delhi", "Chennai")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "Delhi")
        self.assertEqual(path[-1], "Chennai")
        self.assertGreater(explored, 0)
        
        dist = real_distance(INDIA_ROADS, path)
        self.assertEqual(dist, 3520)

    def test_start_equals_goal(self):
        """Test edge case when start city is already the goal city."""
        bfs_path, bfs_exp = bfs(INDIA_ROADS, "Delhi", "Delhi")
        self.assertEqual(bfs_path, ["Delhi"])
        self.assertEqual(bfs_exp, 1)

        dfs_path, dfs_exp = dfs(INDIA_ROADS, "Delhi", "Delhi")
        self.assertEqual(dfs_path, ["Delhi"])
        self.assertEqual(dfs_exp, 1)

    def test_multiple_city_pairs(self):
        """Test searches on various Indian city pairs."""
        pairs = [
            ("Mumbai", "Kolkata"),
            ("Delhi", "Bangalore"),
            ("Jaipur", "Chennai"),
            ("Ahmedabad", "Patna")
        ]
        for start, goal in pairs:
            bfs_path, _ = bfs(INDIA_ROADS, start, goal)
            dfs_path, _ = dfs(INDIA_ROADS, start, goal)
            self.assertIsNotNone(bfs_path, f"BFS failed for {start} -> {goal}")
            self.assertIsNotNone(dfs_path, f"DFS failed for {start} -> {goal}")
            self.assertEqual(bfs_path[0], start)
            self.assertEqual(bfs_path[-1], goal)
            self.assertEqual(dfs_path[0], start)
            self.assertEqual(dfs_path[-1], goal)
            
            # BFS must have <= hops than DFS
            self.assertLessEqual(len(bfs_path), len(dfs_path))


if __name__ == "__main__":
    unittest.main()
