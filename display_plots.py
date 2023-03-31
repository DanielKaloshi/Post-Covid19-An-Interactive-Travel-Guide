import json
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

sample_data = 'data/sample_data_map.csv'  # for testing purposes
data = 'data/country-danger-index.csv'
def plot_map(file: str) -> None:
    """Plot a choropleth map of the countries in the world using the danger indexes from
    the given file.
    """
    world_countries = json.load(open('data/world.geo.json'))
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


def plot_bar_graph(file: str, paths: list[str]) -> None:
    """Plot a bar graph using the given file and countries in the given path. The graph compares the danger indexes of
    the countries in the path.

    Preconditions:
    - len(path) > 1
    - Each country in paths is a country in the given file
    """
    df = pd.read_csv(file)
    df = df.loc[df['country'].isin(paths)]
    country = df['country']
    danger_index = df['danger_index']

    fig = plt.figure(figsize=(10, 5))
    plt.bar(country, danger_index)
    plt.title('Comparison of Danger Indexes')
    plt.xlabel('Countries')
    plt.ylabel('Danger Index')
    plt.show()

if __name__ == '__main__':
    plot_map(data)
