import json
from time import sleep

from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from driver import get_driver

driver = get_driver()


def extract_article_data():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find('ol', {'aria-live': "off"})
    links = results.find_all('li')
    tech_data_list = []
    for link in links:
        data = {
            "title": link.find('h2').text,
            "author_name": link.find("span", {"class": "css-1n7hynb"}).text,
            "date": link.find("span", {"data-testid": "todays-date"}).text,
            "summary": link.find('p').text,
        }
        tech_data_list.append(data)

    return tech_data_list


driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/header/div[4]/ul/li[7]/a').click()

driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="collection-technology"]/div[2]/div/nav/ul/li[1]/a'))))

tech_data = extract_article_data()
print('Tech Article data in dict format\n', tech_data)
json_object = json.dumps(tech_data, indent=4)

print('Tech Article data in dict format\n', json_object)

sleep(0.5)
driver.quit()
