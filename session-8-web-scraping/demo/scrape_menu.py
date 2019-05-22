from bs4 import BeautifulSoup
import requests # We are using requests.get from here

### GOAL: Download dining page
'''
my_responce is a "responce" object
contains all of the information the server sent to us
'''
my_responce = requests.get("http://menu.dining.ucla.edu/Menus")
	

'''
The status code
'''
#print(my_responce.status_code)

'''
Raw html content
'''
#print(my_responce.content)


### GOAL: Narrow down the html page to zoom in on stuff we want

'''
Create BeautifulSoup object with webpage content
'''
soup = BeautifulSoup(my_responce.content, 'html.parser')

# print(soup.prettify())

'''
search for all menu blocks
'''
menu_blocks = soup.find_all("div", {"class":"menu-block half-col"})
# print(menu_blocks[0].prettify())

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
class food_item:
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
		new_items.append(food_item(name, dining_hall, time))
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
Function that goes throught the list of food from
the website and gives back a list of foods we like
'''
def find_food(food_list, foods):
	found_food = []
	for item in food_list:
		if item.name in foods:
			found_food.append(item) 
	return found_food

print(find_food(my_food, ["Scarbled Eggs"]))

### Extra: What if we want to find all foods with "Eggs" in it
'''
Looks at each item in sub_list and checks if it's a substring of item
'''
def contains_substring(sub_list, item):
	for sub in sub_list:
		if sub in item:
			return True
	return False
# Returns a list of elements from food_list that contain 
def find_food2(food_list, foods):
	return list(filter(lambda x: contains_substring(foods, x.name), food_list))

#Search for food I like
print(find_food2(my_food, ["Pizza", "Pork"]))






