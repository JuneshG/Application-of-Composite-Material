import matplotlib.pyplot as plt

# Example data (replace these with your actual data)
materials = ['E-glass', 'S-glass', 'Graphite (high modulus)', 'Graphite (high tensile strength)', 'Boron', 'Silica', 'Tungsten', 'Beryllium', 'Kevlar 49(aramid polymer)', 
             'Steel',  'Aluminium alloys', 'Glass', 'Tungsten', 'Beryllium']
specific_modulus = [28.5, 34.5, 205, 126, 146, 33, 21, 131, 87, 26.9, 25.9, 28, 18.1, 164]  # Specific Modulus (E/ρ)
specific_strength = [1.38, 1.85, 1.1, 1.3, 2.65, 0.22, 0.71, 1.87, 0.27, 0.23, 0.84, 0.057 ]  # Specific Strength (σu/ρ)

print(len(materials))
# Custom markers and colors for each material
markers = ['o', 's', 'D', '^', 'P']
colors = ['red', 'green', 'blue', 'orange', 'purple', 'khaki', 'pink', 'gold', 'cyan', 'maroon']

# Plot each material as a separate series
for i in range(len(materials)):
    plt.scatter(specific_modulus[i], specific_strength[i], marker=markers[i], color=colors[i], label=materials[i])

# Adding labels and title
plt.xlabel('Specific Modulus (E/ρ)')
plt.ylabel('Specific Strength (σu/ρ)')
plt.title('Specific Modulus vs Specific Strength for Various Materials')

# Adding a legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Display the plot
plt.show()
