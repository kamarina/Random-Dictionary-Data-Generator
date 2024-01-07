import json
import random

def generate_random_data(items):
    # Initialize an empty dictionary to store random data
    random_data = {}

    # Iterate over each item
    for item in items:
        # Initialize a nested dictionary for each item
        random_data[item] = {}

        # Iterate over each related item
        for related_item in items:
            # Ensure the item and related_item are different
            if item != related_item:
                # Assign a random value (you can customize this based on your needs)
                random_data[item][related_item] = random.randint(300, 1000)

    # Return the generated random data dictionary
    return random_data

# List of items (you can add more as needed)
items_list = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"]

# Generate random data for the given list of items
random_data = generate_random_data(items_list)

# Save random data to a file
filename = "random_data.json"
with open(filename, 'w') as file:
    json.dump(random_data, file, indent=2)

print(f"Random data have been saved to '{filename}'")
