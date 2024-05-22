import requests
import pandas as pd

# Funkcija za dohvat podataka o kvaliteti zraka za zadani grad i godinu
def get_air_quality_data(city, year):
    # URL za dohvat podataka
    url = f"http://iszz.azo.hr/iskzl/rest/medcom/v1/airquality/index/param=pm10/city={city}/from={year}-01-01/to={year}-12-31/xml"

    # Dohvat podataka
    response = requests.get(url)
    data = response.json()

    # Pretvaranje podataka u DataFrame
    df = pd.DataFrame(data['results'])

    return df

# Dohvaćanje mjerenja dnevne koncentracije lebdećih čestica PM10 za 2017. godinu za grad Osijek
city = "Osijek"
year = 2017
df = get_air_quality_data(city, year)

# Ispis tri datuma u godini kada je koncentracija PM10 bila najveća
top_dates = df.nlargest(3, 'value')['date']
print("Tri datuma u godini kada je koncentracija PM10 bila najveća:")
print(top_dates)

