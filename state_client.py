import requests


def get_user_coords():
    longitude = input("\nPlease enter a longitude:  ")
    latitude = input("\nPlease enter a latitude:  ")
    # ERROR CHECK LAT AND LONG SOMEWHERE IN HERE ********
    user_coords = {
        'longitude': float(longitude),
        'latitude': float(latitude)
    }

    r = requests.post('http://127.0.0.1:8080', json = user_coords)
    # print(r.text)


get_user_coords()



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




# r = requests.post("http://yoururl/post", data={'foo': 'bar'})
# # And done.
# print(r.text) # displays the result body.


# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# response = requests.post('http://127.0.0.1:8080/', data = user_coords)
# print(response.json())
# print (response.text)

# print ("state_data", state_data)
# session = requests.Session()
# response = session.post('http://127.0.0.1:8080/', data=user_coords)
# print ("response", response.text)













