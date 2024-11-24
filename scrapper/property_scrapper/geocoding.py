import googlemaps
import os
import json


# Load your API key from a secure location
API_KEY = "AIzaSyCiRfij5vw6SLLbocakpTrhrEYYBJ-UIQw"

def geocode_address(address):
    try:
        # Initialize the Google Maps client
        gmaps = googlemaps.Client(key=API_KEY)

        # Geocode the address
        geocode_result = gmaps.geocode(address)

        # Check if any results were returned
        if geocode_result:
            # Extract latitude and longitude
            location = geocode_result[0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']

            return {'lat': lat, 'lng': lng}
        else:
            return {'error': 'No results found'}

    except Exception as e:
        return {'error': str(e)}


# Define the directories where JSON files are located
directories = ["./for-sale", "./to-rent"]

for directory in directories:
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)

                # Load the JSON data from the file
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)

                # Process each property in the JSON data
                for id, property_details in data.items():
                    address = property_details.get('address')
                    if address:
                        result = geocode_address(address)
                        if 'error' not in result:
                            property_details['coordinates'] = result

                # Save the updated data back to the file
                with open(file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                print(f'Processed: {os.path.normpath(file_path)}')
