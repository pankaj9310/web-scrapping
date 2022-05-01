from selenium import webdriver

url = 'https://www.nytimes.com/'


def get_driver():
    driver = webdriver.Chrome("/snap/bin/chromium.chromedriver")  # driver path
    driver.get(url)
    return driver
