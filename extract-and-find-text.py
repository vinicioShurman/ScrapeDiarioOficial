import PyPDF2 # enables extraction of text from PDF - pip install PyPDF2
import re # enables to search and modify texts
import json
import os

# Extract text from PDF files:

# Scraping Text From PDF Using Python | Python For Beginners
# https://www.youtube.com/shorts/T08KcZwIZ_Q?feature=share

# Load JSON it will download, from a JSON file
with open('scrapped-urls-monteMor.json', 'r') as json_file:
    loaded_json = json.load(json_file)

# Extract 'name' that have not been downloaded before
filtered_names = [item['name'] for item in loaded_json]

# Create a dictionary for fast lookup based on nameFound
# nameFound_dict = {item['nameFound']: item for item in loaded_json}

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store the extracted text
        pdf_text = ""

        # Iterate through all pages and extract text
        for page in pdf_reader.pages:
            # Extract text from the page
            pdf_text += page.extract_text()

    # re Removes punctuations
    return re.sub(r'[^\w\s]', '', pdf_text)

def find_words(text, word_list):
    # Create a pattern that matches any word from the specified word list
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, word_list)) + r')\b', flags=re.IGNORECASE)
    
    # Use findall to find all occurrences of the pattern in the text
    words_found = pattern.findall(text)
    
    return words_found

def process_and_delete_pdfs(directory_path):
    # Get the names of the files in the directory
    pdf_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.pdf')]

    # Iterate through the names and process each PDF
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(directory_path, pdf_file)

        # Call the function to extract text from the PDFname
        extracted_text = extract_text_from_pdf(pdf_file_path)

        # Perform further processing or save the extracted text as needed
        if extracted_text is not None:
            # Search for words inside the extracted text
            word_list_to_find = ['', '', ''] # write here the names you want to find
            found_words = find_words(extracted_text, word_list_to_find)
            if found_words:
                print(found_words)
            else:
                print("No matching words.")
                try:
                    os.remove(pdf_file_path)
                    print(f"{pdf_file} deleted.")
                except Exception as e:
                    print(f"Error deleting {pdf_file}: {e}")
        else:
            print("Error extracting text")

    # Save the modified 'loaded_json' back to the JSON file
    with open('scrapped-urls-monteMor.json', 'w') as json_file:
        json.dump(loaded_json, json_file, indent=2)

# Specify the directory path containing PDF files
pdf_directory_path = r"D:\output"

# Call the function to process and delete PDFs in the specified directory
process_and_delete_pdfs(pdf_directory_path)




