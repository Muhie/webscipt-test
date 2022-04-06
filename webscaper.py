from selenium import webdriver

url = 'https://www.nike.com/gb/t/air-force-1-le-older-shoe-D59pRJ/DH2920-111'
browser = webdriver.Chrome()
browser.find_element_by_xpath('//*[@id="floating-atc-wrapper"]/div[2]/button[1]').click