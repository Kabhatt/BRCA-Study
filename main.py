import csv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver
driver = Chrome()

# Load the main webpage
url = "https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=cases"
driver.get(url)

# Find the main table element
wait = WebDriverWait(driver, 60)
main_table_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#repository-cases-table")))

# Extract initial links from the main table
initial_links = main_table_container.find_elements(By.CSS_SELECTOR, "a.unnamed-link")

data = []

# Process each initial link
for link in initial_links:
    # Get the overlay element and wait until it disappears
    overlay = wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ReactModal__Overlay")))

    # Click on the initial link
    link.click()

    # Wait for the new page to load
    wait.until(EC.staleness_of(main_table_container))

    # Find the new table element on the linked page
    new_table_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-container")))
    new_table = new_table_container.find_element(By.TAG_NAME, "#clinical-supplement-file-table")
    rows = new_table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "th")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)

    # Go back to the previous page
    driver.back()

# Write data to CSV file
csv_filename = "data.csv"
with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
print(f"Data written to {csv_filename}")

# Quit the driver
driver.quit()