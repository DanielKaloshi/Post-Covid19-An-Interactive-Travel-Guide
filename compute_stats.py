"""CSC111 Winter 2023 Course Project: Post COVID-19: An Interactive Travel Guide
This module computes statistics for plotting the map as well as computing the danger index.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the CSC111 instructors and
TAs at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 Alex Nguyen, Anson Lau, Daniel Kaloshi, Dua Hussain
"""
import csv
import python_ta


def compute_num_infections(country_name: str) -> int:
    """ Computes the number of infections for each country.

    >>> compute_num_infections('France')
    170995

    >>> compute_num_infections('Canada')
    58713

    >>> compute_num_infections('Japan')
    851190

    """

    cases_so_far = 0

    with open('data/covid19_capitalized') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[2] == country_name:
                cases_so_far += int(row[4])

    return cases_so_far


def compute_population(country_name: str) -> int:
    """ Computes the population of each country.

    >>> compute_population('France')
    64626628

    >>> compute_population('Canada')
    38454327

    >>> compute_population('Japan')
    123951692
    """

    population = 1

    with open('data/un_population_capitalized') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            if row[0] == country_name:
                population = int(row[1])
                assert population > 0
                break

    return population


def compute_num_deaths(country_name: str) -> int:
    """ Computes the number of deaths for each country.

    >>> compute_num_deaths('France')
    1061

    >>> compute_num_deaths('Canada')
    1060

    >>> compute_num_deaths('Japan')
    5428
    """

    deaths_so_far = 0

    with open('data/covid19_capitalized') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[2] == country_name:
                deaths_so_far += int(row[6])

    return deaths_so_far


def compute_infection_rate_per(country_name: str) -> float:
    """ Computes the infection rate per 1000 people for each country.

    >>> compute_infection_rate_per('France')
    2.64589079287875

    >>> compute_infection_rate_per('Canada')
    1.5268242764981947

    >>> compute_infection_rate_per('Japan')
    6.86711077731799

    >>> compute_infection_rate_per('Bangladesh')
    0.002284060322278458

    >>> compute_infection_rate_per('Albania')
    0.14037823314115472
    """

    cases = compute_num_infections(country_name)
    population = compute_population(country_name)

    assert population > 0

    return (cases / population) * 1000


def compute_death_rate_per(country_name: str) -> float:
    """ Computes the death rate per 100 cases for each country.

    >>> compute_death_rate_per('France')
    0.6204859791221966

    >>> compute_death_rate_per('Canada')
    1.8053923321921892

    >>> compute_death_rate_per('Japan')
    0.6376954616478107

    >>> compute_death_rate_per('Bangladesh')
    0.7672634271099744

    >>> compute_death_rate_per('Albania')
    1.0025062656641603
    """

    cases = compute_num_infections(country_name)
    deaths = compute_num_deaths(country_name)

    if cases == 0:
        return 0.0
    else:
        return (deaths / cases) * 100


def compute_danger_index(country_name: str) -> float:
    """ Computes the 'danger index' for each country by averaging out the infection rate and the death rate.

    >>> compute_danger_index('France')
    1.6331883860004732

    >>> compute_danger_index('Canada')
    1.666108304345192

    >>> compute_danger_index('Japan')
    3.7524031194829

    >>> compute_danger_index('Bangladesh')
    0.38477374371612644

    >>> compute_danger_index('Albania')
    0.5714422494026575
    """

    infection_rate = compute_infection_rate_per(country_name)
    death_rate = compute_death_rate_per(country_name)

    return (infection_rate + death_rate) / 2


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120,
        'disable': ['E9999', 'E9998', 'too-many-nested-blocks', 'R0912', 'R0915', 'E9970']
    })
