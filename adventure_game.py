

#adventure game
# first scenario
match_or_flashlight = str(input("""
      You are walking through a dark forest and find two items:
      a MATCH and a FLASHLIGHT. Which one do you want to pick up?
        """)).lower()

if match_or_flashlight == "match":
    run_or_hide = str(input("""
        You pick up the match and strike it, and for an instant, the forest around you is illuminated.
        You see a large grizzly bear, and then the match burns out.
        Do you want to RUN, or HIDE behind a tree?
          """)).lower()
    
    print("\033[031m\nWORK IN PROGRESS...\033[m")

elif match_or_flashlight == "flashlight":
    follow_look = str(input("""
        You pick up the flashlight and turn it on.
        You see the pathway lit up in front of you, but you thought you also heard something off to the side.
        Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?
          """)).lower()
    
    print("\033[33m\nWORK IN PROGRESS...\033[m")

else:
  print()
  print("SORRY, I CANNOT UNDERSTAND YOUR ANSWER. TRY AGAIN")
  
