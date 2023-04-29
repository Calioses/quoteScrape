from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# removed auto install as I already have chrome and it was causing issues
driver = webdriver.Chrome()
url = 'http://quotes.toscrape.com/js'


# added some potential dry as I'm not sure if this is for actual use?
def quoteScrape(url):
    driver.get(url)

    while True:
        # first sleep for initial page load
        time.sleep(1)
        # Not really sure what was going on wit the previous selectors. Selenium has a bug where several By.<options> are defaulting to CSS selector so I've been strong armed.
        first_quote = driver.find_element(
            By.XPATH, '/html/body/div/div[2]').text
        next_button = driver.find_element(
            By.CSS_SELECTOR, 'body > div > nav > ul > li > a')
        # My machine needs the second sleep for selenium to work write. Not need everywhere. Just a budget fix for a silly problem
        time.sleep(1)
        # changed the logic to make a little more sense.
        if not next_button:
            break
        # It's good habit to use action chain to click as it will avoid pain with what tag actual holds the button. Not to mention bot protections
        webdriver.ActionChains(driver).click(next_button).perform()
        # No need to change
        print(first_quote)


# added some pain removing boilerplate. Force of habit.
if __name__ == '__main__':
    quoteScrape(url)
