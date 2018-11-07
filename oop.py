class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound 
		self.name = name
		self.age = age
		self.favorite_color = favorite_color 
	def eat(self,food):
		print("yummy!!" + self.name + " is eating " + food)

	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self):
		print (self.sound*3)

cat = Animal("meow", "Juliet", "4", "white")    	        
cat.make_sound()
cat.description()



class Person(object):
	def__init__(self, name, age, city, gender, school):
		self.name = name 
		self.name = name 
		self.age = age
		self.city = city 
		self.gender = gender 
		self.school = school
	def eat(self,favorite_breakfast)
		print(self.name + " is eating pancakes his " + favorite_breakfast)

	def play(self,favorite_sport)
		print(self.name + " plays tennis his " + favorite_sport)

person = Person("Aboud", "15", "Hebron", "male", "JSB")
person.eat() 
person.play()






