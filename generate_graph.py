""""""
import csv
import flights as f

def generate_flight_network(file: str) -> f.Flights():
    """ """
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            source = row[0]
            dest = row[1]
