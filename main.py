from bs4 import BeautifulSoup
import requests
import csv


class table_scraper:
    results = []

    def fetch(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find_all('div', id='explore-case-table')
        rows = table.find_all('th')
        columns = table.find_all('tr')
        self.results.append([header.text for header in rows])
        print(self.results)
        for row in columns:
            self.results.append([data.text for data in row.find_all('td')])
            for one in self.results:
                print(one)

    def to_csv(self):
        with open('table_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.results)

    def run(self):
        response = self.fetch('https://portal.gdc.cancer.gov/exploration?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D')
        self.parse(response)


if __name__ == '__main__':
    scraper = table_scraper()
    scraper.run()
