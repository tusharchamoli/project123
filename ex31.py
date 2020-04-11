print("""
You are in a room which has 3 doors
You have to chose any one door to enter
""")
door = input(">")

if door=="1":
    print("Cogratulations there is bear eating a cheesecake now directly starring at you")
    print("What would you do now")
    print("1. Take the cake.")
    print("2. Scream .")
    bear= input(">")
    if bear=="1":
        print("The bear eats your face off , GOOD JOB")
    elif bear=="2":
        print("The bear eats your legs off, GOOD JOB")
    else:
        print("You should let whatever bear wants to do, frankly you can't don anything about it")
    
elif door == "2": 
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.") 
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.") 
    
    insanity = input("> ") 
    if insanity == "1" or insanity == "2": 
        print("Your body survives powered by a mind of jello.") 
        print("Good job!") 
    else: 
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
else:
    print("You stumble around and fall on a knife and die. Good")