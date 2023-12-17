from city_functions import city_country

def test_city_country():
    s = city_country('santiago', 'chile')
    assert s == 'Santiago, Chile'

def test_city_country_population():
    x = city_country('santiago', 'chile', 5000000)
    assert x == 'Santiago, Chile - Population 5000000'
