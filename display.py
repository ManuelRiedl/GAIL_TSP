
from geopy import distance
import folium

def displaymap(cities):
    # create a list of tuples containing the latitude and longitude of each city
    locations = [(city[1], city[2]) for city in cities]

    # calculate the distance between each pair of cities
    distances = []
    for i in range(len(locations) - 1):
        dist = distance.distance(locations[i], locations[i + 1]).km
        distances.append(dist)

    # create a map of the cities using folium
    map = folium.Map(location=[cities[0][1], cities[0][2]], zoom_start=3)

    # add markers for each city to the map
    for city in cities:
        folium.Marker(location=[city[1], city[2]], popup=city[0]).add_to(map)

    # add a line connecting the cities to the map
    folium.PolyLine(locations=locations, weight=5, color='blue').add_to(map)

    # display the map
    map.