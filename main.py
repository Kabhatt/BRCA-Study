from bs4 import BeautifulSoup
import requests

source= requests.get('https://portal.gdc.cancer.gov/exploration?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D').text
soup = BeautifulSoup(source,"lxml")
print(soup.prettify())
table = soup.find('div', id('explore-case-table'))
print(soup.prettify(table))



