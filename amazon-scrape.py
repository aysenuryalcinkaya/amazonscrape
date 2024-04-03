from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.amazon.com.tr/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome('path/to/chromedriver', options=options)

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
other="https://www.amazon.de/dp/"

div_elements = soup.find_all('div', {'data-asin': True})

for div in div_elements:
    data_asin = div['data-asin']
    print('Data-asin:', data_asin)

    div_element = div.find('div', class_='a-section a-spacing-none a-spacing-top-small s-price-instructions-style')
    if div_element:
        link = div_element.find('a')['href']
        price = div_element.find('span', class_='a-price-whole').text + '.' + div_element.find('span', class_='a-price-fraction').text + ' ' + div_element.find('span', class_='a-price-symbol').text
        
        print('Link:', link)
        print('Price:', price)
        otherurl = other + data_asin
        driver.get(otherurl)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        



    else:
        print('Div element not found.')

driver.quit()
print(len(div_elements))