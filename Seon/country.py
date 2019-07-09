import time
from geopy.geocoders import Nominatim

from collections import OrderedDict
import operator

from geopy.exc import GeocoderTimedOut

import matplotlib.pyplot as plt

import csv

geolocator = Nominatim(user_agent="Abdullah_Alfarrarjeh_app")

def do_reverse_geocode(address):
    try:
        return geolocator.reverse(address)
    except GeocoderTimedOut:
        return do_reverse_geocode(address)

count = 0
         
f_input= open("tweet_input.csv",encoding="utf8")

final_dictionary = {}

lines = [x.strip() for x in f_input.readlines()]
for line in lines:
    count+=1
    
    #first line is a headerline. Skip intentionally.
    if count == 1:    
        continue
    
    lineTokens = line.split(',')
    latitude = lineTokens[3]
    longitude = lineTokens[4]
    
    location = do_reverse_geocode(latitude + "," + longitude)
    
    county = location.raw['address']['county']   
    print(latitude + "\t" + longitude + "\t" + county)
    
    if county not in final_dictionary:
        final_dictionary[county] = 1
    else:
        final_dictionary[county] = final_dictionary[county] + 1
                    
    # Wait for 300 milliseconds
    time.sleep(0.300)
    
sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)

f_input.close()


with open('GeoRegionCount.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    
    my_writer.writerow(['GeoRegion', 'Count'])
    
    for key in sorted_d:
        current_RegionName = str(key[0])
        current_Count = int(key[1])
        
        my_writer.writerow([current_RegionName, current_Count])

plt.figure(figsize=(25, 3))
plt.title('Spatial Distribution of Tweets')
plt.xlabel('Counties')
plt.ylabel('# of Tweets per county')
plt.bar(final_dictionary.keys(), final_dictionary.values(), width=0.3, color='g')

plt.show()