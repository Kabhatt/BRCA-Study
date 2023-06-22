from bs4 import BeautifulSoup
import requests
import csv


class table_scrap:
    results=[]
    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        content = BeautifulSoup(html,'lxml')
        table = content.find_all('explore-case-table')
        rows = table.findAll('th')
        column = table.findAll('tr')
        self.results.append([header.text for header in rows[0].findAll('th')])
        print(self.results)

    def to_csv(self):
        pass

    def run(self):
        response =self.fetch = ('https://portal.gdc.cancer.gov/exploration?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D')
        self.parse(response.text)

if __name__ == '_main_':
    scraper = table_scrap()
    scraper.run()
