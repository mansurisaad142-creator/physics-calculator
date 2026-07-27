# Physics Calculator 🔬

A comprehensive Python project for calculating physics-related quantities including energy analysis and material stress calculations.

## 🎯 Features

### Physics Calculator Module
- ✅ **Kinetic Energy (KE)** - Calculate KE = 0.5 × m × v²
- ✅ **Potential Energy (PE)** - Calculate PE = m × g × h
- ✅ **Stress Analysis** - Calculate stress = Force / Area
- ✅ **Total Mechanical Energy** - Sum of KE and PE
- ✅ **Array Operations** - Using NumPy for efficient calculations

### Stress Calculator Module
- ✅ **Range-based Force Analysis** - Analyze stress across force range
- ✅ **Material Safety Check** - Warn when stress exceeds limits
- ✅ **Danger Alert System** - Automatic warnings for unsafe conditions
- ✅ **Formatted Output** - Clear, readable results

## 📋 Prerequisites

```bash
pip install numpy
```

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/mansurisaad142-creator/physics-calculator.git
cd physics-calculator

# Install dependencies
pip install -r requirements.txt
```

## 💻 How to Use

### Physics Calculator
```bash
python src/physics_calculator.py
```

**Input required:**
- Mass (in kg)
- Height (in m)
- Velocity (in m/s)
- Diameter (in mm)
- Force (in N)

**Output:**
- Kinetic Energy (J)
- Potential Energy (J)
- Stress (Pa)
- Total Mechanical Energy (J)

### Stress Calculator
```bash
python src/stress_calculator.py
```

**Input required:**
- Starting limit of force (in N)
- Ending limit of force (in N)
- Area (in mm²)
- Stress limit of material (in N/m²)

**Output:**
- Stress for each force value
- Safety status (✓ Safe or ⚠️ Danger)
- Alert when stress exceeds limit

## 📊 Example Usage

### Physics Calculator Example
```
Enter mass (in kg): 10
Enter height (in m): 5
Enter velocity (in m/s): 20
Enter diameter (in mm): 50
Enter force (in N): 1000

OUTPUT:
Kinetic Energy (KE) = 2000.0 J (Joules)
Potential Energy (PE) = 490.0 J (Joules)
Stress = 509.30 Pa (Pascals / N/m²)
Total Mechanical Energy = 2490.0 J
```

### Stress Calculator Example
```
Starting limit of force (in N): 100
Ending limit of force (in N): 500
Area (in mm²): 50
Stress limit of material (in N/m²): 5000

OUTPUT:
Force: 100N | Stress: 2.0000 N/m² ✓ Safe
Force: 101N | Stress: 2.0200 N/m² ✓ Safe
...
Force: 250N | Stress: 5.0000 N/m² ⚠️ DANGER!
```

## 📁 Project Structure

```
physics-calculator/
├── src/
│   ├── physics_calculator.py      # Energy and stress calculations
│   └── stress_calculator.py       # Material stress analysis
├── requirements.txt               # Python dependencies
├── README.md                      # Documentation
└── .gitignore                     # Git ignore rules
```

## 🔬 Physics Formulas Used

### Kinetic Energy
```
KE = 0.5 × m × v²
where:
  m = mass (kg)
  v = velocity (m/s)
```

### Potential Energy
```
PE = m × g × h
where:
  m = mass (kg)
  g = acceleration due to gravity (9.8 m/s²)
  h = height (m)
```

### Stress
```
Stress = Force / Area
where:
  Force (N)
  Area (m²)
  Stress (Pa or N/m²)
```

### Cross-sectional Area (Circular)
```
Area = π × (diameter/2)²
```

## 🏷️ Topics

`python` `physics` `energy` `stress` `numpy` `calculator` `mechanics` `material-science` `engineering`

## 📜 License

MIT License - Feel free to use and modify this project

## 👨‍💻 Author

**Mo Saad**
- GitHub: [@mansurisaad142-creator](https://github.com/mansurisaad142-creator)
- Email: mansurisaad142@gmail.com

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork and submit pull requests.

---

⭐ If you find this project helpful, please consider giving it a star!
