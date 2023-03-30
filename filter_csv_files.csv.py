"""
This file is for filtering the four datasets, WHO-COVID-19-global-data, COVID-19-data-from-2023-02-01.csv, routes.csv
and airports.csv
"""

import csv
from datetime import datetime


def csv_airports_dict(file: str) -> dict[str, list[str]]:
    """
    This Takes the airports.csv and returns a dict with key values of countries in the file
    and then the associated value is the airports within that country

    :param file:
    :return:
    """
    # Accumalator Dict
    dict_so_far = {}

    # Opens airport.csv
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            # country name
            country = row[3]
            # associated airport code
            airports = row[4]

            # Checks if country is already in accumaltor to not get duplicates
            if country not in dict_so_far:
                dict_so_far[country] = [airports]
            # By this point, country should be in accumalator and should add assosiated
            # airport code to country in dict
            else:
                assert country in dict_so_far
                dict_so_far[country].append(airports)
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

            non_un_list = ['American Samoa', 'Anguilla', 'Aruba', 'Bermuda', 'Bonaire', 'British Virgin Islands',
                           'Cayman Islands', 'Cook Islands', 'Curaçao', 'Falkland Islands', 'Faroe Islands',
                           'French Guiana', 'French Polynesia', 'Gibraltar', 'Greenland', 'Guadeloupe', 'Guam',
                           'Guernsey',
                           'Holy See', 'Isle of Man', 'Jersey', 'Kosovo[1]', 'Martinique', 'Mayotte', 'Montserrat',
                           'New Caledonia', 'Niue', 'Northern Mariana Islands (Commonwealth of the)',
                           'occupied Palestinian territory, including east Jerusalem', 'Other', 'Pitcairn Islands',
                           'Puerto Rico', 'Réunion', 'Saba', 'Saint Barthélemy',
                           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Martin',
                           'Saint Pierre and Miquelon',
                           'Sint Eustatius', 'Sint Maarten', 'Tokelau', 'Turks and Caicos Islands',
                           'United States Virgin Islands', 'Wallis and Futuna']

            special_codes = ['CW', 'BL', 'RE']

            first_date = datetime(2023, 2, 1).date()
            writer.writerows(row for row in reader if datetime.strptime(row[0], '%Y-%m-%d').date() >= first_date and
                             row[2] not in non_un_list and row[1] not in special_codes)


if __name__ == '__main__':
    filter_csv_file('data/WHO-COVID-19-global-data.csv')
