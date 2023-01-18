from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def main():
  DRIVER_PATH = "D:\\Utilities\\geckodriver.exe"
  service = Service(DRIVER_PATH)
  
  options = Options()
  options.binary_location = "E:\\Program Files\\Mozilla Firefox\\firefox.exe"
  
  driver = webdriver.Firefox(service=service, options=options)
  driver.get("https://en.wikipedia.org/wiki/Main_Page")

  elem = driver.find_elements(By.CSS_SELECTOR, "#mp-otd li")
  print(elem[0].text)

  search = driver.find_element(By.CSS_SELECTOR, "#searchInput")
  search.send_keys("Starkey")
  search.send_keys(Keys.ENTER)
  #elem = driver.find_elements(By.CSS_SELECTOR, ".mw-search-results li")
  #print(elem[0].text)

  #driver.close() # Close tab
  driver.quit() # Close browser
  
if __name__ == "__main__":
  main()