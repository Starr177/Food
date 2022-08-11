import random

print("This is the random food generator,may I ask what your name is?")
named = input()

print("hey " + named + " type eat to see what we have for you")

Userinput = input()


if Userinput == "eat":
   Userinput = random.randint(1,11)

eat = Userinput

#program logic 
if eat == 1:
    print("Tacos seem like a good choice today")

elif eat == 2:
    print("Just eat cereal")

elif eat == 3:
    print("Eat some fruits")

elif eat == 4:
    print("McDonalds seems like a good choice")

elif eat == 5:
    print("Wawa is right down the street")

elif eat == 6:
   print("A nice cheesy quesidilla will do")

elif eat == 7:
   print("Peanut butter.....mmhmm")

elif eat == 8:
   print("Drink some water...ha ha")

elif eat == 9:
   print("Make some spaghetti and meatballs")

elif eat == 10:
   print("A nice philly cheese steak might do")

elif eat == 11:
   print("A subway footlong might be nice")

elif eat == 12:
   print(" Nachos.... the only way!")

else:
   print("gReEn BeAnS")

 









