"""CSC111 Winter 2023 Course Project: Post COVID-19: An Interactive Travel Guide
This module plots the choropleth map displaying the danger index for each country.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the CSC111 instructors and
TAs at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 Alex Nguyen, Anson Lau, Daniel Kaloshi, Dua Hussain
"""
import json
import doctest
import pandas as pd
import plotly.express as px
import python_ta


def plot_map(file: str) -> None:
    """Plot a choropleth map of the countries in the world using the danger indexes from
    the given file.
    """
    with open('data/world.geo.json', encoding='utf-8') as data:
        world_countries = json.load(data)
    df = pd.read_csv(file)

    map_id = {}
    for feature in world_countries['features']:
        feature['id'] = feature['properties']['adm0_a3_us']
        map_id[feature['properties']['name_long']] = feature['id']

    df['id'] = df['country'].apply(lambda country: map_id[country])

    fig = px.choropleth_mapbox(df, geojson=world_countries, locations='id', color='danger_index',
                               color_continuous_scale=px.colors.diverging.RdYlGn_r,
                               range_color=(0, 4),
                               mapbox_style='carto-positron',
                               zoom=3, center={'lat': 37.0902, 'lon': -95.7129},
                               title='World Danger Indexes',
                               opacity=0.5,
                               )
    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    fig.show()


if __name__ == '__main__':
    plot_map('data/country-danger-index.csv')
    doctest.testmod()
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120,
        'disable': ['E9999', 'E9998', 'too-many-nested-blocks', 'R0912', 'R0915', 'E9970', 'R1732']
    })
