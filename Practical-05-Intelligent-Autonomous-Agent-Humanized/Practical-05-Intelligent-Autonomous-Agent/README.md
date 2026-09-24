# Practical 5 - Intelligent Autonomous Agent for Smart Environments

## Aim

To develop a simple intelligent agent for a simulated environment and understand three agent architectures:

- Simple Reflex Agent
- Model-Based Agent
- Goal-Based Agent

The same basic Python logic is used for three common examples:

1. Robotic vacuum cleaner
2. Warehouse robot
3. Traffic signal controller

---

## 1. What is an Intelligent Agent?

An intelligent agent observes its environment and takes an action.

```text
Sense
  ↓
Decide
  ↓
Act
```

Example:

```text
Vacuum sees dirt
      ↓
Decides to clean
      ↓
Cleans the room
```

---

## 2. PEAS

PEAS describes an intelligent agent.

| Part | Meaning | Example: Vacuum |
|---|---|---|
| P | Performance Measure | Clean rooms |
| E | Environment | House |
| A | Actuators | Move, clean |
| S | Sensors | Dirt sensor |

For other examples:

```text
Warehouse robot → find and deliver packages
Traffic signal  → manage traffic flow
```

---

## 3. Agent Architectures

### Simple Reflex Agent

It looks at the **current situation only**.

```text
IF problem
THEN take action
ELSE do normal action
```

Example:

```text
Room is dirty → Clean
```

It does not remember the past.

### Model-Based Agent

It uses the current situation and **memory**.

```text
Current situation
       +
Memory
       ↓
Decision
```

Example:

```text
Room is clean
+
Already visited
↓
Explore another room
```

### Goal-Based Agent

It chooses an action according to a **goal**.

```text
Current situation
       +
Goal
       ↓
Decision
```

Example:

```text
Goal = clean all rooms
↓
Move toward a dirty room
```

### Easy memory trick

```text
Reflex   = React
Model    = Remember
Goal     = Reach
```

---

## 4. Examples

### Robotic Vacuum

```text
Dirty room → Clean
Clean room → Move
Goal       → Clean all rooms
```

### Warehouse Robot

```text
Package found → Pick
Empty shelf   → Move
Goal          → Deliver package
```

### Traffic Signal

```text
Heavy traffic → Keep green longer
Low traffic   → Change normally
Goal          → Reduce traffic
```

---

## 5. How the Code Works

Every input is a small dictionary called a **percept**.

Example:

```python
{
    "state": "Room A is dirty",
    "problem": True,
    "action": "Clean room"
}
```

The three agents read the same type of information.

```text
Percept
  ↓
Simple Reflex / Model-Based / Goal-Based
  ↓
Action
```

The only major difference is the information used:

```text
Simple Reflex → current percept

Model-Based   → current percept + memory

Goal-Based    → current percept + goal
```

---

## 6. Complete Google Colab Code

Copy the code from:

```text
intelligent_agent.py
```

into one Google Colab cell and run it.

No dataset is required.

No AI framework is required.

Only Python is needed.

---

## 7. Output

The program prints decisions such as:

```text
Step 1: Room A is dirty
Simple Reflex : Clean room
Model-Based   : Clean room
Goal-Based    : Clean room
```

The same process is then demonstrated for:

```text
Vacuum
Warehouse
Traffic Signal
```

This makes it easy to see how the same intelligent-agent concept works in different applications.

---

## 8. Workflow

```text
Environment
    ↓
Percept / Sensor
    ↓
Agent Architecture
    ↓
Decision
    ↓
Action
    ↓
Environment changes
```

### Architecture view

```text
                 Percept
                    ↓
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       Reflex     Model      Goal
          ↓         ↓         ↓
       Action     Action    Action
```

---

## 9. Result

Three intelligent agent architectures were successfully implemented and demonstrated using three simulated smart-environment examples.

The agents showed different decision rules based on:

- current information,
- memory, and
- desired goal.

---

## 10. Conclusion

This practical demonstrates the basic decision-making process of intelligent agents.

```text
Simple Reflex
→ uses current situation

Model-Based
→ uses current situation + memory

Goal-Based
→ uses current situation + goal
```

The same concept can be used in robots, smart homes, warehouses, traffic systems, and many other autonomous applications.

---

## 11. Viva Questions

**1. What is an intelligent agent?**  
A system that observes its environment and takes actions.

**2. What is a simple reflex agent?**  
It chooses an action from the current percept.

**3. Does a simple reflex agent have memory?**  
No.

**4. What is a model-based agent?**  
It uses the current percept and stored information about the environment.

**5. What is a goal-based agent?**  
It chooses actions to achieve a goal.

**6. What does PEAS stand for?**

```text
Performance Measure
Environment
Actuators
Sensors
```

**7. Why is the vacuum a good example?**  
It senses the room and automatically decides whether to clean or move.

**8. What is the main difference between the three architectures?**  
The information used to make the decision.

---

## 12. Files

| File | Description |
|---|---|
| `README.md` | Practical explanation |
| `intelligent_agent.py` | Complete Colab-friendly code |
