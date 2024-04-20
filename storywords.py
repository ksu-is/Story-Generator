# import random module
import random
# list of genres for user to pick
genres = ['fantasy', 'history', 'action', 'classic']
print("Which genre would you like?", genres)
# adding intros and phrases for each genre
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
fantasy_conclusions = ["With a final incantation, the darkness was sealed away, never to return.",
    " The hero's sacrifice ensured that peace would reign for generations to come.",
    " As the sun set on the battlefield, the echoes of war faded into memory.",
    " The realm was restored to its former glory, bathed in the light of a new dawn.",
    " With the defeat of the tyrant, hope bloomed anew in the hearts of the people."]

history_conclusions = [" With the rebel leader captured and their stronghold destroyed, the uprising was quelled once and for all.",
    " The decisive battle turned the tide of war, securing victory for the victorious army and restoring peace to the land.",
    " In the aftermath of the siege, the city lay in ruins, a stark reminder of the cost of conflict.",
    " With the traitor's plot exposed and their allies scattered, the kingdom emerged from the brink of collapse stronger than ever.",
    " As the dust settled on the battlefield, the fallen were mourned and the survivors looked towards a brighter future."]

action_conclusions = [" With the bomb disarmed and the villain apprehended, the city breathed a collective sigh of relief.",
    " The hero's decisive action saved countless lives and brought an end to the villain's reign of terror.",
    " As the dust settled, the hero stood victorious, a beacon of hope in a world plagued by darkness.",
    " With the villain defeated and justice served, peace was restored to the streets once more.",
    " The hero's bravery and cunning outmatched the villain's schemes, ensuring that evil would never prevail."]
the_conclusions = []
# print whichever genre the user selected
user_genre = input("Enter genre: ")
if user_genre == "fantasy":
    the_phrases = fantasy_phrases
    the_conclusions = fantasy_conclusions
elif user_genre == "history":
    the_phrases = history_phrases
    the_conclusions = history_conclusions
else:
    the_phrases = action_phrases
    the_conclusions = action_conclusions

# select an item from lists to print story
print(random.choice(intro)+
      random.choice(setting) + 
      random.choice(the_phrases) + 
      random.choice(the_conclusions))