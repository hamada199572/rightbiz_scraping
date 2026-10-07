import logging
from scraper.browser_connector import BrowserConnector
from parsers.search_parser import parse_search_results
from utils.exporter import save_to_jsonl


logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    try:
    
        connector = BrowserConnector()
        browser = connector.connect_browser()
        
        if not browser:
            logger.error("Failed to connect to browser via CDP.")
            return
        context = browser.contexts[0]
        page = context.pages[0]

        logger.info("Starting search results extraction...")
        
        
        listings = parse_search_results(page)

        
        if listings:
            save_to_jsonl(listings, filename="output_listings.jsonl")
        else:
            logger.warning("No listings found to save.")

    except Exception as e:
        logger.error(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()