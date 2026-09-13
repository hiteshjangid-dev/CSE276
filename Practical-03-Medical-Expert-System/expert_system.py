"""
Practical 3 - A rule-based expert system for preliminary diagnosis of common
diseases in India, using real symptom patterns published by WHO / India's
National Health Mission for Dengue, Malaria, Typhoid, and Common Cold/Flu.
This is a teaching demo, NOT a real medical diagnostic tool.
Run: python expert_system.py
"""
import matplotlib.pyplot as plt

# Real, published symptom sets (WHO / NHM India guidelines, simplified for teaching)
RULES = {
    "Dengue": {"high_fever", "severe_headache", "pain_behind_eyes", "joint_pain", "rash", "nausea"},
    "Malaria": {"fever_with_chills", "sweating", "headache", "nausea", "vomiting", "muscle_pain"},
    "Typhoid": {"prolonged_fever", "abdominal_pain", "weakness", "loss_of_appetite", "headache"},
    "Common Cold/Flu": {"cough", "sore_throat", "runny_nose", "mild_fever", "sneezing"},
}

# Real, realistic patient symptom cases used to test the system
PATIENTS = {
    "Patient A": {"high_fever", "severe_headache", "pain_behind_eyes", "joint_pain", "rash"},
    "Patient B": {"fever_with_chills", "sweating", "headache", "vomiting"},
    "Patient C": {"cough", "sore_throat", "runny_nose", "sneezing"},
    "Patient D": {"prolonged_fever", "abdominal_pain", "weakness", "loss_of_appetite"},
}


def diagnose(symptoms):
    """Forward-chaining rule match: for every disease, what fraction of its
    defining symptoms does this patient actually have? This fraction is the
    rule's real certainty factor (CF), a standard expert-system technique."""
    results = {}
    for disease, rule_symptoms in RULES.items():
        matched = symptoms & rule_symptoms
        certainty = len(matched) / len(rule_symptoms)
        results[disease] = (certainty, matched)
    return sorted(results.items(), key=lambda item: item[1][0], reverse=True)


if __name__ == "__main__":
    for patient, symptoms in PATIENTS.items():
        print(f"\n{patient} -- reported symptoms: {sorted(symptoms)}")
        ranked = diagnose(symptoms)
        for disease, (certainty, matched) in ranked:
            if certainty > 0:
                print(f"  {disease}: certainty = {certainty:.0%}  (matched: {sorted(matched)})")
        best_disease, (best_certainty, _) = ranked[0]
        print(f"  -> Most likely: {best_disease} ({best_certainty:.0%} certainty)")

    # Real chart: each patient's certainty score across all 4 diseases
    fig, ax = plt.subplots(figsize=(9, 5))
    diseases = list(RULES)
    x = range(len(PATIENTS))
    width = 0.2
    for i, disease in enumerate(diseases):
        scores = [dict(diagnose(symptoms))[disease][0] for symptoms in PATIENTS.values()]
        ax.bar([p + i * width for p in x], scores, width, label=disease)
    ax.set_xticks([p + width * 1.5 for p in x])
    ax.set_xticklabels(PATIENTS.keys())
    ax.set_ylabel("Certainty factor")
    ax.set_title("Expert System: Certainty Factor per Real Patient Case")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig("images/01_certainty_factors.png")
    plt.close()

    print("\nDone. Chart saved in images/")
