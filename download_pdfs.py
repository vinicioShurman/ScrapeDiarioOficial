import os # enables interaction with the OS
import requests # enables HTTP request - pip install requests
import json
import time

# Download PDF files:

# Create a Python program to download PDF files from the web
# https://www.youtube.com/watch?v=ye1oi8Lcobc

# Load links it will download, from a JSON file
with open('scrapped-urls-monteMor.json', 'r') as json_file:
    loaded_json = json.load(json_file)

# Extract urls that have not been downloaded before
filtered_urls = [item['url'] for item in loaded_json if item['downloaded'] == False]

print(filtered_urls)

# Output of the download
output_dir = r"D:\output"

# Check if the output directory exists; if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a dictionary for fast lookup based on URL
url_dict = {item['url']: item for item in loaded_json}

# Loop that goes through all the links
for url in filtered_urls:
    try:
        # Send the download request
        response = requests.get(url)

        # Check if the response is OK (status code 200)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, os.path.basename(url + ".pdf"))
            # file_path = os.path.join(output_dir, os.path.basename(url))
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")

            # Update 'downloaded' field to 1 for the corresponding item in loaded_json
            url_dict [url]['downloaded'] = True
        else:
            print(f"Error downloading {url}: {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

    # Add a small delay to be polite to the server
    time.sleep(1)

# Save the modified 'loaded_json' back to the JSON file
with open('scrapped-urls-monteMor.json', 'w') as json_file:
    json.dump(loaded_json, json_file, indent=2)
