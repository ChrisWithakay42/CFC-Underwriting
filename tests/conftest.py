import pytest

from core.app import WebScraper


@pytest.fixture
def index_scraper():
    return WebScraper("http://example.com")


@pytest.fixture
def mock_response(mocker):
    mock_response = mocker.Mock()
    mock_response.text = """
    <html>
    <body>
        <p>This is a test. This is only a test.</p>
    </body>
    </html>
    """
    mock_response.raise_for_status.return_value = None
    return mock_response



