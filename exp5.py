import numpy as np

student_scores = np.array([
    [80,75,90,85],
    [70,88,92,78],
    [85,80,86,90],
    [60,70,75,80]
])

subjects = ["Math","Science","English","History"]

avg_scores = np.mean(student_scores, axis=0)

print("Average score per subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", avg_scores[i])

highest_subject = subjects[np.argmax(avg_scores)]
print("\nHighest average subject:", highest_subject)
