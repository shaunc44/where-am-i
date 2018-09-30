import requests
import json
import ast

from shapely.geometry import Polygon, Point
from flask import Flask, request


# Start Flask server
app = Flask(__name__)
@app.route('/', methods=['POST'])


# def get_state_data():
#     with open("states.json") as state_json:
#         state_data = json.load(state_json)
#         return state_data


def result():
    if request.method == 'POST':
        # state_data = get_state_data()
        user_coords = request.json

        # print ("longitude", user_coords['longitude'])
        # print ("latitude", user_coords['latitude'])
        provided_coord = Point(
            user_coords['longitude'], 
            user_coords['latitude']
        )

        with open("states.json") as state_json:
            state_data = json.load(state_json)

            for state in state_data:
                # Create a polygon based on the border coordinates provided
                state_borders = Polygon(state['border'])

                if state_borders.contains(provided_coord):
                    # print (
                    #     "\nThat longitude & latitude is located in: ", 
                    #     state['state']
                    # )
                    print (state['state'])
                    return state['state']
        # print ("user_coords:", user_coords)
        # return 'Received!' # response to your request.
        print ("Provided coordinates not found")
        return "Provided coordinates not found"
        # return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
# app.run()






# def get_user_coords():
#     longitude = input("\nPlease enter a longitude:  ")
#     latitude = input("\nPlease enter a latitude:  ")
#     # ERROR CHECK LAT AND LONG SOMEWHERE IN HERE ********
#     user_coords = {
#         'longitude': float(longitude),
#         'latitude': float(latitude)
#     }
#     return user_coords





# def check_coords():
#     user_coords = get_user_coords()
#     state_data = get_state_data()
#     provided_coord = Point(user_coords['longitude'], user_coords['latitude'])

#     for state in state_data:
#         # Create a polygon based on the border coordinates provided
#         state_borders = Polygon(state['border'])

#         if state_borders.contains(provided_coord):
#             print ("\nThat longitude and latitude is located in:  ", state['state'])
#             return state['state']
#     # return None
#     # return "Provided coordinates not found"
#     print ("\nProvided coordinates not found")
#     return None


# check_coords()






    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # response = requests.post('http://127.0.0.1:8080/', data = user_coords)
    # print(response.json())
    # print (response.text)

    # print ("state_data", state_data)
    # session = requests.Session()
    # response = session.post('http://127.0.0.1:8080/', data=user_coords)
    # print ("response", response.text)

