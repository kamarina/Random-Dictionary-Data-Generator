import json
import random


# Function that generates random flight costs based on a defined list of cities
def random_flight_costs(cities):
    # Initialize a dictionary to store generated flight costs
    flight_costs = {}

    # Iterate over departure cities
    for departure in cities:
        # Initialize a nested dictionary for every departure city on the cities list
        flight_costs[departure] = {}

        # Iterate over destination cities
        for destination in cities:
            # Ensure the  destination city doesn't equal the departure city
            if departure != destination:
                # Randomize fright cost in a range from 300 and 1200
                flight_costs[departure][destination] = random.randint(300, 1200)

    # Return the flight costs dictionary
    return flight_costs


# List of cities (can be modified)
cities = ["New York", "Los Angeles", "Paris", "Tokyo", "London", "Sydney", "London", "Dubai", "Ankara", "Delhi",
          "Shanghai", "São Paulo", "Mumbai", "Beijing", "Cairo", "Dhaka", "Mexico City", "Osaka", "Karachi",
          "Chongqing", "Birmingham",
          "Istanbul", "Kolkata", "Lahore", "Shenzhen", "Mumbai", "Kinshasa", "Tianjin", "Lima", "Mumbai", "Bangkok",
          "Kyiv", "Berlin", "Toronto", "Budapest", "Leuven", "Dublin"]

# Generate the flight costs for the list of the cities declared
flight_costs = random_flight_costs(cities)

# Save generated data to an output file
filename = "flight_costs.json"
with open(filename, 'w') as file:
    json.dump(flight_costs, file, indent=2)

print("Randomized flight costs have been saved to 'flight_costs.json'")
