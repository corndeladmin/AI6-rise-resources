import numpy as np

# Your raw list of quiz scores
quiz_scores = np.array([85, 92, 78, 85, 92, 78, 95, 85, 78, 92])

# Use np.unique to get the unique scores and their frequencies
# The function returns a tuple: (unique_values_array, counts_array)
unique_scores, score_counts = np.unique(quiz_scores, return_counts=True)

print(f"Unique Scores Achieved: {unique_scores}")
print(f"Number of Students per Score: {score_counts}")

# Output:
# Unique Scores Achieved: [78 85 92 95]
# Number of Students per Score: [3  3  3  1]