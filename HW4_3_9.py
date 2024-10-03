# Material properties
E_f = 70  # GPa for the glass fiber
sigma_u_f = 2800  # MPa (2.8 GPa converted to MPa)
V_f = 0.5  # Fiber volume fraction (50%)
V_m = 1 - V_f  # Matrix volume fraction

# Matrix stress from the graph at 1% strain and 4% strain for A and B
stress_matrix_A_1 = 17.5  # MPa
stress_matrix_A_4 = 35  # MPa
stress_matrix_B_1 = 35  # MPa
stress_matrix_B_4 = 70  # MPa

# Fiber stress at 1% and 4% strain using Hooke's Law (E_f * strain)
strain_1 = 0.01
strain_4 = 0.04
fiber_stress_1 = E_f * strain_1 * 1000  # Convert to MPa
fiber_stress_4 = E_f * strain_4 * 1000  # Convert to MPa

# Composite stress calculations using rule of mixtures
composite_A_1 = V_f * fiber_stress_1 + V_m * stress_matrix_A_1
composite_A_4 = V_f * fiber_stress_4 + V_m * stress_matrix_A_4

composite_B_1 = V_f * fiber_stress_1 + V_m * stress_matrix_B_1
composite_B_4 = V_f * fiber_stress_4 + V_m * stress_matrix_B_4

# Print the results
print(f"Composite A stress at 1% strain: {composite_A_1:.2f} MPa")
print(f"Composite A stress at 4% strain: {composite_A_4:.2f} MPa")
print(f"Composite B stress at 1% strain: {composite_B_1:.2f} MPa")
print(f"Composite B stress at 4% strain: {composite_B_4:.2f} MPa")
