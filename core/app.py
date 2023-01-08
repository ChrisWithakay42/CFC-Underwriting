import json
import logging
import re
from collections import Counter
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests import RequestException


class WebScraper:
    """
        A class for scraping webpages.

        Attributes:
            url (str): The URL of the webpage to be scraped.
            soup (BeautifulSoup): The BeautifulSoup object representing the HTML of the webpage.

        Methods:
            scrape: Sends an HTTP request to the webpage and parses the HTML.
            get_resources: Extracts a list of externally loaded resources from the webpage.
            get_privacy_policy_url: Extracts the URL of the "Privacy Policy" page from the webpage.
            get_word_count: Produces a case-insensitive word frequency count from the visible text on the webpage.
        """

    def __init__(self, url):
        self.url = url
        self.soup = None

    def scrape(self):
        try:
            req = requests.get(self.url)
            req.raise_for_status()
            self.soup = BeautifulSoup(req.text, "html.parser")
        except RequestException as error:
            logging.error(error)

    def get_resources(self):
        resources = []
        for tag in self.soup.find_all(["img", "script", "link"]):
            src = tag.get("src")
            href = tag.get("href")
            if src and "cfcunderwriting.com" not in src:
                resources.append(src)
            if href and "cfcunderwriting.com" not in href:
                resources.append(href)
        return resources

    def get_privacy_policy_url(self):
        for a_tag in self.soup.find_all("a"):
            href = a_tag.get("href")
            if href and "privacy policy" in a_tag.text.lower():
                return urljoin(self.url, href)

    def get_word_count(self):
        text = self.soup.get_text()
        text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
        words = text.lower().split()

        word_count = Counter(words)
        return dict(word_count)


class Scraper:
    """
        A class for scraping the index webpage hosted at "cfcunderwriting.com" and the "Privacy Policy" page.

        Attributes:
            index_url (str): The URL of the index webpage.
            resources_path (str): The file path for the JSON output file containing the list of externally loaded
            resources.
            word_count_path (str): The file path for the JSON output file containing the word frequency count.

        Methods:
            scrape: Scrapes the index webpage, writes a list of all externally loaded resources to a JSON output file,
                identifies the location of the "Privacy Policy" page, and scrapes the privacy policy page and produces a
                case-insensitive word frequency count.
        """

    def __init__(self):
        self.index_url = "https://cfcunderwriting.com"
        self.resources_path = "resources.json"
        self.word_count_path = "word_count.json"

    def scrape(self):
        scraper = WebScraper(self.index_url)
        scraper.scrape()

        resources = scraper.get_resources()
        with open(self.resources_path, "w") as file:
            json.dump(resources, file)

        privacy_policy_url = scraper.get_privacy_policy_url()

        scraper = WebScraper(privacy_policy_url)
        scraper.scrape()
        word_count = scraper.get_word_count()
        with open(self.word_count_path, "w") as file:
            json.dump(word_count, file)


def main():
    scraper = Scraper()
    scraper.scrape()


if __name__ == "__main__":
    main()
