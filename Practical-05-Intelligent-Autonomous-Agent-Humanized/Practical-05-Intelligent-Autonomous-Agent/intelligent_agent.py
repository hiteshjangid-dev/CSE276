# Practical 5 - Intelligent Autonomous Agent

# 1. Simple Reflex Agent
def simple_reflex(percept):
    if percept["problem"]:
        return percept["action"]
    return percept["normal_action"]


# 2. Model-Based Agent
def model_based(percept, memory):
    memory.add(percept["state"])

    if percept["problem"]:
        return percept["action"]

    return percept["memory_action"]


# 3. Goal-Based Agent
def goal_based(percept):
    if percept["goal_done"]:
        return "Stop"

    if percept["problem"]:
        return percept["action"]

    return percept["goal_action"]


def run_example(title, examples):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)

    memory = set()

    for number, percept in enumerate(examples, 1):
        print(f"\nStep {number}: {percept['state']}")
        print("Simple Reflex :", simple_reflex(percept))
        print("Model-Based   :", model_based(percept, memory))
        print("Goal-Based    :", goal_based(percept))


# ------------------------------------------------------------
# Example 1: Robotic Vacuum Cleaner
# ------------------------------------------------------------

vacuum = [
    {
        "state": "Room A is dirty",
        "problem": True,
        "action": "Clean room",
        "normal_action": "Move",
        "memory_action": "Explore another room",
        "goal_action": "Go to dirty room",
        "goal_done": False
    },
    {
        "state": "Room B is clean",
        "problem": False,
        "action": "Clean room",
        "normal_action": "Move",
        "memory_action": "Explore another room",
        "goal_action": "Go to dirty room",
        "goal_done": False
    },
    {
        "state": "All rooms are clean",
        "problem": False,
        "action": "Clean room",
        "normal_action": "Move",
        "memory_action": "Explore another room",
        "goal_action": "Go to dirty room",
        "goal_done": True
    }
]

run_example("Robotic Vacuum Cleaner", vacuum)


# ------------------------------------------------------------
# Example 2: Warehouse Robot
# ------------------------------------------------------------

warehouse = [
    {
        "state": "Package found",
        "problem": True,
        "action": "Pick package",
        "normal_action": "Move",
        "memory_action": "Check another shelf",
        "goal_action": "Take package to delivery area",
        "goal_done": False
    },
    {
        "state": "Shelf is empty",
        "problem": False,
        "action": "Pick package",
        "normal_action": "Move",
        "memory_action": "Check another shelf",
        "goal_action": "Take package to delivery area",
        "goal_done": False
    },
    {
        "state": "Package delivered",
        "problem": False,
        "action": "Pick package",
        "normal_action": "Move",
        "memory_action": "Check another shelf",
        "goal_action": "Take package to delivery area",
        "goal_done": True
    }
]

run_example("Warehouse Robot", warehouse)


# ------------------------------------------------------------
# Example 3: Traffic Signal Controller
# ------------------------------------------------------------

traffic = [
    {
        "state": "Heavy traffic",
        "problem": True,
        "action": "Keep green longer",
        "normal_action": "Change signal",
        "memory_action": "Check other lane",
        "goal_action": "Reduce traffic",
        "goal_done": False
    },
    {
        "state": "Low traffic",
        "problem": False,
        "action": "Keep green longer",
        "normal_action": "Change signal",
        "memory_action": "Check other lane",
        "goal_action": "Reduce traffic",
        "goal_done": False
    },
    {
        "state": "Traffic is clear",
        "problem": False,
        "action": "Keep green longer",
        "normal_action": "Change signal",
        "memory_action": "Check other lane",
        "goal_action": "Reduce traffic",
        "goal_done": True
    }
]

run_example("Traffic Signal Controller", traffic)
