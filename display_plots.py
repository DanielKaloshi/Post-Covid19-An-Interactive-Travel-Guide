import json
import pandas as pd
import plotly.express as px

sample_data = 'data/sample_data_map.csv'  # for testing purposes
def plot_map(file: str) -> None:
    """Plot a choropleth map of the countries in the world using the safety indexes from
    the given file.
    """
    world_countries = json.load(open('data/world.geo.json'))
    df = pd.read_csv(file)

    map_id = {}
    for feature in world_countries['features']:
        feature['id'] = feature['properties']['woe_id']
        map_id[feature['properties']['name']] = feature['id']

    df['id'] = df['country'].apply(lambda country: map_id[country])

    fig = px.choropleth_mapbox(df, geojson=world_countries, locations='id', color='safety_index',
                               color_continuous_scale=px.colors.diverging.RdYlGn_r,
                               range_color=(0, 5),
                               mapbox_style='carto-positron',
                               zoom=3, center={'lat': 37.0902, 'lon': -95.7129},
                               opacity=0.5,
                               )
    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    fig.show()

world_data = 'data/sample_data_map.csv'
def plot_bar_graph(file: str, path: list[str]) -> None:
    """Plot a bar graph using the given file and countries in the given path. The graph compares the ____ of
    the countries in the path.

    Preconditions:
    - len(path) > 1
    """
    df = pd.read_csv(file)
    # TODO: implement after filter_csv functions are complete
