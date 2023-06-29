import asyncio
import csv
import nest_asyncio
from requests_html import AsyncHTMLSession

nest_asyncio.apply()  # Enable nested asyncio support

async def scrape_website():
    session = AsyncHTMLSession()
    response = await session.get("https://portal.gdc.cancer.gov/exploration?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D")
    await response.html.arender()
    elements = response.html.find('.explore-case-table')

    # Prepare data for CSV
    data = []
    for element in elements:
        data.append(element.text)

    # Write data to CSV
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

async def main():
    await scrape_website()

asyncio.run(main())
