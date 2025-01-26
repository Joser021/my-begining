# i added colors and for the choices when the player ask
# i also added the library time to use the function sleep, to delay the sentences

from time import sleep
# colors
red_1 = ("\033[31m") # opening
red_2 = ("\033[m") # closing
yellow_1 = ("\033[33m") #opening
yellow_2 = ("\033[m") #closing


# codes that i will use a lot
else_variable = (f"\nSorry I don't understand your choice, {red_1}TRY AGAIN!{red_2}")

#adventure game
player = str(input("Inser your nickname:\n")).capitalize()

print(f"""
      You are walking through a dark forest and find two items:
      a {yellow_1}MATCH{yellow_2} and a {yellow_1}FLASHLIGHT{yellow_2}.
      """)
sleep(1)
match_or_flashlight = str(input("Which one do you want to pick up?\n")).lower()

sleep(0.5)
if match_or_flashlight == "match":
  print("""
      You pick up the match and strike it, and for an instant, the forest around you is illuminated.
      You see a large grizzly bear, and then the match burns out.
  """)
  sleep(1)
  run_or_hide = str(input(f"Do you want to {yellow_1}RUN{yellow_2}, or {yellow_1}HIDE{yellow_2} behind a tree?\n")).lower()

  if run_or_hide == "run":
    sleep(0.5)
    print("""
      You are so afraid and starts running.
      The bear is chasing you, you trip over a root.
          """)
    sleep(1)
    beg_or_play = str(input(f"Do you want to {yellow_1}BEG{yellow_2} for your life, or {yellow_1}PLAY{yellow_2} dead?\n")).lower()

    if beg_or_play == "beg":
      sleep(0.5) 
      print(f"""
      You beg for your life like you were about to lose it, and you really are.
      and you cry:
            {player}: Please Mr. Bear don't eat me, I'm not yummy
            """)
      
      sleep(2)
      print("""
      The bear stands on two legs, takes a hat out of its pocket, and putt it on its head.
      He says:
            
            Mr. Bear: Don't be concerned, I don't consume humans.
            In fact, it would be my pleasure to invite you to have dinner with my family."
            """)
      
      sleep(2)
      print("""
      Strangely, you accepted Mr. Bear's invitation.
      You had one of the best dinners of your life
      """)

      sleep(2)
      print(f"{"END":>25}\n")

    elif beg_or_play == "play":
      sleep(0.5)
      print("""
      You take advantage that you are already on the ground, and you try not to move.
      You get it, the bear thought you were dead and left
            """)
      
      sleep(2)
      print("""
      But you played so well that you actually died.
            """)

      sleep(2)
      print(f"{"END":>25}\n")
    
    else:
      sleep(0.5)
      print()
      print(else_variable)

  elif run_or_hide == "hide":
    sleep(0.5)
    print(f"""
      You hide behind a tree, and wait until the bear go away
      The bear left.
      You have options, {yellow_1}FIND{yellow_2} a way out, or {yellow_1}CHECK{yellow_2} if you can get other item
          """)
    sleep(1)
    find_or_check = str(input("Which one will you pick up?\n"))

    if find_or_check == "find":
      sleep(0.5)
      print("""
      You leave your hiding place, you walk around and find a path.
      You go through it, and find a pasture.
      There are a lot of cows.
            """)
      
      sleep(2)
      print("""
      You hear a weird noise, you start floating
      Oh, no you are being abducted
            """)

      sleep(2)
      print("""
                *Unknown Language*
            """)

      sleep(1.5)
      print("""
      You see aliens before you fall asleep
            """)

      sleep(1.5)
      print("""
      you wake up in your bed, it's so confortable.
      You don't remember much about last night.
      
      Everything was a dream, or maybe not...
            """)
      sleep(2)
      print(f"{"END":>25}")

    elif find_or_check == "check":
      sleep(0.5)
      print("""
            You go and check if there was more itens there
            You find a MATCH and a FLASHLIGHT
            """)
      
      sleep(2)
      print("""
      You pick up the match and strike it, and for an instant, the forest around you is illuminated.
      You see a large grizzly bear, and then the match burns out.
            """)
      
      sleep(2)
      print("""
      You hide behind a tree, and wait until the bear go away
      The bear left.
      You have options, FIND a way out, or CHECK if you can get other item
            """)
      
      sleep(2)
      print("""
      You are stuck in a loop.
      You are reliving this moment over and over again
            """)
      
      sleep(2)
      print(f"{"END":>25}")

    else:
      sleep(0.5)
      print()
      print(else_variable)

  else:
    sleep(0.5)
    print(else_variable)

