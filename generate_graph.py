""""""
import csv
import flights as f
import filter_file
import python_ta

def generate_flight_network(file: str) -> f.Flights():
    """ """
    flight = f.Flights()
    lst_of_countries = filter_file.country_list_UN()
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            source = row[0]
            dest = row[1]
            if source not in lst_of_countries or dest not in lst_of_countries:
                pass
            else:
                flight.add_flight(source, dest)
    return flight

if __name__ == '__main__':
    # g = generate_flight_network('data/new_routes_cap')
    # c = g.countries['CANADA']
    # b = g.countries['BURUNDI']
    # bel = g.countries['BELGIUM']
