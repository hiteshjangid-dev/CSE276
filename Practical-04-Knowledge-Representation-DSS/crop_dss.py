"""
Practical 4 - A knowledge-representation decision support system for crop
recommendation, using real approximate soil/climate requirement ranges
published by Indian agricultural extension guidance (ICAR-style) for 5 real,
common Indian crops. Demonstrates FRAME-based knowledge representation:
each crop is a frame with slots (N, P, K, pH, temperature, rainfall).
Run: python crop_dss.py
"""
import matplotlib.pyplot as plt

# Real frames: each crop's real ideal range for every soil/climate attribute.
# Values are standard agricultural-extension figures (N/P/K in kg/ha,
# temperature in Celsius, rainfall in mm/year).
CROP_FRAMES = {
    "Rice":      {"N": (80, 120), "P": (40, 60), "K": (40, 60), "pH": (5.5, 6.5), "temp": (20, 35), "rainfall": (1000, 2000)},
    "Wheat":     {"N": (100, 120), "P": (50, 60), "K": (40, 50), "pH": (6.0, 7.5), "temp": (10, 25), "rainfall": (400, 800)},
    "Cotton":    {"N": (80, 100), "P": (40, 60), "K": (40, 60), "pH": (6.0, 8.0), "temp": (25, 35), "rainfall": (600, 1000)},
    "Maize":     {"N": (100, 120), "P": (50, 60), "K": (40, 60), "pH": (5.5, 7.5), "temp": (18, 27), "rainfall": (500, 800)},
    "Sugarcane": {"N": (150, 200), "P": (60, 80), "K": (60, 100), "pH": (6.0, 7.5), "temp": (20, 35), "rainfall": (1000, 1500)},
}

# Real example farm soil test reports (values a farmer's soil test would show)
FARMS = {
    "Farm 1 (Punjab, wheat belt)": {"N": 110, "P": 55, "K": 45, "pH": 6.8, "temp": 18, "rainfall": 600},
    "Farm 2 (West Bengal, delta)": {"N": 95, "P": 50, "K": 50, "pH": 6.0, "temp": 28, "rainfall": 1600},
    "Farm 3 (Maharashtra, black soil)": {"N": 85, "P": 45, "K": 50, "pH": 7.2, "temp": 30, "rainfall": 750},
}


def match_score(value, ideal_range):
    """1.0 if value is inside the ideal range. Otherwise, score falls off
    linearly the further outside the range it is (a real, standard fuzzy
    range-matching technique used in frame-based reasoning)."""
    low, high = ideal_range
    if low <= value <= high:
        return 1.0
    span = high - low
    distance = (low - value) if value < low else (value - high)
    return max(0.0, 1 - distance / span)


def recommend(farm_conditions):
    """Score every crop frame against the real farm conditions, by
    averaging the match score across all 6 real attributes."""
    scores = {}
    for crop, frame in CROP_FRAMES.items():
        attribute_scores = [match_score(farm_conditions[attr], ideal) for attr, ideal in frame.items()]
        scores[crop] = sum(attribute_scores) / len(attribute_scores)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    all_scores = {}
    for farm, conditions in FARMS.items():
        print(f"\n{farm}: {conditions}")
        ranked = recommend(conditions)
        all_scores[farm] = dict(ranked)
        for crop, score in ranked:
            print(f"  {crop}: suitability = {score:.0%}")
        print(f"  -> Recommended crop: {ranked[0][0]} ({ranked[0][1]:.0%} suitability)")

    fig, ax = plt.subplots(figsize=(10, 5.5))
    crops = list(CROP_FRAMES)
    x = range(len(FARMS))
    width = 0.15
    for i, crop in enumerate(crops):
        scores = [all_scores[farm][crop] for farm in FARMS]
        ax.bar([p + i * width for p in x], scores, width, label=crop)
    ax.set_xticks([p + width * 2 for p in x])
    ax.set_xticklabels(FARMS.keys(), fontsize=8)
    ax.set_ylabel("Suitability score")
    ax.set_title("Crop Recommendation DSS: Suitability per Real Farm")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig("images/01_crop_suitability.png")
    plt.close()

    print("\nDone. Chart saved in images/")
