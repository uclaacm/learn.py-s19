from bs4 import BeautifulSoup
import requests # We are using requests.get from here


### GOAL: Download dining page
'''
my_response is a "response" object
contains all of the information the server sent to us
'''
my_response = requests.get("http://menu.dining.ucla.edu/Menus")
	

'''
The status code
'''
#print(my_response.status_code)

'''
Raw html content
'''
#print(my_response.content)


### GOAL: Narrow down the html page to zoom in on stuff we want

'''
Create BeautifulSoup object with webpage content
'''
soup = BeautifulSoup(my_response.content, 'html.parser')

# print(soup.prettify())

'''
search for all menu blocks
'''
		#menu_blocks = soup.find_all("div", {"class":"menu-block half-col"})
def is_menu_item(css_class):
	return str(css_class).startswith("menu-block")

menu_blocks = soup.find_all("div", {"class":is_menu_item})
#print(menu_blocks[0].prettify())

def print_menu_block(block):
	time = block.find_previous_sibling("h2").text
	print(f"Dining hall: {block.h3.text} ({time})")
	menu_items = block.find_all("li", {"class":"menu-item"})
	for item in menu_items:
		print(f"    Item: {item.span.a.text}")
	print("")

for block in menu_blocks:
	print_menu_block(block)


### GOAL: Search the foods and find ones we like
'''
We printed all the stuff... that's good, but what if
we want to search through it
'''
class FoodItem:
	def __init__(self, name, hall, time):
		self.name = name
		self.hall = hall
		self.time = time.split()[0]

	'''
	__repr__ is a special function that answers the question:
	How should a food_item object look when printed?
	'''
	def __repr__(self):
		return f"Name: {self.name}\nHall: {self.hall}\nTime: {self.time}\n"

'''
Finds all food items in a block
'''
def get_food_from_block(block):
	new_items = []
	time = block.find_previous_sibling("h2").text
	dining_hall = block.h3.text
	menu_items = block.find_all("li", {"class":"menu-item"})
	for item in menu_items:
		name = item.span.a.text
		new_items.append(FoodItem(name, dining_hall, time))
	return new_items

'''
Gets a list of ALL foods in ALL blocks
'''
my_food = []

for block in menu_blocks:
	food_items = get_food_from_block(block)
	my_food.extend(food_items)

#print(my_food)

'''
Looks at each item in sub_list and checks if it's a substring of item
'''
def contains_substring(sub_list, item):
	for sub in sub_list:
		if sub in item:
			return True
	return False
# Returns a list of elements from food_list that contain 
def find_food(menu, fav_foods):
    found_food = []
    for menu_option in menu:
        if contains_substring(fav_foods, menu_option.name):
            found_food.append(menu_option)
	return found_food

#Search for food I like
print(find_food(my_food, ["Pizza", "Pork"]))






