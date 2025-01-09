'''
The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family. Because they were going to the [place] to eat a delicious [food] without me,
only because I was wearing a shiny [clothing] from my favorite movie, [movie].
'''
#Exclamation word needs to be CAPITALIZED, because it begins a new sentence

#greetings to the story
#I added colors with the ANSI escape
print()
print("\033[33m-=-\033[m" * 15) #make it yellow
print("\033[31mWelcome to your Clever Stories Generator!\033[m") #Make it read
print("\033[33m-=-\033[m" * 15) #Make it yellow

print("\nPlease enter the following:")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb = input("Verb: ")
verb = input("Verb: ")
place = input("Place: ")
food = input("Food: ")
clothing = input("Clothing: ")
movie = input("Movie: ")

print("-=-" * 30)
print(f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb}
right in front of my family. Because they were going to the {place} to eat
a delicious {food} without me, only because I was wearing a shiny {clothing}
from my favorite movie, {movie.title()}.""")
print("-=-" * 30)