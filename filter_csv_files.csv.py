<<<<<<< HEAD
"""
This file is for filtering the three datasets, COVID-19-data-from-2023-02-01.csv
"""

import csv
from datetime import datetime


def csv_airports_dict(file: str) -> dict[str, list[str]]:
    """

    :param file:
    :return:
    """
    dict_so_far = {}
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            country = row[3]
            airports = row[4]
            if country not in dict_so_far:
                dict_so_far[country] = [airports]
            elif airports not in dict_so_far[country]:
                dict_so_far[country].append(airports)
            else:
                pass
    return dict_so_far


def test(file: str) -> None:
    """

    :param file:
    :return:
    """
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            assert len(row[2]) == 3 and len(row[4]) == 3


def new_csv(file: str, country_dict: dict[str, list[tuple[str, str]]], output_file='data/new_routes_with_countries'):
    """

    :param aiports:
    :param output_file:
    :return:
    """
    with open(file, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')
            for row in reader:
                source = row[2]
                dest = row[4]
                source_country = ''
                dest_country = ''
                for k, v_list in country_dict.items():
                    for airport in v_list:
                        if airport == source:
                            source_country = k
                        elif airport == dest:
                            dest_country = k

                if source_country == dest_country:
                    pass
                elif source_country == '' and dest_country != '':
                    pass
                elif dest_country == '' and source_country != '':
                    pass
                else:
                    row_to_write = [source_country, dest_country]
                    writer.writerow(row_to_write)


def filter_csv_file(filename: str, output_file='data/COVID-19-data-from-2023-02-01.csv'):
    """Read the data in filename, and write the data - filtered by the starting date of
    2023-02-01 up to the latest date - onto the output_file.

    """
    with open(filename, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')

            first_date = datetime(2023, 2, 1).date()
            writer.writerows(row for row in reader if datetime.strptime(row[0], '%Y-%m-%d').date() >= first_date)


if __name__ == '__main__':
    filter_csv_file('data/WHO-COVID-19-global-data.csv')
=======
# Dua
>>>>>>> 8bb22f09fc950d538b7426d5f5642c799aa9b854
