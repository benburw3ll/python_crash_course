# friends = ['Emma', 'Peter', 'Megan', 'Andi', 'Kayla']
# print(friends[-1])

# print(f"Hello {friends[1]}")

# friends[1] = "Jacob"

# print(f"Hello {friends[1]}")

# #add to last spot in list
# friends.append("Maria")
# print(friends[-1])

# ##insert into list
# friends.insert(1, "Andrew")
# print(friends)

# #delete at index
# del friends[4]
# print(friends)

# #popping allows you to delete while adding to var
# popped_friend = friends.pop(3)
# print(popped_friend)

# #Remove by string
# # friends.remove('Andi')
# # print(friends)

# ##Guest List Try Yourself
# guest_list = ['marilyn', 'sopor', 'squeaky']
# print(f"You are invited to dinner {guest_list[0]}")
# cant_attend = guest_list.pop(0)
# print(f"{cant_attend} can't make it.")
# guest_list.insert(0, 'Katya')
# print(guest_list)
# print("We got a bigger table")
# guest_list.insert(0, "Grandpa")
# guest_list.insert(3, "Grandma")
# guest_list.append("Emma")
# print(guest_list)
# print("Have to shrink it down to 2 sorry")
# guest_list.pop()
# guest_list.pop()
# del friends[0]
# print(guest_list)

friends = ['Emma', 'Peter', 'Megan', 'Andi', 'Kayla']
friends.sort(reverse=True)
print(friends)

friends_temp_sorted = ['Emma', 'Peter', 'Megan', 'Andi', 'Kayla']

#temp sorts
print(sorted(friends_temp_sorted))
print(friends_temp_sorted)

friends_temp_sorted.reverse()
print(friends_temp_sorted)

#length
print(len(friends_temp_sorted))

# #Purposeful index out of range
# print(friends_temp_sorted[9])