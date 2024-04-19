# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
# print whichever genre the user selected
print(random.choice(genres))
# define lists to start story
intro = ['Once upon a time ', 'Long ago ', 'Wandering through the darkness ', 'The sun shone and birds were chirping merrily ']
plot = ['there was a lost kingdom ', 'there was a grand civilization ', 'I crept around looking for light ', 'I was reading my book and sitting against a tree ']
climax = ['']
end = ['']
# select an item from lists to print story
print(random.choice(intro)+random.choice(plot))