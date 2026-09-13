import matplotlib.pyplot as plt


# Admission rules
rules = {
    "admit": (75, 70),
    "waitlist": (60, 50),
    "scholarship": (90, 85)
}


# Applicant frames
applicants = [
    {
        "name": "Aman",
        "percentage": 92,
        "entrance_score": 88,
        "interview_score": 84,
        "documents_complete": True
    },
    {
        "name": "Riya",
        "percentage": 78,
        "entrance_score": 72,
        "interview_score": 76,
        "documents_complete": True
    },
    {
        "name": "Kabir",
        "percentage": 65,
        "entrance_score": 55,
        "interview_score": 68,
        "documents_complete": True
    },
    {
        "name": "Neha",
        "percentage": 52,
        "entrance_score": 45,
        "interview_score": 60,
        "documents_complete": False
    }
]


# Apply the admission rules
def make_decision(applicant):

    if (
        applicant["percentage"] >= rules["admit"][0]
        and applicant["entrance_score"] >= rules["admit"][1]
        and applicant["documents_complete"]
    ):
        decision = "Admit"

    elif (
        applicant["percentage"] >= rules["waitlist"][0]
        and applicant["entrance_score"] >= rules["waitlist"][1]
        and applicant["documents_complete"]
    ):
        decision = "Waitlist"

    else:
        decision = "Reject"

    scholarship = (
        applicant["percentage"] >= rules["scholarship"][0]
        and applicant["entrance_score"] >= rules["scholarship"][1]
    )

    return decision, scholarship


results = []

for applicant in applicants:
    decision, scholarship = make_decision(applicant)
    results.append(decision)

    print(
        applicant["name"],
        "->",
        decision,
        "| Scholarship:",
        "Yes" if scholarship else "No"
    )


# Show decision counts
counts = [
    results.count("Admit"),
    results.count("Waitlist"),
    results.count("Reject")
]

plt.bar(
    ["Admit", "Waitlist", "Reject"],
    counts
)

plt.title("University Admission Decisions")
plt.ylabel("Number of Applicants")
plt.show()
