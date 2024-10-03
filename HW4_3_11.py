# Given Data
E_aluminum = 70  # GPa
rho_aluminum = 2.7  # g/cm³

E_f = 390  # GPa (Graphite Fiber)
rho_f = 1.9  # g/cm³

E_m = 3.5  # GPa (Epoxy Matrix)
rho_m = 1.2  # g/cm³

# Step 1: Calculate the required fiber volume fraction (V_f)
E_c = E_aluminum  # We want the composite modulus to match aluminum

# Using Rule of Mixtures: E_c = V_f * E_f + (1 - V_f) * E_m
# Solve for V_f
V_f = (E_c - E_m) / (E_f - E_m)

# Matrix Volume Fraction (V_m)
V_m = 1 - V_f

# Step 2: Calculate the composite density
rho_c = V_f * rho_f + V_m * rho_m

# Step 3: Calculate the percentage weight saving
weight_saving = (rho_aluminum - rho_c) / rho_aluminum * 100

# Display Results
print(f"Required Fiber Volume Fraction (V_f): {V_f:.4f}")
print(f"Composite Density (rho_c): {rho_c:.4f} g/cm³")
print(f"Percentage Weight Saving: {weight_saving:.2f}%")