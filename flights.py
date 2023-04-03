""" CSC111 Winter 2023 Course Project: Post COVID-19: An Interactive Travel Guide
This module contains our base Country and Flight classes as well as their associated methods.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the CSC111 instructors and
TAs at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 Alex Nguyen, Anson Lau, Daniel Kaloshi, Dua Hussain
"""
from __future__ import annotations
import csv
import math
import doctest
import python_ta
import compute_stats


class Country:
    """A vertex that represents a country in the flights network.

    Instance Attributes:
    - name:
        The name of this country.
    - neighbours:
        A mapping containing the neighbours of this country. A country is a neighbour if there
        is a direct flight between self and that country.
        Each key in the mapping is the name of a neighbouring country, and the corresponding
        value is the vertex associated with that country.
    - danger_index:
        The calculated danger index for this country.
    - region:
        The WHO region this country is located in.

    Representation Invariants:
    - self.name not in self.neighbours
    - all(self.name in country.neighbours for country in self.neighbours.values())
    """
    name: str
    neighbours: dict[str, Country]
    danger_index: float
    region: str

    def __init__(self, name: str) -> None:
        """Initialize this country with the given name, region, and neighbours."""
        self.name = name
        self.neighbours = {}
        self.danger_index = compute_stats.compute_danger_index(name)
        self.add_region()

    def add_region(self) -> None:
        """Add the WHO region that this country is located in."""
        with open('data/COVID-19-data-from-2023-02-01.csv') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[2] == self.name:
                    self.region = row[3]
                    break

    def check_connected(self, target_item: str, visited: set[Country]) -> bool:
        """Return whether this vertex is connected to a vertex
        corresponding to the target_item, WITHOUT using any the vertices in visited,

        Precondition:
          - self not in visited

        """
        if self.name == target_item:  # Base case
            return True

        else:
            visited.add(self)

            for u in self.neighbours:
                if self.neighbours[u] not in visited:
                    if self.neighbours[u].check_connected(target_item, visited):
                        return True

            return False


class Flights:
    """A network representing the available flight paths around the world.

    Instance Attributes:
    - countries
        A collection of the countries connected by flights in this network.
        Maps the name to the Country object.

    Representation Invariants:
    - all(country == self.countries[country].name for country in self.countries)
    """
    countries: dict[str, Country]

    def __init__(self) -> None:
        """Initialize an empty flight network."""
        self.countries = {}

    def add_country(self, name: str) -> None:
        """Add a country with the given name to this flight netowrk.

        The new country is not connected by a flight to any other countries.
        """
        self.countries[name] = Country(name)

    def add_flight(self, country1: str, country2: str) -> None:
        """Add a flight between the two countries with the given names in this flight network.

        Preconditions:
            - country1 != country2
        """
        if country1 not in self.countries:
            self.add_country(country1)
        if country2 not in self.countries:
            self.add_country(country2)

        f1 = self.countries[country1]
        f2 = self.countries[country2]

        f1.neighbours[country2] = f2
        f2.neighbours[country1] = f1

    def connected(self, country1: str, country2: str) -> bool:
        """Return whether country1 and country2 are countries connected.
        """
        if country1 in self.countries and country2 in self.countries:
            c1 = self.countries[country1]
            return c1.check_connected(country2, set())
        else:
            return False

    def adjacent(self, country1: str, country2: str) -> bool:
        """Return whether country1 is adjacent to country2 in this flights network

         In our domain context, if country1 is adjacent to country2,
         that means there is a direct flight between two countries.

        Return False if country1 and country2 do not appear as countries in this flight.
        """
        if country1 in self.countries and country2 in self.countries:
            v1 = self.countries[country1]
            return any(neighbour == country2 for neighbour in v1.neighbours)
        else:
            # We didn't find an existing vertex for both items.
            return False

    def generate_countries(self) -> list[str]:
        """Return a list of all countries in this flight network.

        """
        countries_so_far = []
        for country in self.countries:
            countries_so_far.append(country)

        return countries_so_far


def compute_safest_neighbour(neighbours: set[Country]) -> list[(str, float)]:
    """ Computes the danger index for each country in the set of neighbours returned by find_paths and returns
     a list of tuples containing the capitalzied country names of the Top 3 'safest' neighbours and their associated
     danger indexes (or Top 2 if neighbours is a set of length 2, Top 1 if neighbours has length 1, empty list if
     neighbours is an empty set).

    >>> c = Country('Canada')
    >>> f = Country('France')
    >>> j = Country('Japan')
    >>> compute_safest_neighbour({c, f, j})
    [('FRANCE', 1.6331883860004732), ('CANADA', 1.666108304345192), ('JAPAN', 3.7524031194829)]

    >>> al = Country('Albania')
    >>> af = Country('Afghanistan')
    >>> i = Country('Italy')
    >>> c = Country('Canada')
    >>> m = Country('Morocco')
    >>> compute_safest_neighbour({al, af, i, c, m})
    [('MOROCCO', 0.003964443242267447), ('ALBANIA', 0.5714422494026575), ('AFGHANISTAN', 0.5924590111707589)]

    >>> b = Country('Belarus')
    >>> uk = Country('The United Kingdom')
    >>> compute_safest_neighbour({b, uk})
    [('BELARUS', 0.0), ('THE UNITED KINGDOM', 2.237682350179056)]
    """

    top_three_so_far = []
    lowest_index_so_far = math.inf
    neighbour_so_far = ''
    set_neighbours = neighbours

    while len(top_three_so_far) < 3 and set_neighbours != set():
        for neighbour in set_neighbours:
            neighbour_index = compute_stats.compute_danger_index(neighbour.name)
            if neighbour_index < lowest_index_so_far:
                lowest_index_so_far = neighbour_index
                neighbour_so_far = neighbour

        top_three_so_far.append((str.upper(neighbour_so_far.name), lowest_index_so_far))
        set.remove(set_neighbours, neighbour_so_far)
        lowest_index_so_far = math.inf
        neighbour_so_far = ''

    return top_three_so_far


if __name__ == '__main__':
    doctest.testmod()
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120,
        'disable': ['E9999', 'E9998', 'too-many-nested-blocks']
    })
