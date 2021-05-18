##if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#not equal 
requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("Hold the anchnovives")

#magic_number
answer = 75

if answer != 42:
    print("That is not the correct answer. Please try again.")

#logical and 
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21) #false

#logcal or 
(age_0 >= 21) or (age_1 >= 21) #true

request_toppings = ['onion', 'mushroom', 'cheese']
'mushroom' in request_toppings #true

topping  = 'steak'
if topping not in request_toppings:
    print("not in there")

#try it yourself
car = 'subaru'
print(car == 'van')
carupper = 'SuV'
print(carupper.lower() == 'suv')
print((2+5) and (3+4) == 7)

if('onion' in request_toppings):
    print('onion found')

age = 2
if age >= 18:
    print("have you registered cause you are 19")
elif age <3:
    print("you way too young")
else: 
    print("you too young")

alien_color = 'blue'
if alien_color == 'green':
    print("it's green you get 5 pts")
else:
    print("it's not green")

if alien_color == 'green':
    print("It's green")
elif alien_color == 'blue':
    print("it's blue")
else:
    print("It's some other color")

age = 19
if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")

favorite_foods = ['banana', 'apple', 'orange']
if 'banana' in favorite_foods:
    print('found banana')
if 'orange' in favorite_foods:
    print('found orange')

requested_toppings = []

if requested_toppings:
    print("won't hit")
else:
    print("Are you sure you want a plain pizza?")

#using multiple lists example
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making you pizza!")


##try it yourself
admins = ["ben", "mark", "amy", "katie", "mike"]
if not admins: #checks if list is empty
    print("won't hit")
for admin in admins:
    print(f"Hey {admin}")

current_users = ["ben", "mark", "amy", "katie", "mike"]
new_users = ["lilly", "ben", "coco", "dudley", "paris"]

for current_user in current_users:
    if current_user in new_users:
        print(f"{current_user} already exists")
    else: 
        print(f"{current_user} added")

o_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for o_number in o_numbers:
    if o_number == 1:
        print(f"{o_number}st")
    elif o_number == 2:
        print(f"{o_number}nd")
    elif o_number == 3:
        print(f"{o_number}rd")
    else:
        print(f"{o_number}th")