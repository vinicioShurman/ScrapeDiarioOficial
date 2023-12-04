# diario-oficial
1. First it scrape some sites and gets all the links, then filter the links and saves then into a JSON file.
2. Download the PDFs from the remaining links and marks the downloaded links with "Downloaded" in the JSON file.
3. Then it extract the text from all PDFs and look the text for specified words then deletes the files that do not have matches.
4. In the end the PDFs files that remain have words that you were looking for.
 
Lots of comments in the code because I was in the process of learning Python, and I knew I would forget what something was in the next day.
I was planning in cleaning everything up and making it scrape the website for new PDFs every time I turn on the computer, but I have other responsibilities at the moment.
