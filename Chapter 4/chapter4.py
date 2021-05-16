magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician} that was a great trick!")
    print(f"{magician.title()} that was a great trick with your name caps!\n")

print("This isn't in the loop good job magicians lulz")

#try it yourself 
pizzas = ['pepperoni', 'sausage', 'steak']
for pizza in pizzas:
    print(f'{pizza} is my favorite pizza') 
print("wow I like pizza")

for value in range(1,6):
    print(value)

#this makes a list 
numbers = list(range(1, 6))
print(numbers)

#this does only even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#lets put squares into the list
squares = []
for value in range (1, 10):
    squares.append(value ** 2)
print(squares)

#stats
digits = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 0]
min (digits) #0
max(digits) #9
sum(digits) #45

##try it yourself
for value in range(1, 21):
    print(value)

millionlist = []
for value in range(1, 1_000_001):
    millionlist.append(value)
print(min(millionlist))
print(max(millionlist))
print(sum(millionlist))

#this does only odd numbers
odd_numbers = list(range(2, 11, 1))
print(odd_numbers)

#slicing a list 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:4])
print(players[:3])
print(players[2:])
print(players[-3:])

#loop through a list
for player in players[:3]:
    print(player.title())

#copying lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('my foods')
print(my_foods)
friend_foods.append('ice cream')
print('friends foods')
print(friend_foods)

#try it yourself 
print('the first 3 players in this are')
print(players[:3])
print('3 items in middle of list')
print(players[2:4])
print('the last 3 items in this list are')
print(players[-3:])

pizzas = ['pepperoni', 'sausage', 'steak']
friends_pizzas = pizzas[:]
pizzas.append('cheese')
friends_pizzas.append('cake')
print('my favorite pizzas')
print(pizzas)
print('my friends pizzas')
print(friends_pizzas)

for pizza in pizzas:
    print(pizza)
for friends_pizza in friends_pizzas:
    print(friends_pizza)

#tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for deminsion in dimensions:
    print(deminsion)
dimensions = [400, 100]
for deminsion in dimensions:
    print(deminsion)

#try it yourself
basic_foods = ('bread', 'apple', 'pasta', 'yogurt', 'eggs')
for basic_food in basic_foods:
    print(basic_food)
print('menu changed')
basic_foods = ('pizza', 'popcorn', 'pasta', 'yogurt', 'eggs')
for basic_food in basic_foods:
    print(basic_food)