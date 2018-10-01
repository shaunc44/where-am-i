import json
from shapely.geometry import Polygon, Point
from flask import Flask, request


# Start Flask
app = Flask(__name__)
@app.route('/', methods=['POST'])


def result():
    if request.method == 'POST':
        user_coords = request.json
        # Convert longitude and latitude to shapely Point
        user_provided_coord = Point(
            user_coords['longitude'], 
            user_coords['latitude']
        )

        # Get state data from JSON file
        with open("states.json") as state_json:
            state_data = json.load(state_json)
            # Iterate over state data
            for state in state_data:
                # Create a polygon based on the border coordinates provided
                state_borders = Polygon(state['border'])
                # Check if coords are located within state's borders
                if state_borders.contains(user_provided_coord):
                    return state['state']
        # If coordinates not located within any of the state's 
        # polygonal borders return not found
        return "Provided coordinates not found"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



