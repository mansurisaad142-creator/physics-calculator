import numpy as np

print("=" * 60)
print("         PHYSICS CALCULATOR - ENERGY & STRESS ANALYSIS")
print("=" * 60)

# Input parameters
m = (np.array([(int(input("Enter mass (in kg): ")))]))
h = np.array([int(input("Enter height (in m): "))])
v = np.array([int(input("Enter velocity (in m/s): "))])
diameter = np.array([int(input("Enter diameter (in mm): "))])
force = np.array([int(input("Enter force (in N): "))])

# Calculate Potential Energy (PE)
# PE = m * g * h (where g = 9.8 m/s^2)
PE = 9.8 * m * h

# Calculate Kinetic Energy (KE)
# KE = 0.5 * m * v^2
KE = 0.5 * m * v**2

# Calculate Cross-sectional area
# Area = π * (diameter/2)^2
area = np.pi * (diameter / 2)**2

# Calculate Stress
# Stress = Force / Area
stress = force / area

# Display Results
print("\n" + "=" * 60)
print("                    CALCULATION RESULTS")
print("=" * 60)
print(f'Kinetic Energy (KE) = {KE} J (Joules)')
print(f'Potential Energy (PE) = {PE} J (Joules)')
print(f'Stress = {stress} Pa (Pascals / N/m²)')
print("=" * 60)

# Additional calculations
total_energy = KE + PE
print(f'\nTotal Mechanical Energy = {total_energy} J')
print(f'Stress Value = {stress[0]:.2f} Pa')
print("=" * 60)
