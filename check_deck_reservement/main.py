from get_chrome_driver import GetChromeDriver
from selenium import webdriver

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.get('https://hashito.biz/')
print(driver.find_element_by_xpath('/html/body/div[1]/div/section/div/div/h2').text)
print(driver.current_url)
driver.quit()
