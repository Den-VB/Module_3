# Задание "Раз, два, три, четыре, пять .... Это не всё?

structure_2 = []

def data_structure(data):
    global structure_2
    result = 0
    structure = []
    for i in data:
        if isinstance(i, str):
            i = len(i)
        if isinstance(i, set):
            i = list(i)
        if isinstance(i, tuple):
            i = list(i)
        if isinstance(i, dict):
            i = list(zip(i.keys(), i.values()))
        if isinstance(i, list):
            structure.extend(data_structure(i))
        else:
            structure.append(i)

    structure_2 = structure
    return structure

data_structure([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])])
print(sum(structure_2))
