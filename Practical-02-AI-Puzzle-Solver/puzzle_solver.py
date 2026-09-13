import heapq
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
START = (1, 5, 2, 4, 3, 0, 7, 8, 6)


def get_neighbors(state):
    blank = state.index(0)
    row, column = divmod(blank, 3)
    neighbors = []

    for row_change, column_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = row + row_change
        new_column = column + column_change

        if 0 <= new_row < 3 and 0 <= new_column < 3:
            new_blank = new_row * 3 + new_column
            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            neighbors.append(tuple(new_state))

    return neighbors


def manhattan_distance(state):
    distance = 0
    for position, tile in enumerate(state):
        if tile != 0:
            goal_position = tile - 1
            distance += abs(position // 3 - goal_position // 3)
            distance += abs(position % 3 - goal_position % 3)
    return distance


def hill_climbing(start):
    current_state = start
    path = [current_state]

    while current_state != GOAL:
        best_state = min(get_neighbors(current_state), key=manhattan_distance)

        if manhattan_distance(best_state) >= manhattan_distance(current_state):
            return path, False

        current_state = best_state
        path.append(current_state)

    return path, True


def a_star(start):
    priority_queue = [(manhattan_distance(start), 0, start, [start])]
    best_cost = {start: 0}
    explored = 0

    while priority_queue:
        total_cost, path_cost, current_state, path = heapq.heappop(priority_queue)
        explored += 1

        if current_state == GOAL:
            return path, explored

        if path_cost != best_cost[current_state]:
            continue

        for neighbor_state in get_neighbors(current_state):
            new_path_cost = path_cost + 1

            if new_path_cost < best_cost.get(neighbor_state, float("inf")):
                best_cost[neighbor_state] = new_path_cost
                heuristic_cost = manhattan_distance(neighbor_state)
                new_total_cost = new_path_cost + heuristic_cost

                heapq.heappush(
                    priority_queue,
                    (new_total_cost, new_path_cost, neighbor_state, path + [neighbor_state])
                )

    return None, explored


def breadth_first_search(start):
    queue = deque([(start, [start])])
    visited = {start}
    explored = 0

    while queue:
        current_state, path = queue.popleft()
        explored += 1

        if current_state == GOAL:
            return path, explored

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state not in visited:
                visited.add(neighbor_state)
                queue.append((neighbor_state, path + [neighbor_state]))

    return None, explored


print("Starting State:", START)
print("h(n) =", manhattan_distance(START))

hill_path, hill_solved = hill_climbing(START)
astar_path, astar_explored = a_star(START)
bfs_path, bfs_explored = breadth_first_search(START)

print("\nHill Climbing")
print("Solved:", hill_solved)
print("Steps:", len(hill_path) - 1)

print("\nA* Search")
print("Solved:", astar_path is not None)
print("Steps:", len(astar_path) - 1)
print("States explored:", astar_explored)

print("\nBFS (Uninformed Search)")
print("Solved:", bfs_path is not None)
print("Steps:", len(bfs_path) - 1)
print("States explored:", bfs_explored)
