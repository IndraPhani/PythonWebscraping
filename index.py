from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from country_covid_details import country_covid_details
import pickle


load_dotenv()

url = os.environ["URL"]

html_doc = requests.get(url).text
soup_doc = BeautifulSoup(html_doc, 'html.parser')

div_elements = soup_doc.find_all('div', attrs={'class': "tr depth_0"})

countries_list: country_covid_details = []

for obj in div_elements:
    country:country_covid_details = country_covid_details()

    countryName = obj.find('div', attrs={'class': "column_name td"}).text
    country.country_name = countryName

    totalCases = obj.find('div', attrs={'class': "column_Cumulative_Confirmed td"}).text.replace(',', '')
    country.total_cases = int(totalCases) if totalCases != '' else 0

    casesInLast7Days = obj.find('div', attrs={'class': "column_Last_7_Days_Confirmed td"}).text.replace(',', '')
    country.cases_in_last_7days = int(casesInLast7Days) if casesInLast7Days != '' else 0

    totalDeaths = obj.find('div', attrs={'class': "column_Cumulative_Deaths td"}).text.replace(',', '')
    country.total_deaths = int(totalDeaths) if totalDeaths != '' else 0

    deathsInLast7Days = obj.find('div', attrs={'class': "column_Last_7_Days_Deaths td"}).text.replace(',', '')
    country.deaths_in_last_7days = int(deathsInLast7Days) if deathsInLast7Days != '' else 0

    countries_list.append(country)

for obj in countries_list:
    print(obj.country_name + " " + str(obj.total_cases) + " " + str(obj.cases_in_last_7days) + " " + str(obj.total_deaths) + " " + str(obj.deaths_in_last_7days))
    

obj = {}
i = 1

for result in countries_list:
    obj[str(i)] = result
    i = i + 1

with open("countriesDataPickle", 'wb') as pickle_file:
    pickle.dump(obj, pickle_file)

pickle_file.close()