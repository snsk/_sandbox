from get_chrome_driver import GetChromeDriver
from selenium import webdriver
import sys

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.implicitly_wait(10)

driver.get('https://www.steamdeck.com/ja/')

expect_text = 'Steam Deckは、2022年2月より、アメリカ、カナダ、欧州連合、イギリスで出荷が開始されます。その後、他の地域でも出荷予定です。今後のお知らせをお楽しみに。'
if len(driver.find_elements_by_id('availability'))>0:
    actual_text = driver.find_element_by_xpath('/html/body/div[3]/section[12]/div/div[2]/p').text
else:
    print("Steam Deck availability region has changed!")

if expect_text == actual_text:
    print('Steam Deck does not available my region ...')
else:
   sys.exit("Steam Deck availability region has changed!")

driver.quit()
