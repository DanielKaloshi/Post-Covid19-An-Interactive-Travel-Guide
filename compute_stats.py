import csv
import math
from flights import Country


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

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
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

    population = 0

    with open('data/filter_world_population.csv') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            if row[0] == country_name:
                population = int(row[1])
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

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[2] == country_name:
                deaths_so_far += int(row[6])

    return deaths_so_far


def compute_infection_rate_per_1000(country_name: str) -> float:
    """ Computes the infection rate per 1000 people for each country.

    >>> compute_infection_rate_per_1000('France')
    2.64589079287875

    >>> compute_infection_rate_per_1000('Canada')
    1.5268242764981947

    >>> compute_infection_rate_per_1000('Japan')
    6.86711077731799
    """

    cases = compute_num_infections(country_name)
    population = compute_population(country_name)

    return (cases / population) * 1000


def compute_death_rate_per_1000(country_name: str) -> float:
    """ Computes the death rate per 1000 people for each country.

    >>> compute_death_rate_per_1000('France')
    6.204859791221965

    >>> compute_death_rate_per_1000('Canada')
    18.053923321921893

    >>> compute_death_rate_per_1000('Japan')
    6.376954616478107
    """

    cases = compute_num_infections(country_name)
    deaths = compute_num_deaths(country_name)

    return (deaths / cases) * 1000


def compute_safety_index(country_name: str) -> float:
    """ Computes the 'safety index' for each country by averaging out the infection rate and the death rate.

    >>> compute_safety_index('France')
    4.425375292050358

    >>> compute_safety_index('Canada')
    9.790373799210045

    >>> compute_safety_index('Japan')
    6.6220326968980485

    """

    infection_rate = compute_infection_rate_per_1000(country_name)
    death_rate = compute_death_rate_per_1000(country_name)

    return (infection_rate + death_rate) / 2


def compute_safest_neighbour(neighbours: set[str]) -> dict:
    """ Computes the safety index for each country in the set of neighbours returned by find_paths and returns
     a dictionary containing the Top 3 'safest' neighbours and their associated safety indexes.

    >>> compute_safest_neighbour({'Canada', 'France', 'Japan'})
    {'France': 4.425375292050358, 'Japan': 6.6220326968980485, 'Canada': 9.790373799210045}

    >>> compute_safest_neighbour({'Canada', 'Japan'})
    {'Japan': 6.6220326968980485, 'Canada': 9.790373799210045}

    >>> compute_safest_neighbour({'Albania', 'Afghanistan', 'Italy', 'Canada', 'Morocco'})
    {'Morocco': 0.003964443242267447, 'Albania': 5.082720444891379, 'Afghanistan': 5.801719919452148}

    """

    top_three_so_far = {}
    lowest_index_so_far = math.inf
    neighbour_so_far = ''
    set_neighbours = neighbours

    while len(top_three_so_far) < 3 and set_neighbours != set():
        for neighbour in set_neighbours:
            neighbour_index = compute_safety_index(neighbour)
            if neighbour_index < lowest_index_so_far:
                lowest_index_so_far = neighbour_index
                neighbour_so_far = neighbour

        top_three_so_far[neighbour_so_far] = lowest_index_so_far
        set.remove(set_neighbours, neighbour_so_far)
        lowest_index_so_far = math.inf
        neighbour_so_far = ''

    return top_three_so_far
