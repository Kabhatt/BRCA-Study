from bs4 import BeautifulSoup
import requests

source = requests.get('https://portal.gdc.cancer.gov/').text
soup = BeautifulSoup(source, "lxml")

table = soup.find('table', id="genes-table")

# Find all header rows (tr)
header_rows = table.find_all("tr")
for row in header_rows:
    # Extract header cells (th)
    headers = row.find_all("th")
    header_texts = [header.text for header in headers]
    print(header_texts)

# Find all data rows (tr)
data_rows = table.find_all("tr")
for row in data_rows:
    cells = row.find_all("td")
    cell_texts = [cell.text for cell in cells]
    print(cell_texts)

