deviations = [-3.5, 2.0, -1.8, 0.0, 4.1]
# Prepare an empty list for results
abs_deviations_imperative = [] 

for dev in deviations:
    # Explicitly calculate abs value and add
    abs_deviations_imperative.append(abs(dev)) 

print("Imperative (Absolute Deviations):", abs_deviations_imperative)
# Output: Imperative (Absolute Deviations): [3.5, 2.0, 1.8, 0.0, 4.1]