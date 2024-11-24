from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parsel import Selector
import re
import math
import concurrent.futures

def parse_zoopla(deal_type, city):
    pn = 1
    # Configure Chrome to run in headless mode and disable images and JavaScript
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
    chrome_options.add_argument("start-maximized")  # ensure window is full-screen
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (may help with headless mode)
    chrome_options.add_argument('--no-sandbox')  # Disable sandboxing (maybe necessary on certain systems)
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-javascript')  # Disable JavaScript
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # Disable loading images

    # Create a Chrome WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Load a webpage
    start_url = f'https://zoopla.co.uk/{deal_type}/property/{city}/?pn={pn}'
    driver.get(start_url)
    # Get the text content of the page
    page_text = driver.page_source
    selector = Selector(text=page_text)
    header_div = selector.css('div[data-testid="search-results-header-control"]')
    results_text = header_div.css('p[data-testid="total-results"]::text')
    results_total_no = int(re.search(r'\d+', str(results_text)).group()) \
        if re.search(r'\d+', str(results_text)) else 0
    no_of_listings_on_a_page = len(selector.css('div[data-testid="regular-listings"]').css('div[id^="listing_"]'))
    page_source = driver.page_source
    # Close the WebDriver
    driver.quit()

    print(results_total_no)
    print(no_of_listings_on_a_page)
    try:
        max_pgn = results_total_no / no_of_listings_on_a_page
        max_pgn = math.ceil(max_pgn)
    except Exception as e:
        return f"Error occurred: {e}"
    print(max_pgn)

    # Save the page text as a text file
    with open('page_contents.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(page_source)

    return pn, max_pgn, deal_type, city


pn, max_pgn, deal_type, city = parse_zoopla("to-rent", "aberdeen")
print(pn, max_pgn, deal_type, city)

page_sources = []
urls = []


def urls_parsing():
    # Configure Chrome to run in headless mode and disable images and JavaScript
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
    chrome_options.add_argument("start-maximized")  # ensure window is full-screen
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (may help with headless mode)
    chrome_options.add_argument('--no-sandbox')  # Disable sandboxing (maybe necessary on certain systems)
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-javascript')  # Disable JavaScript
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # Disable loading images

    # Create a Chrome WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    for pg in range(pn, max_pgn+1):
        urls.append(f'https://zoopla.co.uk/{deal_type}/property/{city}/?pn={pn}')
    for url in urls:
        try:
            # Load the URL
            driver.get(url)

            # Perform actions on the webpage
            # You can extract data, click buttons, submit forms, etc. here

            # Example: Get the page title and print it
            page_source = driver.page_source
            page_sources.append(page_source)
        finally:
            # Ensure that the WebDriver is closed, even in case of exceptions
            driver.quit()

