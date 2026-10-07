import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

def parse_search_results(page: Page) -> list[dict]:
    
    listings_data = []
    
    try:
        cards = page.locator(".content__body__item").all()
        logger.info(f"Found {len(cards)} listing cards on the page.")

        for card in cards:
            try:
                listing = {
                    "advert_id": card.get_attribute("id"),
                    "title": card.get_attribute("data-title"),
                    "location": card.get_attribute("data-location"),
                    "price": card.get_attribute("data-price"),
                    "url": card.get_attribute("data-url"),
                    "latitude": card.get_attribute("data-lat"),
                    "longitude": card.get_attribute("data-lng"),
                }
                listings_data.append(listing)
            except Exception as inner_e:
                logger.warning(f"Failed to parse an individual card: {inner_e}")
                continue

        logger.info(f"Successfully extracted {len(listings_data)} listings from search page.")
        return listings_data

    except Exception as e:
        logger.error(f"Error occurred while parsing search results page: {e}")
        return []