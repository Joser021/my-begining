#I added colors with the ANSI escape and chain characters just to make it looks good
#I added new three lines to the story

#greetings to the story
print()
print("\033[33m-=-\033[m" * 15)
print("\033[31mWelcome to your Clever Stories Generator!\033[m")
print("\033[33m-=-\033[m" * 15)

#asking for user's prompting
print("\nPlease enter the following:")
adjective = input("\033[33mAdjective:\033[m ")
animal = input("\033[33mAnimal:\033[m ")
verb_1 = input("\033[33mVerb:\033[m ")
exclamation = input("\033[33mExclamation:\033[m ")
verb_2 = input("\033[33mVerb:\033[m ")
verb_3 = input("\033[33mVerb:\033[m ")
place = input("\033[33mPlace:\033[m ")
food = input("\033[33mFood:\033[m ")
clothing = input("\033[33mClothing:\033[m ")
movie = input("\033[33mMovie:\033[m ")

#displaying the story with the words given by the user
print()
print("\033[4;31mYOUR STORY IS:\033[m")
print("\033[33m-=-\033[m" * 30)
print(f"""\033[36mThe other day, I was really in trouble. It all started when I saw a very
\033[33m{adjective} {animal} {verb_1}\033[33m \033[36mdown the hallway. "\033[33m{exclamation.capitalize()}\033[m\033[36m!" I yelled. But all
I could think to do was to \033[33m{verb_2}\033[m \033[36mover and over. Miraculously,
that caused it to stop, but not before it tried to \033[33m{verb_3}
\033[36mright in front of my family. Because they were going to the \033[33m{place} \033[36mto eat
a delicious \033[33m{food} \033[36mwithout me, only because I was wearing a shiny \033[33m{clothing}
\033[36mfrom my favorite movie called \033[33m{movie.title()}\033[36m.""")
print("\033[33m-=-\033[m" * 30)
