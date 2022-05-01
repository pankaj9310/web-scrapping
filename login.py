import json
import os

from bs4 import BeautifulSoup

from time import sleep

from driver import get_driver


def get_user_details():
    _username = os.environ.get("EMAIL")
    _password = os.environ.get("PASSWORD")
    if _username is None:
        raise Exception("Email id is required")
    if _password is None:
        raise Exception("Password is required")
    return _username, _password


def get_account_details():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find('section', {'data-testid': 'your-profile'})
    account_data = {
        "accountNumber": results.find("span", {"data-testid": "account-number:list-item-body"}).text,
        "email": results.find("span", {"data-testid": "email-address:list-item-body"}).text,
        "memberSince": soup.find("span", {"class": "css-10umaqq"}).text.strip(),
    }
    return account_data


USERNAME, PASSWORD = get_user_details()
driver = get_driver()
login_button = driver.find_element_by_link_text("LOG IN").click()
username = driver.find_element_by_id("email")  # username form field
username.send_keys(USERNAME)
driver.find_element_by_class_name("css-9c8h5i-buttonBox-buttonBox-primaryButton-primaryButton-Button").click()
sleep(2)
password = driver.find_element_by_id("password")  # password form field
password.send_keys(PASSWORD)
sleep(1)
driver.find_element_by_xpath('//*[@type="submit"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@data-testid="user-settings-button"]').click()
sleep(0.5)
driver.find_element_by_class_name('css-cexmzz').click()
sleep(2)

account_details = get_account_details()
print("Account details in dict format\n", account_details)
print("Account details in json format\n", json.dumps(account_details, indent=4))

driver.quit()
