"""CSC111 Winter 2023 Course Project: Post COVID-19: An Interactive Travel Guide
This module filters the four datasets, WHO-COVID-19-global-data, COVID-19-data-from-2023-02-01.csv,
routes.csv and airports.csv.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the CSC111 instructors and
TAs at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 Alex Nguyen, Anson Lau, Daniel Kaloshi, Dua Hussain
"""
import csv
from datetime import datetime
import doctest
import python_ta


def capitalize(output_file='data/un_population_capitalized') -> None:
    """ Capatalizes file filter_un_populations for user interaction file """
    with open('data/filter_un_populations.csv', mode='r') as main_file:
        reader = csv.reader(main_file)
        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')
            for row in reader:
                row1 = row[0].upper()
                row2 = row[1]
                row3 = [row1, row2]
                writer.writerow(row3)


def capitalize2(output_file='data/covid19_capitalized') -> None:
    """ Capatalizes file COVID 19 for user interaction file """
    with open('data/COVID-19-data-from-2023-02-01.csv', mode='r') as main_file:
        reader = csv.reader(main_file)
        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')
            for row in reader:
                row1 = [row[0], row[1], row[2].upper(), row[3], row[4], row[5], row[6], row[7]]
                writer.writerow(row1)


def csv_airports_dict(file: str) -> dict[str, list[str]]:
    """
    This Takes the airports.csv and returns a dict with key values of countries in the file
    and then the associated value is the airports within that country

    This dict will be used in new_csv function

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


def new_csv(country_dict: dict[str, list[tuple[str, str]]], output_file='data/new_routes_with_countries') -> None:
    """
    Outputs a new file by reading airports.csv, so instead of routes being in terms of airport codes it is in
    terms of countries

    """
    # Opens file to read
    with open('data/airports.csv', mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)
        # opens output file to write in
        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')
            for row in reader:
                source = row[2]
                dest = row[4]
                source_country = ''
                dest_country = ''
                # iterates through the dictionary to assign values to source and dest only if they are in the input dict
                for k, v_list in country_dict.items():
                    for airport in v_list:
                        if airport == source:
                            source_country = k
                        elif airport == dest:
                            dest_country = k

                # Only allows rows that consist of both source and dest and thatg they are not the same
                if source_country == dest_country:
                    pass
                elif source_country == '' and dest_country != '':
                    pass
                elif dest_country == '' and source_country != '':
                    pass
                else:
                    row_to_write = [source_country, dest_country]
                    writer.writerow(row_to_write)


def country_list_un() -> list[str]:
    """ A Function to output all countries in data_file un_populations"""
    # Accumalator
    lst_so_far = []
    with open('data/filter_un_populations.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] not in lst_so_far:
                lst_so_far.append(row[0].upper())
    return lst_so_far


def filter_covid(filename: str, output_file='data/COVID-19-data-from-2023-02-01.csv') -> None:
    """Read the data in filename, and write the data - filtered by the starting date of
    2023-02-01 up to the latest date - onto the output_file.

    """
    with open(filename, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',', lineterminator="\n")

            non_un_list = ['American Samoa', 'Anguilla', 'Aruba', 'Bermuda', 'Bonaire', 'British Virgin Islands',
                           'Cayman Islands', 'Cook Islands', 'Curaçao', 'Falkland Islands (Malvinas)', 'Faroe Islands',
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

            for row in reader:
                first_date = datetime(2023, 2, 1).date()
                if datetime.strptime(row[0], '%Y-%m-%d').date() >= first_date and row[2] \
                        not in non_un_list and row[1] not in special_codes:
                    if row[1] == 'TR':
                        row[2] = 'Turkiye'
                    elif row[1] == 'CI':
                        row[2] = 'Cote d\'Ivoire'

                    writer.writerow(row)


if __name__ == '__main__':
    filter_covid('data/WHO-COVID-19-global-data.csv')


def filter_routes(filename: str, output_file='data/new_routes_2.0') -> None:
    """Read the data in filename, and write the data - filtered by the starting date of
    2023-02-01 up to the latest date - onto the output_file.

    This function is used to correct naming convention for all files to follow one single convention since the datasets
    all follow different naming style
    """
    with open(filename, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',', lineterminator="\n")

            non_un_list = ['American Samoa', 'Anguilla', 'Aruba', 'Bermuda', 'Bonaire',
                           'British Virgin Islands',
                           'Cayman Islands', 'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Curaçao',
                           'Falkland Islands', 'Falkland Islands (Malvinas)', 'Faroe Islands',
                           'French Guiana', 'French Polynesia', 'Gibraltar', 'Greenland', 'Guadeloupe',
                           'Guam',
                           'Guernsey', 'Holy See', 'Hong Kong', 'Isle of Man', 'Jersey', 'Macau',
                           'Kosovo[1]',
                           'Martinique',
                           'Mayotte', 'Montserrat', 'Netherlands Antilles', 'New Caledonia', 'Niue', 'Norfolk Island',
                           'Northern Mariana Islands (Commonwealth of the)', 'Northern Mariana Islands',
                           'occupied Palestinian territory, including east Jerusalem',
                           'Other', 'Pitcairn Islands',
                           'Puerto Rico', 'Réunion', 'Saba', 'Saint Barthélemy',
                           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Martin',
                           'Saint Pierre and Miquelon',
                           'Sint Eustatius', 'Sint Maarten', 'Taiwan', 'Tokelau',
                           'Turks and Caicos Islands',
                           'United States Virgin Islands', 'Virgin Islands', 'Wallis and Futuna', 'Western Sahara']

            rows_so_far = []

            for row in reader:

                if row[0] == 'United Kingdom':
                    row[0] = 'The United Kingdom'
                if row[1] == 'United Kingdom':
                    row[1] = 'The United Kingdom'
                if row[0] == 'Turkey':
                    row[0] = 'Turkiye'
                if row[1] == 'Turkey':
                    row[1] = 'Turkiye'
                if row[0] == 'United States':
                    row[0] = 'United States of America'
                if row[1] == 'United States':
                    row[1] = 'United States of America'
                if row[0] == 'Venezuela':
                    row[0] = 'Venezuela (Bolivarian Republic of)'
                if row[1] == 'Venezuela':
                    row[1] = 'Venezuela (Bolivarian Republic of)'
                if row[0] == 'Tanzania':
                    row[0] = 'United Republic of Tanzania'
                if row[1] == 'Tanzania':
                    row[1] = 'United Republic of Tanzania'
                if row[0] == 'Syria':
                    row[0] = 'Syrian Arab Republic'
                if row[1] == 'Syria':
                    row[1] = 'Syrian Arab Republic'
                if row[0] == 'South Korea':
                    row[0] = 'Republic of Korea'
                if row[1] == 'South Korea':
                    row[1] = 'Republic of Korea'
                if row[0] == 'North Korea':
                    row[0] = 'Democratic People\'s Republic of Korea'
                if row[1] == 'North Korea':
                    row[1] = 'Democratic People\'s Republic of Korea'
                if row[0] == 'Moldova':
                    row[0] = 'Republic of Moldova'
                if row[1] == 'Moldova':
                    row[1] = 'Republic of Moldova'
                if row[0] == 'Micronesia':
                    row[0] = 'Micronesia (Federated States of)'
                if row[1] == 'Micronesia':
                    row[1] = 'Micronesia (Federated States of)'
                if row[0] == 'Laos':
                    row[0] = 'Lao People\'s Democratic Republic'
                if row[1] == 'Laos':
                    row[1] = 'Lao People\'s Democratic Republic'
                if row[0] == 'Iran':
                    row[0] = 'Iran (Islamic Republic of)'
                if row[1] == 'Iran':
                    row[1] = 'Iran (Islamic Republic of)'
                if row[0] == 'Vietnam':
                    row[0] = 'Viet Nam'
                if row[1] == 'Vietnam':
                    row[1] = 'Viet Nam'
                if row[0] == 'Russia':
                    row[0] = 'Russian Federation'
                if row[1] == 'Russia':
                    row[1] = 'Russian Federation'
                if row[0] == 'Bolivia':
                    row[0] = 'Bolivia (Plurinational State of)'
                if row[1] == 'Bolivia':
                    row[1] = 'Bolivia (Plurinational State of)'
                if row[0] == 'Cape Verde':
                    row[0] = 'Cabo Verde'
                if row[1] == 'Cape Verde':
                    row[1] = 'Cabo Verde'
                if row[0] == 'Congo (Brazzaville)':
                    row[0] = 'Congo'
                if row[1] == 'Congo (Brazzaville)':
                    row[1] = 'Congo'
                if row[0] == 'Congo (Kinshasa)':
                    row[0] = 'Democratic Republic of the Congo'
                if row[1] == 'Congo (Kinshasa)':
                    row[1] = 'Democratic Republic of the Congo'
                if row[0] == 'Brunei':
                    row[0] = 'Brunei Darussalam'
                if row[1] == 'Brunei':
                    row[1] = 'Brunei Darussalam'
                if row[0] == 'Czech Republic':
                    row[0] = 'Czechia'
                if row[1] == 'Czech Republic':
                    row[1] = 'Czechia'
                if row[0] == 'East Timor':
                    row[0] = 'Timor-Leste'
                if row[1] == 'East Timor':
                    row[1] = 'Timor-Leste'
                if row[0] == 'Burma':
                    row[0] = 'Myanmar'
                if row[1] == 'Burma':
                    row[1] = 'Myanmar'

                if row[0] not in non_un_list and row[1] not in non_un_list and row not in rows_so_far:
                    writer.writerow(row)
                    rows_so_far.append(row)


if __name__ == '__main__':
    filter_routes('data/new_routes_with_countries')


def capitalize3(file: str, output_file='data/new_routes_capitalized') -> None:
    """ Capatalizes file new_routes_2.0 for user interaction file """
    with open(file, mode='r') as main_file:
        reader = csv.reader(main_file)
        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',', lineterminator="\n")
            for row in reader:
                row1 = [row[0].upper(), row[1].upper()]
                writer.writerow(row1)


if __name__ == '__main__':
    capitalize3('data/new_routes_2.0')

if __name__ == '__main__':
    doctest.testmod()
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120,
        'disable': ['E9999', 'E9998', 'too-many-nested-blocks', 'R0912', 'R0915', 'E9970']
    })