elif match_or_flashlight == "flashlight":
  print("""
      You pick up the flashlight and turn it on.
      You see the pathway lit up in front of you, but you thought you also heard something off to the side.
        """)
  sleep(2)
  follow_or_look = str(input(f"Do you wanto to {yellow_1}FOLLOW{yellow_2} the path or {yellow_1}LOOK{yellow_2} in the trees for the thing that made the noise?\n")).lower()

  if follow_or_look == "follow":
    sleep(0.5)
    print("""
      Following the path helped you to find a cabin,
      it seems nobody is there, it seems to cozy
          """)
    
    sleep(2)
    enter_or_stay = str(input(f"You can {yellow_1}ENTER{yellow_2} the house or {yellow_1}STAY{yellow_2} outside. What do you want?\n")).lower

    if enter_or_stay == "enter":
      sleep(0.5)
      print("""
      You try to open the door, it is easy,the door is open.
      What is that? it smells so good.
      you go to the kitchen and you see three bowls of porridge
            """)
      
      sleep(2)
      eat_or_key = str(input(f"You have two options: {yellow_1}\nEat{yellow_2} the porridge, or that the {yellow_1}KEY{yellow_2} on the table.")).lower

      if eat_or_key == "eat":
        sleep(0.5)
        print("""
      You eat the porridge, it was delicious!
      Now you are sleepy, you go up stairs, and sleep in a comfy bed
              """)
        
        sleep(2)
        print("""
      After some minutes of sleeping the door opens slowly.
      A hige bear enters in the room.
      Bear: "Why did you eat my porridge? and why are you sleeping in my bed?""
              """)

        sleep(2)
        print("""
      You wake up scared and just start running and you never came back.
              """)

        sleep(2)
        print(f"{"END":>25}\n")

      elif eat_or_key == "eat":
        sleep(0.5)
        print("""
      The porridge seems so Yummy, but you took the car keys
      You find the car, and you run it
              """)

        sleep(2)
        print("""
      The car is running, You start driving
      you drive until you find a road and civilization
      You got home!
              """)

        sleep(2)
        print(f"{"END":>25}\n")

      else:
        sleep(0.5)
        print()
        print(else_variable)

    elif enter_or_stay == "stay":
      sleep(0.5)
      print("""
      You did right, it's not good entering in stranger's house wihtout invitation.
      but it started snowing when you got away from de cabin
      you didn't have cold clothes and then you died
            """)
      
      sleep(2)
      print(f"{"END":>25}\n")

    else:
      sleep(0.5)
      print(else_variable)

  elif follow_or_look == "look":
    sleep(0.5)
    print("""
      You find a dog behind a bush, it's a little afraid because it's alone
      It seems pretty frindly and happy to see someone
          """)

    sleep(2)
    take_or_leave_or_pet = str(input(f"You can {yellow_1}TAKE{yellow_2} the dog with you, or {yellow_1}LEAVE{yellow_2}, or {yellow_1}PET{yellow_2} the dog.")).lower()

    if take_or_leave_or_pet == "take":
      sleep(0.5)
      print("""
      The dog seems to be a good companior, so you decided to take it with you.
      It was a really good decision, the dog knows what it's doing
      You guys found a way to leave the forest
            """)
      
      sleep(2)
      print(f"{"END":>25}\n")

    elif take_or_leave_or_pet == "leave":
      sleep(0.5)
      print("""
      You decided to leave the dog there, it'll better without you
      it was a bad idea not taking the dog with you
      now you are lost, and have no idea where you are
            """)
      
      sleep(2)
      print(f"{"END":>25}\n")
    
    elif take_or_leave_or_pet == "pet":
      sleep(0.5)
      print("""
      You petted the dog, it's so fluffy
      you came down and decided to way until morning to do something
      """)

      sleep(2)
      print("""
      You waited until morning and could leave the forest safety and with a new friend
      """)

      sleep(2)
      print(f"{"END":>25}\n")

    else:
      sleep(0.5)
      print(else_variable)

  else:
    print(else_variable)

else:
  sleep(0.5)
  print(else_variable)
