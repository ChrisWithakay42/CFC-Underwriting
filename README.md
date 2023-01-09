# CFC-Underwriting WebScraper
WebScraper is a Python script that scrapes a webpage and extracts a list of externally loaded resources and produces a case-insensitive word frequency count from the visible text on the webpage.

## Setup
To set up the WebScraper app, follow these steps:

1. Clone the repository and navigate to the root directory:
Copy code
```
git clone https://github.com/<your-username>/WebScraper.git
cd CFC-Underwriting
```
2. Install the required dependencies by running 
```
pip install -r requirements/test.in
```
## Usage
To use the WebScraper app, follow these steps:

Run the script:

Copy code
```
python app.py
```
The script will scrape the index webpage hosted at "cfcunderwriting.com" and the "Privacy Policy" page.
The list of externally loaded resources will be written to a JSON file called resources.json.
The word frequency count will be written to a JSON file called word_count.json.

### Note

It is advisable to create a 