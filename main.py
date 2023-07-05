import csv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver
driver = Chrome()

# Load the webpage
url = "https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=cases"
driver.get(url)

# Find the table element
wait = WebDriverWait(driver, 10)
table_element = wait.until(EC.presence_of_element_located((By.ID, "repository-cases-table")))

# Check if the table element was found
if table_element is None:
    print("Table element not found on the page.")
else:
    # Extract data from the table
    rows = table_element.find_elements(By.TAG_NAME, "tr")
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        for cell in cells:
            # Handle nested elements within the cell
            nested_elements = cell.find_elements(By.CSS_SELECTOR, "div, span")
            cell_text = ""
            for element in nested_elements:
                cell_text += element.text.strip() + " "
            cell_text = cell_text.strip()
            if cell_text:  # Skip empty cells
                row_data.append(cell_text)
        if row_data:  # Skip empty rows
            data.append(row_data)

    # Write data to CSV file
    csv_filename = "data.csv"
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)
    print(f"Data written to {csv_filename}")

# Quit the driver
driver.quit()

