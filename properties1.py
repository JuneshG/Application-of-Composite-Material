# Define material properties for fiber and matrix for each composite
materials = {
    'glass_epoxy': {
        'E_f': 72,  # Young's modulus of glass fibers in GPa
        'E_m': 3.2, # Young's modulus of epoxy in GPa
        'G_f': 30,  # Shear modulus of glass fibers in GPa
        'G_m': 1.5, # Shear modulus of epoxy in GPa
        'nu_f': 0.22,  # Poisson's ratio of glass fibers
        'nu_m': 0.35   # Poisson's ratio of epoxy
    },
    'graphite_epoxy': {
        'E_f': 230,  # Young's modulus of graphite fibers in GPa
        'E_m': 3.2,
        'G_f': 90,   # Shear modulus of graphite fibers in GPa
        'G_m': 1.5,
        'nu_f': 0.2,
        'nu_m': 0.35
    },
    'kevlar_epoxy': {
        'E_f': 130,  # Young's modulus of Kevlar fibers in GPa
        'E_m': 3.2,
        'G_f': 40,   # Shear modulus of Kevlar fibers in GPa
        'G_m': 1.5,
        'nu_f': 0.34,
        'nu_m': 0.35
    },
    'boron_aluminum': {
        'E_f': 400,  # Young's modulus of boron fibers in GPa
        'E_m': 70,   # Young's modulus of aluminum in GPa
        'G_f': 180,  # Shear modulus of boron fibers in GPa
        'G_m': 26,   # Shear modulus of aluminum in GPa
        'nu_f': 0.1,
        'nu_m': 0.33
    }
}

# Define volume fractions to analyze
volume_fractions = [0.25, 0.50, 0.75]

# Function to calculate the moduli and Poisson's ratio
def calculate_properties(material, V_f):
    V_m = 1 - V_f
    
    # Calculate Longitudinal Modulus (E_L)
    E_L = V_f * material['E_f'] + V_m * material['E_m']
    
    # Calculate Transverse Modulus (E_T)
    E_T = 1 / (V_f / material['E_f'] + V_m / material['E_m'])
    
    # Calculate Shear Modulus (G_LT)
    G_LT = 1 / (V_f / material['G_f'] + V_m / material['G_m'])
    
    # Calculate Poisson's Ratio (nu_LT)
    nu_LT = V_f * material['nu_f'] + V_m * material['nu_m']
    
    return E_L, E_T, G_LT, nu_LT

# Loop through each material and calculate properties for each volume fraction
for material_name, material_props in materials.items():
    print(f"\nMaterial: {material_name}")
    for V_f in volume_fractions:
        E_L, E_T, G_LT, nu_LT = calculate_properties(material_props, V_f)
        print(f"V_f = {V_f * 100}%")
        print(f"  Longitudinal Modulus (E_L): {E_L:.2f} GPa")
        print(f"  Transverse Modulus (E_T): {E_T:.2f} GPa")
        print(f"  Shear Modulus (G_LT): {G_LT:.2f} GPa")
        print(f"  Poisson's Ratio (nu_LT): {nu_LT:.3f}")
