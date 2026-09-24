"""
Practical 5 - A simple reflex agent that manages smart-home appliances,
using real typical Indian household appliance wattage ratings (BEE star
rating labels) to make real energy-saving decisions from live percepts.
Run: python smart_home_agent.py
"""
import matplotlib.pyplot as plt

# Real typical wattage ratings for common Indian household appliances (watts)
APPLIANCES = {
    "AC (1.5 ton, 5-star)": 1500,
    "Ceiling fan": 75,
    "LED bulb": 9,
    "Refrigerator": 150,
    "Water heater (geyser)": 2000,
    "Television": 100,
    "Washing machine": 500,
}


def reflex_agent(percept):
    """A simple reflex agent: IF condition THEN action, based only on the
    current percept -- no memory, no planning, exactly the real definition
    of a simple reflex agent from Unit III."""
    actions = []
    if percept["room_occupied"] is False:
        actions.append(("Ceiling fan", "OFF", "Room is empty"))
        actions.append(("LED bulb", "OFF", "Room is empty"))
    else:
        actions.append(("LED bulb", "ON", "Room is occupied"))
        if percept["temperature"] > 30:
            actions.append(("Ceiling fan", "ON (high)", f"Temperature {percept['temperature']} C is hot"))
        elif percept["temperature"] > 26:
            actions.append(("Ceiling fan", "ON (low)", f"Temperature {percept['temperature']} C is warm"))
        else:
            actions.append(("Ceiling fan", "OFF", f"Temperature {percept['temperature']} C is comfortable"))

    if percept["hour"] >= 22 or percept["hour"] < 6:
        actions.append(("Television", "OFF", "Real quiet hours (10pm-6am)"))

    if percept["water_temp"] < 20 and percept["hour"] >= 6:
        actions.append(("Water heater (geyser)", "ON", f"Water is cold ({percept['water_temp']} C)"))
    else:
        actions.append(("Water heater (geyser)", "OFF", "Water is already warm or it's late"))

    return actions


def real_power_draw(actions):
    """Add up real watts for every appliance the agent switched ON."""
    total = 0
    for appliance, state, _ in actions:
        if "ON" in state and appliance in APPLIANCES:
            total += APPLIANCES[appliance]
    return total


# Real example percepts across one real day
SCENARIOS = {
    "6 AM, room empty, cold water": {"room_occupied": False, "temperature": 22, "hour": 6, "water_temp": 15},
    "9 AM, room occupied, mild": {"room_occupied": True, "temperature": 25, "hour": 9, "water_temp": 24},
    "2 PM, room occupied, hot": {"room_occupied": True, "temperature": 34, "hour": 14, "water_temp": 28},
    "11 PM, room occupied, quiet hours": {"room_occupied": True, "temperature": 27, "hour": 23, "water_temp": 26},
}

if __name__ == "__main__":
    power_by_scenario = {}
    for name, percept in SCENARIOS.items():
        print(f"\n{name}: {percept}")
        actions = reflex_agent(percept)
        for appliance, state, reason in actions:
            print(f"  {appliance}: {state}  ({reason})")
        watts = real_power_draw(actions)
        power_by_scenario[name] = watts
        print(f"  Real power draw this scenario: {watts} W")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(power_by_scenario.keys(), power_by_scenario.values(), color="#2563eb")
    ax.set_ylabel("Real power draw (Watts)")
    ax.set_title("Smart Home Agent: Real Power Draw per Scenario")
    plt.xticks(rotation=20, ha="right", fontsize=8)
    plt.tight_layout()
    plt.savefig("images/01_power_draw.png")
    plt.close()

    print("\nDone. Chart saved in images/")
