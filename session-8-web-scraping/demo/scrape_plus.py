# from bs4 import BeautifulSoup
# import requests

# my_responce = requests.get("http://quotes.toscrape.com/js")

# soup = BeautifulSoup(my_responce.content, 'html.parser')

# print(soup.prettify())

'''
Wait! This doesn't have anything useful
'''

# https://pypi.org/project/selenium/
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.get('http://quotes.toscrape.com/js')

'''
https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
Gives us back list of special selenium "WebElements"
'''
for i in range(1, 3):
	quote_boxes = browser.find_elements_by_class_name("quote")

	for quote_box in quote_boxes:
		#https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html
		quote = quote_box.find_element_by_class_name("text").text
		author = quote_box.find_element_by_class_name("author").text
		print(f"Author: {author}\nQuote: {quote}\n")
	next_button = browser.find_element_by_class_name("next").find_element_by_tag_name("a")
	next_button.click()
input()
browser.quit()
