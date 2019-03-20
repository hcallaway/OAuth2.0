from api_mashup import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "Q4ASFE3KFIPYJHCC23W5TF2XID0O5S5FVAGESNNK3VZR4QYG"
foursquare_client_secret = "JFJBSUZNUWRZ4C2DITCQITZNWKOCMQ3HNLP4JNBSAABR4XPT"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	latitude, longitude = getGeocodeLocation(location)
        print(latitude, longitude)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
        url = ("https://api.foursquare.com/v2/venues/search?ll={},{}&query=[{}]&client_id={}&client_secret={}&v=20190101".format(
            latitude, longitude, mealType, foursquare_client_id, foursquare_client_secret
            )
    )
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
    #3. Grab the first restaurant
        restaurant = result['response']['venues'][0]
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        pictureURL = ("https://api.foursquare.com/v2/venues/{}/photos?client_id={}&client_secret={}&v=20190101&".format(restaurant['id'], foursquare_client_id, foursquare_client_secret))
	#5. Grab the first image
        if pictureURL['response']['photos']['items']:
            image = pictureURL['response']['photos']['items'][0]
            imageURL = "{}300x300{}".format(image['prefix'],image['suffix'])
        else:
            imageURL = 'www.example.com/defaultimage.jpg'
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url
        restaurantDictionary = {}
        restaurantDictionary['name'] = restaurant['name']
        restaurantDictionary['address'] = restaurant['location']['address']
        restaurantDictionary['image_url'] = imageURL

        return restaurantDictionary

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	# findARestaurant("Tacos", "Jakarta, Indonesia")
	# findARestaurant("Tapas", "Maputo, Mozambique")
	# findARestaurant("Falafel", "Cairo, Egypt")
	# findARestaurant("Spaghetti", "New Delhi, India")
	# findARestaurant("Cappuccino", "Geneva, Switzerland")
	# findARestaurant("Sushi", "Los Angeles, California")
	# findARestaurant("Steak", "La Paz, Bolivia")
    #     findARestaurant("Gyros", "Sydney, Australia")