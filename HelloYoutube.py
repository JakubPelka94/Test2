import math

# first_name = "Bro1"
# last_name = "Szef"
# full_name = first_name +" "+ last_name
# print("Hello " +full_name)
# print(type(name)) - sprawdzanie typu danych
# print("Hello "+name)

# age = 21fhg
# age +=1
# print("Your age ist "+str(age))
# print(type(age))

# height = 250.5
# print("Your height ist "+str(height)+"cm")
# print(type(height))
# human = True
# print("Are you a human: "+str(human))
# print(type(human))

# multiple assignments = allows us to assign variables at the same time in one line of code

# name = "Jakub"
# age = 21
# attractive = True
# name, age, attractive = "Chuj", 21, True
# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# name = "jakub"
# print(len(name))
# print(name.find("j"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a","u"))
# print(name*5)
# ------------------------------------------------------------

# type casting = convert the data of a value to another data type.

# x = 1 #int
# y = 2.0 #float
# z = "3" #str
# print(type(x),type(y),type(z))
# print(x,y,z)

# x = str(x)
# y = str(y)
# z = str(z)

# print("X is "+str(x),"Y is "+str(y),"Z is "+z*3)
# ------------------------------------------------------------
# name = input("What is your name?:")
# age = int(input("How old are you?:"))
# age +=1
# height = float(input("Whats is your height?:"))
# print("Hello "+name+", you are "+str(age)+" years old; your have "+str(height)+"cm")
# -----------------------------------------------------------

# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3
# print(type(pi), pi, round(pi), math.ceil(pi), math.floor(pi), abs(pi), pow(pi,2), math.sqrt(42),)
# print(max(pi,x,y,z), min(pi,x,y,z))
# -----------------------------------------------------------

# slicing = create a substring by extracting elements from another string
# indexing [] or slice ()
# [start:stop:step]
# name ?

# name = "Bro Code"

# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name[::-1]

# print(type(first_name),first_name,last_name)
# print(funky_name)
# print(reversed_name)

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)
#print(website1[slice])
#print(website2[slice])
# -----------------------------------------------------------

# if statement = a block of code will execute if it's condition is true

#age = int(input("How old are you?: "))

#if age > 18 and age < 65:
# print("Pijesz piwko!")
#elif age < 0:
# print("No chyba nie!")
#elif age == 18:
# print("sTO LAT!")
#elif age >= 65:
    #print("Do trumny!")
#else:
# print("Wypierdalaj gowniaku!")
# -----------------------------------------------------------

# logical operators (and, or, not) = used to check uf two or more conditional statments

#temp = float(input("Whats is the temperature outside?: "))


#if not (temp >= 0 and temp <= 30):
    #print("The temperature is bad today!")
    #print("Stay inside!")
# #not (temp < 0 or temp > 30):
 #   print("The temperature is good today:")
   # print("Go outside!")

#1:04.00
# -----------------------------------------------------------
 #while loop = a statement that will execute it's block of code as long as it's condition remains true

#while 1==1:
  #  print("Help")

#name = None
#while not name:
#    name = input("Enter your name: ")
#print("Hello "+name)
# -----------------------------------------------------------
#for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print(i)

#for i in "Bro Code":
#    print(i)

#import time
#for i in range(10,0-1,-1):
#    print(i)
#    time.sleep(0.5)
#print("Happy new year")

#----------------------------------------
#1.13.07
#nested loop = The "inner loop" will finisch all of it's iterations before finishing oone iiteratio of the "outerloop "

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
 #   for j in range(columns):
  #      print(symbol, end="")
   # print() # drukowanie nowej linii

    #-----------

#Loop Control Statements = channge a loop execution from ti's sequence
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

#while True:
 #   name = input("Enter your name: ")
  #  if name != "":
   #     break

#phone_number = "123-456-789"
#for i in phone_number:
 #    if "-" == i:
  #     continue
   #  print(i, end="")

#for i in range(1,21):
 #   if i == 13:
  #      pass
   # else:
    #    print(i, end=" ")

#----------------------------
#lists = used to store multiplce items in a singe variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding", "hamburger"]
food[0] = "pizza1"
#for i in food:
#     print(i, end=" ")
#food.append("ice cream")
#for x in food:
#     print(x, end=" ")
#food.remove("hamburger")
#food.pop()
#food.insert(0, "chuj")
#food.sort()
#food.clear()
#print(food)

#----------------------------
#1.27.00
