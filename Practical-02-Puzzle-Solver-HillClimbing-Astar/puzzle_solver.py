"""
Practical 2 - Solve the classic 8-puzzle using Hill Climbing and A* Search.
Run: python puzzle_solver.py
"""
import heapq
import random
import time

import matplotlib.pyplot as plt

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 = blank tile


def neighbours(state):
    """All boards reachable by sliding one tile into the blank."""
    blank = state.index(0)
    row, col = divmod(blank, 3)
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            swap = r * 3 + c
            new_state = list(state)
            new_state[blank], new_state[swap] = new_state[swap], new_state[blank]
            moves.append(tuple(new_state))
    return moves


def h(state):
    """Manhattan distance: how many rows+cols every tile is from home."""
    total = 0
    for i, tile in enumerate(state):
        if tile:
            gi = GOAL.index(tile)
            total += abs(i // 3 - gi // 3) + abs(i % 3 - gi % 3)
    return total


def hill_climbing(start, max_sideways=20):
    """Always move to the best neighbour. Can get stuck (real weakness)."""
    path, sideways = [start], 0
    while path[-1] != GOAL:
        current = path[-1]
        best = min(neighbours(current), key=h)
        if h(best) < h(current):
            sideways = 0
        elif h(best) == h(current) and sideways < max_sideways:
            sideways += 1
        else:
            return path, False  # stuck at a local minimum
        path.append(best)
        if len(path) > 500:
            return path, False
    return path, True


def a_star(start):
    """f(n) = g(n) + h(n). Guarantees the shortest solution."""
    counter = 0
    frontier = [(h(start), 0, counter, start, [start])]
    best_cost = {start: 0}
    explored = 0
    while frontier:
        f, g, _, state, path = heapq.heappop(frontier)
        explored += 1
        if state == GOAL:
            return path, explored
        for nxt in neighbours(state):
            new_g = g + 1
            if nxt not in best_cost or new_g < best_cost[nxt]:
                best_cost[nxt] = new_g
                counter += 1
                heapq.heappush(frontier, (new_g + h(nxt), new_g, counter, nxt, path + [nxt]))
    return None, explored


def scramble(seed, moves=12):
    rng = random.Random(seed)
    state = GOAL
    for _ in range(moves):
        state = rng.choice(neighbours(state))
    return state


def draw_board(state, ax, title):
    ax.set(xlim=(0, 3), ylim=(0, 3), xticks=[], yticks=[])
    ax.set_title(title, fontsize=10)
    for i, tile in enumerate(state):
        row, col = divmod(i, 3)
        y = 2 - row
        color = "#2563eb" if tile else "#e5e7eb"
        ax.add_patch(plt.Rectangle((col, y), 1, 1, facecolor=color, edgecolor="white"))
        if tile:
            ax.text(col + 0.5, y + 0.5, str(tile), ha="center", va="center", fontsize=18, color="white")


if __name__ == "__main__":
    start_state = scramble(seed=7, moves=12)
    print("Start puzzle (real, guaranteed-solvable, 12 random moves from goal):")
    for row in range(3):
        print(start_state[row * 3:row * 3 + 3])
    print("Manhattan distance to goal:", h(start_state))

    t0 = time.perf_counter()
    hc_path, hc_solved = hill_climbing(start_state)
    hc_time = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    as_path, as_explored = a_star(start_state)
    as_time = (time.perf_counter() - t0) * 1000

    print(f"\nHill Climbing: solved={hc_solved} | steps={len(hc_path)-1} | time={hc_time:.3f} ms")
    print(f"A* Search:     solved=True | steps={len(as_path)-1} | explored={as_explored} | time={as_time:.3f} ms")
    if not hc_solved:
        print("\nHill Climbing got stuck at a local minimum -- could NOT solve it.")
    print("A* always finds the shortest solution -- proven optimal for this heuristic.")

    fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
    draw_board(start_state, axes[0], "Start")
    draw_board(hc_path[-1], axes[1], f"Hill Climbing ends here\n(solved={hc_solved})")
    draw_board(GOAL, axes[2], "Goal")
    plt.tight_layout()
    plt.savefig("images/01_hill_climbing_result.png")
    plt.close()

    n = min(len(as_path), 7)
    fig, axes = plt.subplots(1, n, figsize=(2.2 * n, 2.6))
    for i, ax in enumerate(axes if n > 1 else [axes]):
        draw_board(as_path[i], ax, f"Step {i}")
    plt.tight_layout()
    plt.savefig("images/02_astar_solution_path.png")
    plt.close()

    print("\nDone. Charts saved in images/")
