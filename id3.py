
import math
def calculate_entropy(data, target_col):
    values = {}
    for row in data:
        values[row[target_col]] = values.get(row[target_col], 0) + 1
    
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in values.values())
    return entropy


def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    unique_values = set(row[attribute] for row in data)
    weighted_entropy = 0
    
    for value in unique_values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * calculate_entropy(subset, target_col)
    
    return total_entropy - weighted_entropy


def build_tree(data, attributes, target_col):
   
    target_values = [row[target_col] for row in data]
    if len(set(target_values)) == 1:
        return target_values[0] 
    
    if not attributes:
        return max(set(target_values), key=target_values.count)  
    
    gains = {attr: calculate_information_gain(data, attr, target_col) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    
    tree = {best_attr: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attr]
    
    unique_values = set(row[best_attr] for row in data)
    for value in unique_values:
        subset = [row for row in data if row[best_attr] == value]
        tree[best_attr][value] = build_tree(subset, remaining_attributes, target_col)
    
    return tree
def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree  
    
    root = next(iter(tree))
    value = data_point[root]
    return predict(tree[root][value], data_point) if value in tree[root] else None

data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play?': 'Yes'}
]

attributes = ['Weather', 'Temperature']
target_col = 'Play?'
decision_tree = build_tree(data, attributes, target_col)
print("Decision Tree:", decision_tree)
test_data = {'Weather': 'Sunny', 'Temperature': 'Hot'}
prediction = predict(decision_tree, test_data)
print("Prediction for test data:", prediction)

