def calculate_structure_sum(data_structure):
    total = 0
    if isinstance(data_structure,(int,float)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (set, tuple,list)):
        for item in data_structure:
            total += calculate_structure_sum(item)
    elif isinstance(data_structure,dict):
        for value in data_structure.values():
            total += calculate_structure_sum(value)
        for keys in data_structure.keys():
            total += calculate_structure_sum(len(keys))



    return total


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)