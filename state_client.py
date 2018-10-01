import requests


"""
Procure longitude and latitude from the user 
and then submit the POST request
"""
def get_user_coords():
    longitude = input("\nPlease enter a longitude:  ")
    latitude = input("\nPlease enter a latitude:  ")
    user_coords = {
        'longitude': float(longitude),
        'latitude': float(latitude)
    }

    r = requests.post('http://127.0.0.1:8080', json = user_coords)
    print("\n", r.text)


get_user_coords()



