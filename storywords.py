# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
print("Which genre would you like?" + genres)

intro = ['Once upon a time ', 'Long ago ', 'Wandering through the darkness ', ]
setting = ['there was a lost kingdom ', 
           'there was a grand civilization ',  ]
fantasy_phrases = ["The alchemist summoned a storm to thwart the enemy's advance", 
    "The sorceress cast a spell to shield the kingdom from harm", 
    "The druid communed with the spirits of the forest to uncover ancient secrets", 
    "The seeress gazed into her crystal ball, foretelling the fate of nations",
    "The mystic invoked the power of the elements to protect the sacred temple"]
history_phrases = ["Amidst the bustling markets of an ancient metropolis",
    "In the shadow of towering cathedrals and bustling markets",
    "Among the opulent palaces and labyrinthine alleyways of a mighty empire",
    "Within the walls of a majestic castle overlooking rolling hills and verdant valleys",
    "Beneath the towering pyramids of a once-great civilization"]
action_phrases = ["With a swift motion, he unsheathed his sword and cleaved through the enemy's defenses",
    "She leapt from rooftop to rooftop, agile as a cat, evading her pursuers with ease",
    "He swung from the chandelier, crashing into the enemy ranks with a thunderous impact",
    "With a deafening roar, he unleashed a barrage of arrows, each finding its mark with deadly precision",
    "She somersaulted through the air, landing gracefully amidst a swarm of adversaries"]

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