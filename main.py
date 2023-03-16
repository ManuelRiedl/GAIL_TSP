import csv
from geopy.geocoders import Nominatim

if __name__ == '__main__':
    cities = []
    # geolocator = Nominatim(user_agent="Cities")

    with open('./european_cities.csv', 'r') as csvfile:
        # skip header
        csvfile.readline()
        for row in csv.reader(csvfile, delimiter=','):
            cities.append([row[0], float(row[1]), float(row[2])])

print(cities)
