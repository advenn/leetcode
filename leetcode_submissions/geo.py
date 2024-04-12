from geopy.geocoders import Nominatim
from pprint import pprint

nom = Nominatim(user_agent="my_agent")

location = nom.reverse((41.278393, 69.290916))
pprint(location.raw)
