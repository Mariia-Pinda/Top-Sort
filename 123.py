edges = {'a': ['c'], 'c': ['b'], 'd': ['c', 'b', 't'], 'b': [], 't': []}  # вхідні дані: словник, де ключі - вершини орграфа, а значення - вершини, суміжні з ними
                                                                          # граф повинен бути ациклічним
stack = []
edges_list = []

for key in edges:
    edges_list.append(key)


def top_sort(edges, stack, edges_list):
    while len(edges.keys()) != 0:
        for key in edges_list:
            values_list = []
            for val in edges.values():
                for el in val:
                    values_list.append(el)
            if key not in values_list:
                stack.append(key)
                edges_list.remove(key)
                edges.pop(key)
    return stack


stack = top_sort(edges, stack, edges_list)
print(stack)                                                                 # результат - список вершин, що відсортовані за допомогою топологічного сортування



