from geopy.geocoders import Nominatim

def get_countries(lat,lon):
    coordinates = f'{lat} {lon}'
    locator = Nominatim(user_agent='myencoder', timeout=10)
    location = locator.reverse(coordinates,language='en')
    country = location.raw['address']['country_code'].upper()
    return [country,lat,lon]

get_countries(32.782023,35.478867)


#Step 1: get 10 stocks related to the bubble 
#Step 2: Get the correlations between all of them from 1999 to 2000 and 2000 to 2001
#Step 3: Study the difference