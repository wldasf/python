from city_functions import city_country

def test_city_country():
    s = city_country('santiago', 'chile') 
    assert s == 'Santiago, Chile'