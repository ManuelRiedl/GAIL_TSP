import csv

from geopy.geocoders import Nominatim

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cities = {}
    geolocator = Nominatim(user_agent="Cities")

    with open('./european_cities.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            name = row[0]
            cities[name] = (row[1], row[2])

print(cities['Paris'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
