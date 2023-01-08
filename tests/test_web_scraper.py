import requests
from bs4 import BeautifulSoup


class TestWebScraper:

    def test_scrape(self, index_scraper, mocker, mock_response):
        mocker.patch.object(requests, "get", return_value=mock_response)
        index_scraper.scrape()
        assert index_scraper.soup is not None

    def test_get_resources(self, index_scraper):
        html = """
        <html>
        <body>
            <img src="image.jpg">
            <script src="script.js"></script>
            <link href="style.css">
        </body>
        </html>
        """
        index_scraper.soup = BeautifulSoup(html, "html.parser")
        resources = index_scraper.get_resources()
        assert resources == ["image.jpg", "script.js", "style.css"]

    def test_get_privacy_policy_url(self, index_scraper):
        html = """
        <html>
        <body>
            <a href="/privacy-policy">Privacy Policy</a>
        </body>
        </html>
        """
        index_scraper.soup = BeautifulSoup(html, "html.parser")
        privacy_policy_url = index_scraper.get_privacy_policy_url()
        assert privacy_policy_url == "http://example.com/privacy-policy"

    def test_get_word_count(self, index_scraper):
        html = """
        <html>
        <body>
            <p>This is a test. This is only a test.</p>
        </body>
        </html>
        """
        index_scraper.soup = BeautifulSoup(html, "html.parser")
        word_count = index_scraper.get_word_count()
        assert word_count == {"this": 2, "is": 2, "a": 2, "test": 2, "only": 1}
