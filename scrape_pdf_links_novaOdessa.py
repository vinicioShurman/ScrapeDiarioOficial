import requests # enables HTTP request - pip install requests
import time # enables the use of wait times
import json # enables the use of json
import os
from selenium import webdriver # enables interaction with websites - pip install selenium
from webdriver_manager.chrome import ChromeDriverManager # enables to use the correct version of browser
from selenium.webdriver.chrome.service import Service # enables the use of the ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime # enables the use of dates


# Function to check if a string is a valid date
def is_valid_date(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Verify Chrome version and download the corresponding Chrome Driver
service = Service(ChromeDriverManager().install())

# Open a new Chrome window
browser = webdriver.Chrome(service=service)
browser.implicitly_wait(10)

browser.get("http://www.novaodessa.sp.gov.br/DiarioOficial.aspx")

time.sleep(3)

# Initialize an empty list outside the loop
all_urls = []

for i in range(1):
    print("Iteration:", i)
    
    # Gets all <a> tags from the window
    urls = browser.find_elements(By.TAG_NAME, 'a')

    # Create a list of href attributes using list comprehension
    urls = [link.get_attribute('href') for link in urls if link.get_attribute('href') is not None]

    # Removes any urls that are not useful
    prefix = "http://www.novaodessa.sp.gov.br/App_Arquivos/Diario/"
    urls = [value for value in urls if value.startswith(prefix)]

    # Append the current iteration's urls to the all_urls list
    all_urls.extend(urls)

    print(urls)

    time.sleep(3)

# Now, all_urls will contain the accumulated URLs from all iterations
print(all_urls)

import json

# Specify the file path
all_urls_file_path = r"scrapped-urls-novaOdessa.json"

# Read existing JSON data from the file
if os.path.exists(all_urls_file_path):
    with open(all_urls_file_path, 'r') as json_file:
        existing_data = json.load(json_file)

else:
    existing_data = []

# Add the new URLs to the existing data
for _, url in enumerate(all_urls):
    existing_data.append({'downloaded': False, 'url': url, 'name': url[-4:]})

# Convert the modified Python object back to JSON
updated_json_data = json.dumps(existing_data, indent=2)

# Open the file in write mode
with open(all_urls_file_path, 'w') as json_file:
    json_file.write(updated_json_data)

