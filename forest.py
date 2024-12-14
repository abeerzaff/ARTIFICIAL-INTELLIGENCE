data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Hot', 'Play?': 'No'}
]

attributes = ['Weather', 'Temperature']
target_col = 'Play?'

def subset(data, key, value):
    return [entry for entry in data if entry[key] == value]

def calculate_entropy(data, target_col):
    from math import log2
    values = [entry[target_col] for entry in data]
    probs = {v: values.count(v) / len(values) for v in set(values)}
    return -sum(p * log2(p) for p in probs.values())

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    values = {entry[attribute] for entry in data}
    weighted_entropy = sum((len(subset(data, attribute, v)) / len(data)) * calculate_entropy(subset(data, attribute, v), target_col) for v in values)
    return total_entropy - weighted_entropy

def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if depth == max_depth or all(entry[target_col] == data[0][target_col] for entry in data):
        return max(set(entry[target_col] for entry in data), key=lambda v: sum(e[target_col] == v for e in data))
    best_attr = max(attributes, key=lambda attr: calculate_information_gain(data, attr, target_col))
    tree = {best_attr: {}}
    for val in {entry[best_attr] for entry in data}:
        subtree = build_tree(subset(data, best_attr, val), [a for a in attributes if a != best_attr], target_col, depth + 1, max_depth)
        tree[best_attr][val] = subtree
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    attr, branches = next(iter(tree.items()))
    return predict(branches[data_point[attr]], data_point) if data_point[attr] in branches else None

forest = [build_tree(data, attributes, target_col) for _ in range(2)]

new_data_point = {'Weather': 'Rainy', 'Temperature': 'Mild'}
prediction = max([predict(tree, new_data_point) for tree in forest], key=lambda v: sum(predict(tree, new_data_point) == v for tree in forest))

print("Random Forest Trees:")
for i, tree in enumerate(forest, 1):
    print(f"Tree {i}: {tree}")

print("\nNew Data Point:", new_data_point)
print("Prediction:", prediction)
