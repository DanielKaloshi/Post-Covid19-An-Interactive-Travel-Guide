""" A File dedicated to generating a complete flight network of all routes
Worked on by Dua Hussain
"""
import csv
import python_ta
import flights as f
import filter_file


def generate_flight_network(file: str) -> f.Flights():
    """ A function which generates a complete flight network of all routes from data_base new_routes_cap
    >>> net = generate_flight_network('data/new_routes_cap')
    >>> countries = net.countries
    >>> countries['CANADA']
    <flights.Country object at 0x10cc6e4d0>
    """
    # Creates an empty flight network
    flight = f.Flights()
    # Creates list of UN countries to make sure countries not in UN that are in new_routes_cap
    lst_of_countries = filter_file.country_list_un()
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            source = row[0]
            dest = row[1]
            # Only allows countries in the UN to be added to flight network
            if source not in lst_of_countries or dest not in lst_of_countries:
                pass
            else:
                flight.add_flight(source, dest)
    return flight

#
# if __name__ == '__main__':
#     # python_ta.check_all(config={
#     #     'extra-imports': [],  # the names (strs) of imported modules
#     #     'allowed-io': [],  # the names (strs) of functions that call print/open/input
#     #     'max-line-length': 120,
#     #     'disable': ['E9999', 'E9998']
#     # })
