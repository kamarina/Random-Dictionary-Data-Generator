import json
import random
from typing import List, Dict

def generate_data(items: List[str], min_value: int = 300, max_value: int = 900):
    # Create a dictionary nested dictionary with random values for related items
    data = {
        item: {
            related_item: random.randint(min_value, max_value)
            for related_item in items if item != related_item
        } for item in items
    }

    # Iterate over items
    for i in items:
        # Create a nested dictionary for items
        data[i] = {}

        # Iterate over related items
        for related_item in items:
            # Ensure  related_item is not the same as item
            if i != related_item:
                # Assign random values (the range and values are fully customizable)
                data[i][related_item] = random.randint(300, 900)

    # Return a dictionary with randomly generated content
    return data

# Create a list to store items that will serve as keys in your dictionaries
items_list = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"]

# Generate random contents for the items defined in a list
data = generate_data(items_list)

# Save generated data to a .json file
filename = "random.json"
try:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=3)
    print(f"Your generated data have been saved to '{filename}'")
except IOERROR as e:
    print(f"Failed to write data to {filename}: {e}")
