#define properties of different shapes

shapes = {'square': {'formula': lambda s : s * s},
          'circle': {'formula': lambda r : 3.14 * r * r},
          'triangle': {'formula': lambda b, h : 0.5 * b * h}}

sizes = {
    'square': [2,4,6],
    'circle' : [1,3,5],
    'triangle' : [(3,4), (5,6), (7,8)]
}

# Loop through each shape and calculate the area for each size
for shape_name, shape_props in shapes.items():
    print(f"Shape: {shape_name}")
    for size in sizes[shape_name]:
        if shape_name == 'triangle':
            area = shape_props['formula'](*size)
        else:
            area = shape_props['formula'](size)
    
        print(f"Size : {size}, area : {area:.2f}")
            
