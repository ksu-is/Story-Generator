# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
print("Which genre would you like?" + genres)

intro = ['Once upon a time ', 'Long ago ', 'Wandering through the darkness ', 'The sun shone and birds were chirping merrily ']
setting = ['there was a lost kingdom ', 'there was a grand civilization ', 'I crept around looking for light ', 'I was reading my book and sitting against a tree ']
fantasy_phrases = []
history_phrases = []
action_phrases = []

the_phrases = []
# print whichever genre the user selected
user_genre = input("Enter genre: ")
if user_genre == "fantasy":
    the_phrases = fantasy_phrases
elif user_genre == "history":
    the_phrases = history_phrases
else:
    the_phrases = action_phrases

# select an item from lists to print story
print(random.choice(intro)+random.choice(setting) + " "+ random.choice(the_phrases))