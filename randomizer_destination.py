import json
import random


# Function to generate random flight costs for a given list of cities
def generate_flight_costs(cities):
    # Initialize an empty dictionary to store flight costs
    flight_costs = {}

    # Iterate over each departure city
    for departure_city in cities:
        # Initialize a nested dictionary for each departure city
        flight_costs[departure_city] = {}

        # Iterate over each destination city
        for destination_city in cities:
            # Ensure the departure and destination cities are different
            if departure_city != destination_city:
                # Assign a random flight cost between 300 and 1000
                flight_costs[departure_city][destination_city] = random.randint(300, 1000)

    # Return the generated flight costs dictionary
    return flight_costs


# List of cities (you can add more as needed)
cities = ["New York", "Los Angeles", "Paris", "Tokyo", "London", "Sydney", "London", "Dubai", "Ankara", "Delhi",
          "Shanghai", "São Paulo", "Mumbai", "Beijing", "Cairo", "Dhaka", "Mexico City", "Osaka", "Karachi",
          "Chongqing",
          "Istanbul", "Kolkata", "Lahore", "Shenzhen", "Mumbai", "Kinshasa", "Tianjin", "Lima", "Mumbai", "Bangkok",
          "Kyiv", "Berlin", "Toronto", "Budapest", "Leuven", "Dublin"]

# Generate random flight costs for the given list of cities
flight_costs = generate_flight_costs(cities)

# Save flight costs to a file
filename = "flight_costs.json"
with open(filename, 'w') as file:
    json.dump(flight_costs, file, indent=2)

print("Flight costs have been saved to 'flight_costs.json'")
