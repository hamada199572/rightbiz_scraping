# scraper/browser_connector.py

import logging
from typing import Optional
from playwright.sync_api import sync_playwright, Browser
from config.settings import CDP_ENDPOINT

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class BrowserConnector:
    """
    Responsible solely for connecting to an already running manual browser instance 
    via Chrome DevTools Protocol (CDP) port 9222 for anti-bot mitigation.
    """
    
    def __init__(self):
        self.playwright = None
        self.browser: Optional[Browser] = None

    def connect_browser(self) -> Optional[Browser]:
        """Connects to the pre-launched browser instance using CDP endpoint."""
        try:
            self.playwright = sync_playwright().start()
            # Connect to the existing Chrome instance launched manually on port 9222
            self.browser = self.playwright.chromium.connect_over_cdp(CDP_ENDPOINT)
            logger.info("Successfully connected to the browser via CDP.")
            return self.browser
        except Exception as e:
            logger.error(f"Failed to connect to the browser: {e}")
            raise e

    def close(self):
        """Stops the playwright instance safely."""
        if self.playwright:
            self.playwright.stop()
            logger.info("Playwright session closed.")