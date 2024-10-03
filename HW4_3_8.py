import matplotlib.pyplot as plt

# Material properties from the table (Density, Weight %, Young's Modulus, Tensile Strength)
materials = {
    'Binder': {
        'density': 1.3,  # g/cm^3
        'weight_percentage': 35,  # %
        'E': 3.5,  # Young's modulus in GPa
        'sigma_max': 0.06  # Maximum tensile strength in GPa
    },
    'Fiber A': {
        'density': 2.5,  # g/cm^3
        'weight_percentage': 45,  # %
        'E': 70,  # Young's modulus in GPa
        'sigma_max': 1.4  # Maximum tensile strength in GPa
    },
    'Fiber B': {
        'density': 1.6,  # g/cm^3
        'weight_percentage': 20,  # %
        'E': 6,  # Young's modulus in GPa
        'sigma_max': 0.45  # Maximum tensile strength in GPa
    }
}

# Total cross-sectional area of the rod
total_area = 10  # cm^2

# Calculate volume fractions based on weight percentages and densities
volume_fractions = {}
total_inverse_density_weight_ratio = 0

# First, compute the sum of weight% / density for normalization
for material, props in materials.items():
    total_inverse_density_weight_ratio += props['weight_percentage'] / props['density']

# Now calculate the volume fractions and area for each material
for material, props in materials.items():
    volume_fraction = (props['weight_percentage'] / props['density']) / total_inverse_density_weight_ratio
    volume_fractions[material] = volume_fraction
    materials[material]['area'] = volume_fraction * total_area  # Cross-sectional area

# Function to calculate maximum load before failure
def calculate_max_load(materials):
    max_loads = {}
    for material, properties in materials.items():
        max_stress = properties['sigma_max']  # Maximum stress the material can handle
        area = properties['area']  # Cross-sectional area of the material
        # Calculate the maximum load the material can carry (force = stress * area)
        max_load = max_stress * area  # Load in GPa * cm² = GPa * cm²
        max_loads[material] = max_load  # Store the max load for each material
    return max_loads

# Get the maximum loads for each material
max_loads = calculate_max_load(materials)

# Find the limiting load (smallest maximum load)
limiting_material = min(max_loads, key=max_loads.get)
limiting_load = max_loads[limiting_material]

print("Maximum loads each material can carry before failure:")
for material, load in max_loads.items():
    print(f"{material}: {load:.2f} GPa*cm²")
    print(f"{material} Area: {materials[material]['area']:.2f} cm²")

print(f"\nThe limiting material is '{limiting_material}' which fails first.")
print(f"The maximum load the rod can carry is {limiting_load:.2f} GPa*cm².")

# Plotting load vs. elongation for each material (just for illustration)
def plot_load_elongation(materials, max_load):
    loads = []
    elongations = {material: [] for material in materials}
    increments = 50  # Number of increments for the plot

    for load in range(1, increments+1):
        current_load = (load / increments) * max_load
        loads.append(current_load)
        for material, props in materials.items():
            elongation = current_load / (props['E'] * props['area'])  # Simplified elongation formula
            elongations[material].append(elongation)
    
    for material, elong in elongations.items():
        plt.plot(loads, elong, label=material)

    plt.xlabel("Load (GPa*cm²)")
    plt.ylabel("Elongation")
    plt.legend()
    plt.title("Load vs Elongation for Different Materials")
    plt.show()

# Plot load-elongation curves
plot_load_elongation(materials, limiting_load)
