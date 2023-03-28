def compute_country_num_infections(country_name: str) -> int:
    """ Computes the number of infections for each country.
    """

    cases_so_far = 0

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[2] == country_name:
                cases_so_far += int(row[4])

    return cases_so_far


def compute_country_population(country_name: str) -> int:
    """ Computes the population of each country.
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


def compute_country_num_deaths(country_name: str) -> int:
    """ Computes the number of deaths for each country.
    """

    deaths_so_far = 0

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[2] == country_name:
                deaths_so_far += int(row[6])

    return deaths_so_far


def compute_country_infection_rate_per_1000(country_name: str) -> float:
    """ Computes the infection rate per 1000 people for each country.
    """

    cases = compute_num_infections(country_name)
    population = compute_population(country_name)

    return (cases / population) * 1000


def compute_country_death_rate_per_1000(country_name: str) -> float:
    """ Computes the death rate per 1000 people for each country.
    """

    cases = compute_num_infections(country_name)
    deaths = compute_num_deaths(country_name)

    return (deaths_so_far / cases_so_far) * 1000


def compute_country_safety_index(country_name: str) -> float:
    """ Computes the 'safety index' for each country by averaging out the infection rate and the death rate.
    """

    infection_rate = compute_infection_rate_per_1000(country_name)
    death_rate = compute_death_rate(country_name)

    return (infection_rate + death_rate) / 2


def compute_region_infection_rate_per_1000(region_name: str) -> float:
    """ Computes the infection rate per 1000 people for each region.
    """

    cases_so_far = 0
    population_so_far = 0

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[3] == region_name:
                cases_so_far += int(row[4])
                population_so_far += compute_country_population(row[2])

    return (cases_so_far / population_so_far) * 1000


def compute_region_death_rate_per_1000(region_name: str) -> float:
    """ Computes the death rate per 1000 people for each region.
    """

    cases_so_far = 0
    deaths_so_far = 0

    with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[3] == region_name:
                cases_so_far += int(row[4])
                deaths_so_far += int(row[6])

    return (deaths_so_far / cases_so_far) * 1000


def compute_region_safety_index(region_name: str) -> float:
    """ Computes the 'safety index' for each region by averaging out the infection rate and the death rate.
    """

    infection_rate = compute_region_infection_rate_per_1000(region_name)
    death_rate = compute_region_death_rate_per_1000(region_name)

    return (infection_rate + death_rate) / 2
