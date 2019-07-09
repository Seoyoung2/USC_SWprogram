import gmaps
import gmaps.datasets
gmaps.configure(api_key='AIzaSyBK_VVErgwa6zmC-u9f2MZB17s_qqgePZo')# Fill in with your API key
import pandas as pd

#print(gmaps.datasets.list_datasets())
# Get the dataset
#earthquake_df = gmaps.datasets.load_dataset_as_df('taxi_rides')
#earthquake_df = gmaps.datasets.load_dataset_as_df('taxi_rides')
#Get the locations from the data set
#locations = earthquake_df[['latitude', 'longitude']]

locations = []

my_filtered_csv = pd.read_csv("C:/Users/CEO/Desktop/USC/tweet_input.csv", usecols=['latitude', 'longitude'])


#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(my_filtered_csv))
fig