# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
print("Which genre would you like?" + genres)
# print whichever genre the user selected
print(random.choice(genres))
# define lists to start story
characters = ['one', 'two', 'three']
print("How many characters would you like?" + characters)
intro = ['Once upon a time ', 'Long ago ', 'Wandering through the darkness ', 'The sun shone and birds were chirping merrily ']
print("What setting would you like?" + setting)
setting = ['there was a lost kingdom ', 'there was a grand civilization ', 'I crept around looking for light ', 'I was reading my book and sitting against a tree ']
climax = ['who needed a hero to restore it']
end = ['']
# select an item from lists to print story
print(random.choice(intro)+random.choice(plot))