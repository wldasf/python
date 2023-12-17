def city_country(city, country, population=0):
    if population > 0:
        s = f"{city}, {country} - population {population}"
    else:
        s = f"{city}, {country}"
    return  s.title()
