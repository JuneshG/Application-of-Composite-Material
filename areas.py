shapes = {'square': {'function': lambda s: s*s},
          'circle': {'function': lambda r: 3.14 * r**2},
          'triangle': {'function': lambda b,h: 0.5*b*h}}

sizes = {'square': [2,4,6],
         'circle': [1,3,5],
         'triangle': [(1,2),(3,4),(5,6)]}
            
for shape_name, shape_formula in shapes.items():
    print(f'\nShape: {shape_name} ')
    for size in sizes[shape_name]:
        if shape_name == 'triangle':
            area = shape_formula['function'](*size)
        else:
            area = shape_formula['function'](size)
        
        print(f'Size: {size}, area: {area}')

