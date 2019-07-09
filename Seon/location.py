from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Abdullah_Alfarrarjeh_app")

location = geolocator.geocode("숭실대학교", addressdetails=True)

print(location.address)
print((location.latitude, location.longitude))
print(location.raw)


location = geolocator.reverse("52.509669, 13.376294", addressdetails=True)

print(location.address)
print(location.raw)

#print specific part of the address
print(location.raw['address']['city'])