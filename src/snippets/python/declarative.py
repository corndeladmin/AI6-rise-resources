deviations = [-3.5, 2.0, -1.8, 0.0, 4.1]
# Declare the content: abs value of each item
abs_deviations_declarative = [abs(dev) for dev in deviations]

print("Declarative (Absolute Deviations):", abs_deviations_declarative)
# Output: Declarative (Absolute Deviations): [3.5, 2.0, 1.8, 0.0, 4.1]