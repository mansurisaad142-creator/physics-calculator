import numpy as np

print("=" * 60)
print("         STRESS CALCULATOR - MATERIAL ANALYSIS")
print("=" * 60)

start = int(input("\nStarting limit of force (in N): "))
end = int(input("Ending limit of force (in N): "))
area = int(input("Area (in mm²): "))
stress_limit = float(input("Ending limit of material stress (in N/m²): "))

if area == 0:
    print("\n❌ ERROR: Area cannot be zero! Not allowed.")
else:
    print("\n" + "=" * 60)
    print("              STRESS ANALYSIS RESULTS")
    print("=" * 60)
    print(f"Force Range: {start}N - {end}N")
    print(f"Area: {area} mm²")
    print(f"Stress Limit: {stress_limit} N/m²")
    print("=" * 60 + "\n")
    
    danger_triggered = False
    for force in range(start, end):
        stress = force / area
        print(f'Force: {force}N | Stress: {stress:.4f} N/m²', end="")
        
        if stress >= stress_limit:
            print(" ⚠️  DANGER! Material limit exceeded!")
            danger_triggered = True
            break
        else:
            print(" ✓ Safe")
    
    if not danger_triggered:
        print(f"\n✓ All forces within safe limits!")
    
    print("\n" + "=" * 60)
