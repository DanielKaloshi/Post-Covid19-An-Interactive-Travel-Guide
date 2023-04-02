""""""
import csv
import flights as f
import filter_file


def generate_flight_network(file: str) -> f.Flights():
    """ """
    flight = f.Flights()
    lst_of_countries = filter_file.country_list_UN()
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            source = row[0]
            dest = row[1]

            if source or dest not in filter_file:
                pass
            else:
                flight.add_flight(source, dest)

            flight.add_flight(source, dest)
    return flight
