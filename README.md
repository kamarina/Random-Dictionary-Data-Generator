# RandomDictionaryDataGenerator

The **RandomDictionaryDataGenerator** script is designed to generate randomized dictionaries, facilitating the testing of program functionality by providing realistic but randomly generated data for testing programs and methods when no source data is available.

## How to Use

### Requirments
- Python installed on your system

### Usage

1. Clone the repository to your local machine:
```bash
   git clone https://github.com/your-username/RandomDictionaryDataGenerator.git
```
1. Navigate to the repository directory:
```bash
cd RandomDictionaryDataGenerator
```
2. Run the main script to generate random data:
```bash
python random_data_generator.py

```
This script allows you to generate randomized dictionaries for any list of items you provide. The generated data will be saved to a file named **'random_data.json'**.
# Example Implementation
To provide an example of implementation, consider the **'randomizer_destination.py'** file in the same repository:
``` python
import json
import random

# Function to generate random flight costs for a given list of cities
def generate_flight_costs(cities):
    # ... (code omitted for brevity) ...

# List of cities (you can add more as needed)
cities = ["New York", "Los Angeles", "Paris", "Tokyo", "London", ...]

# Generate random flight costs for the given list of cities
flight_costs = generate_flight_costs(cities)

# Save flight costs to a file
filename = "flight_costs.json"
with open(filename, 'w') as file:
    json.dump(flight_costs, file, indent=2)

print("Flight costs have been saved to 'flight_costs.json'")
```
# Sample Output
Here is a snippet of the **'randomizer_destination_OUTPUT.json'** from the same repository:
``` json
{
  "new york": {
    "los angeles": 498,
    "paris": 469,
    "tokyo": 440,
    "london": 997,
    "sydney": 359,
    "dubai": 336,
    ...
  },
  "los angeles": {
    "new york": 945,
    "paris": 499,
    "tokyo": 608,
    "london": 405,
    "sydney": 677,
    "dubai": 333,
    ...
  },
  ...
}
```
This output represents the randomized flight costs between different cities.

Feel free to customize and extend the code as needed for your specific use case.
``` javascript

Replace `your-username` with your actual GitHub username in the repository URL.

```
