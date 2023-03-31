import csv
# import unidecode


def filter_csv_file(filename: str, output_file='data/new_routes_2.0'):
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
                           'Guernsey', 'Holy See', 'Hong Kong', 'Isle of Man', 'Jersey', 'Macau', 'Kosovo[1]',
                           'Martinique',
                           'Mayotte', 'Montserrat', 'Netherlands Antilles', 'New Caledonia', 'Niue',
                           'Northern Mariana Islands (Commonwealth of the)', 'Northern Mariana Islands'
                           'occupied Palestinian territory, including east Jerusalem', 'Other', 'Pitcairn Islands',
                           'Puerto Rico', 'Réunion', 'Saba', 'Saint Barthélemy',
                           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Martin',
                           'Saint Pierre and Miquelon',
                           'Sint Eustatius', 'Sint Maarten', 'Taiwan', 'Tokelau', 'Turks and Caicos Islands',
                           'United States Virgin Islands', 'Wallis and Futuna']

            curr_row = '', ''

            for row in reader:
                if row[0] not in non_un_list and row[1] not in non_un_list and curr_row != row:
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

                    writer.writerow(row)
                    curr_row = row


if __name__ == '__main__':
    filter_csv_file('data/new_routes_with_countries')
