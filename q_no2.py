import operator
from collections import Counter

import pandas as pd


def read_file():
    file = open("IMDb_movies.csv", encoding="UTF8")
    dataframe = pd.read_csv(file, low_memory=False)
    dataframe = dataframe.dropna(subset='country')
    file.close()
    return dataframe


def show_sorted_countries():
    dataframe = read_file()
    countries = []

    for country in dataframe.country.tolist():
        country = country.split(',')
        countries.extend(country)

    countries = [country.strip(' ') for country in countries]
    country_count = Counter(countries)

    return dict(sorted(country_count.items(), key=operator.itemgetter(1), reverse=True)[:10])


def show_graph():
    sorted_countries = show_sorted_countries()
    for movies in sorted_countries.keys():
        movies_count = int((sorted_countries[movies]) / 1000)
        graph = movies_count * chr(9608)
        print(f'{movies:20}{graph} {round(sorted_countries[movies] / 1000,2)}k')


def main():
    show_graph()


main()
