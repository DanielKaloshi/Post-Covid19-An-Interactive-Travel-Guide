from __future__ import annotations
import csv
import compute_stats


class _Country:
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
    neighbours: dict[str, _Country]
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

    def check_connected(self, target_country: str, visited: set[_Country]) -> bool:
        """Return whether this country is connected to a country corresponding to the target_country,
        WITHOUT using any of the countries in visited.

        Preconditions:
            - self not in visited
        """
        if self.name == target_country:
            return True
        else:
            visited.add(self)
            for neighbour in self.neighbours.values():
                if neighbour not in visited:
                    if neighbour.check_connected(target_country, visited):
                        return True
            return False

    def find_flights(self, destination: _Country, visited: set[_Country]) -> set[str]:

        """Return a set containing all the possible country paths from this country that do NOT use any countries in
        visited.

        Preconditions:
            - self not in visited
        """

        country_set = set()

        if self.name == destination.name:
            return {destination.name}
        else:
            visited.add(self)
            for neighbour in self.neighbours:
                if neighbour not in visited:
                    country_set.union(neighbour.find_flights(destination, visited))

        return country_set


class Flights:
    """A network representing the available flight paths around the world.

    Instance Attributes:
    - countries
        A collection of the countries connected by flights in this network.
        Maps the name to the Country object.

    Representation Invariants:
    - all(country == self.countries[country].name for country in self.countries)
    """
    countries: dict[str, _Country]

    def __init__(self) -> None:
        """Initialize an empty flight network."""
        self.countries = {}

    def add_country(self, name: str) -> None:
        """Add a country with the given name to this flight netowrk.

        The new country is not connected by a flight to any other countries.
        """
        self.countries[name] = _Country(name)

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
            return any(neighbour == country2 for neighbour in v1.neighbours)  # v1.neighbours are a dict of vertices of v1
        else:
            # We didn't find an existing vertex for both items.
            return False
