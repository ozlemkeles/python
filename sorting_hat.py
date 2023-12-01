"""
This Python script simulates the process of the Hogwarts Sorting Hat by 
asking the user a series of questions and determining the most suitable
house based on their answers. 
Each house (Gryffindor, Ravenclaw, Hufflepuff, Slytherin) has a point system, 
and the user's responses contribute to the points of the corresponding houses. 
The house with the highest total points is then revealed as the sorted house for the user.
"""

house ={'Gryffindor':0, 'Ravenclaw':0, 'Hufflepuff':0, 'Slytherin':0}

print('===============')
print('The Sorting Hat')
print('===============')

question1 = ["Q1) Do you like Dawn or Dusk?","1) Dawn", "2) Dusk"]
print (*question1, sep="\n")
answer1 = int(input("Enter your answer (1-2):"))

if answer1 == 1:
  house["Gryffindor"] += 1
  house["Ravenclaw"] += 1
elif answer1 == 2:
  house["Hufflepuff"] += 2
  house["Slytherin"] += 2
else:
  print("Wrong input.")

question2 = ["Q2) When I’m dead, I want people to remember me as:","1) The Good", "2) The Great", "3) The Wise", "4) The Bold"]
print (*question2, sep="\n")
answer2 = int(input("Enter your answer (1-4):"))

if answer2 == 1:
  house["Hufflepuff"] += 2
elif answer2 == 2:
  house["Slytherin"] += 2
elif answer2 == 3:
  house["Ravenclaw"] += 2
elif answer2 == 4:
  house["Gryffindor"] += 2
else:
  print("Wrong input.")

question3 = ["Q3) Which kind of instrument most pleases your ear?","1) The violin", "2) The trumpet", "3) The piano", "4) The drum"]
print (*question3, sep="\n")
answer3 = int(input("Enter your answer (1-4):"))

if answer3 == 1:
  house["Slytherin"] += 4
elif answer3 == 2:
  house["Hufflepuff"] += 4
elif answer3 == 3:
  house["Ravenclaw"] += 4
elif answer3 == 4:
  house["Gryffindor"] += 4
else:
  print("Wrong input.")

print("Your house is",max(house, key=house.get))
