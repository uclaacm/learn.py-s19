#!/usr/bin/python

# Class/ Objects
# class Person:
# 	name = "blah"
# 	age = 12
# 	fav_food = "burger"
# 
# p1 = Person()
# print(p1.name)
# print(p1.age)
# print(p1.burger)
# 
# class Person:
# 	name
# 	age
# 	fav_food
# Error!

# class Person:
# 	def __init__(self,name,age,fav_food):
# 		self.name = name
# 		self.age = age
# 		self.fav_food = fav_food
# 	def birthday(self):
# 		self.age += 1
# 	def change_of_heart(self, new_fav_food):
# 		self.fav_food = new_fav_food
# 		print('Yum!')
# 
# p1 = Person("Furn", 20, "Kbbq")
# print(p1.name)
# print(p1.age)
# print(p1.fav_food)
# p1.birthday()
# print(p1.age)
# p1.change_of_heart("Avocado toast")
# print(p1.fav_food)

# File handling
f = open('file.txt', 'r+w')
f.write('Hello World\n')
f.write('This is our new text file')
f.seek(0)
print(f.read(6))
print(f.read())
f.close()

with open('file.txt', 'r') as f:
	read_data = f.read()
	print read_data
f.close()
