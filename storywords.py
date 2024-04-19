# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
print("Which genre would you like?" + genres)
# print whichever genre the user selected
user_genre = input("Enter genre: ")
print(user_genre)
# define lists to start story
characters = ['one', 'two', 'three']
print("How many characters would you like?" + characters)
user_char = input("Enter characters: ")
print(user_char)
intro = ['Once upon a time ', 'Long ago ', 'Wandering through the darkness ', 'The sun shone and birds were chirping merrily ']
setting = ['there was a lost kingdom ', 'there was a grand civilization ', 'I crept around looking for light ', 'I was reading my book and sitting against a tree ']
print("What setting would you like?" + setting)
user_set = input("Enter setting: ")
print(user_set)
climax = ['who needed a hero to restore it']
end = ['']
# select an item from lists to print story
print(random.choice(intro)+random.choice(setting))