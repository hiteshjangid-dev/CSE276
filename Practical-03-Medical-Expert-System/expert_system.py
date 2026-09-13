import matplotlib.pyplot as plt

# Simplified educational symptom rules
rules = {
    "Dengue": {"high fever", "severe headache", "pain behind eyes", "joint pain", "rash", "nausea"},
    "Malaria": {"fever with chills", "sweating", "headache", "nausea", "vomiting", "muscle pain"},
    "Typhoid": {"prolonged fever", "abdominal pain", "weakness", "loss of appetite", "headache"},
    "Common Cold/Flu": {"cough", "sore throat", "runny nose", "mild fever", "sneezing"}
}

# Sample cases for classroom testing
patients = {
    "Patient A": {"high fever", "severe headache", "pain behind eyes", "joint pain", "rash"},
    "Patient B": {"fever with chills", "sweating", "headache", "vomiting"},
    "Patient C": {"cough", "sore throat", "runny nose", "sneezing"},
    "Patient D": {"prolonged fever", "abdominal pain", "weakness", "loss of appetite"}
}


def diagnose(symptoms):
    results = {}

    for disease, rule in rules.items():
        matched = symptoms & rule
        confidence = len(matched) / len(rule)
        results[disease] = confidence

    return sorted(results.items(), key=lambda item: item[1], reverse=True)


print("RULE-BASED MEDICAL EXPERT SYSTEM")
print("=" * 45)

patient_names = list(patients)
chart_scores = {disease: [] for disease in rules}

for patient, symptoms in patients.items():
    results = diagnose(symptoms)
    best_disease, best_confidence = results[0]

    print(f"\n{patient}")
    print("Symptoms:", ", ".join(sorted(symptoms)))

    for disease, confidence in results:
        if confidence > 0:
            print(f"{disease}: {confidence:.0%}")
        chart_scores[disease].append(confidence)

    print(f"Suggested: {best_disease} ({best_confidence:.0%})")

# Visual comparison
x = range(len(patient_names))
width = 0.18

plt.figure(figsize=(9, 5))

for index, disease in enumerate(rules):
    positions = [value + index * width for value in x]
    plt.bar(positions, chart_scores[disease], width, label=disease)

plt.xticks(
    [value + 1.5 * width for value in x],
    patient_names
)
plt.ylabel("Confidence")
plt.ylim(0, 1)
plt.title("Expert System Confidence by Patient")
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig("images/01_diagnosis_confidence.png")
plt.show()
