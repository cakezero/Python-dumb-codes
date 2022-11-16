#CODE FOR PIZZA SELECTION - A 73 LINE CODE

print("Select your Pizza:")
print("1. Pepperoni Pizza")
print("2. Italian Pizza")
print("3. Pizza Rustica")
print("4. Mac & Cheese Pizza\n")
pizza=int(input("Your Option:"))
if pizza== 1:
    print("How would you like your Pepperoni Pizza:")
    print("1. Pepperoni Extra Spicy")
    print("2. Pepperoni Mild")
    print("3. pepperoni Not Spicy")
    piz=int(input("Your Option:"))
    if piz==1:
        print("\nOoh Hot")
    elif piz==2:
        print("\nNo worries, I gotcha!!!")
    else:
        print("Not Spicy it is!!")
elif pizza==2:
    print("How would you like your Italian Pizza:")
    print("1. Spicy")
    print("2. Not Spicy")
    piz=int(input("Your Option:"))
    if piz==1:
        print("\nOoh Ooh Spicy gotcha!!!")
    else:
        print("\nNot Spicy no worries!!!") 
elif pizza==3:
    print("Would you like chicken on it?")
    print("Option 1. Yes")
    print("       2. No")
    piz=int(input("Choose:"))
    if piz==1:
     print("\nThe chicken is on the house! :)")
    else:
     print("Okay")
elif pizza==4:
    print("You like sour foods, Great choice. :)")
    print("Do you want your Cheese extra gooey?")
    print("Option 1. Yes")
    print("       2. No")
    piz=int(input("Choose:"))
    if piz==1:
        print("\nOkay :)")
    else:
        print("\nNo probs! :(") 
if pizza==1:
    if piz==1:
     print("Your Pepperoni Pizza Extra Spicy Order is on its way. Have a sit")
    elif piz==2:
        print("Your Pepperoni Pizza Mild Order is on its way. Have a sit")
    else:
        print("Your Pepperoni Pizza Not Spicy Order is on its way. Have a sit")  
elif pizza==2:
    if piz==1:
     print("Your Spicy Italian Pizza Order is on its way. Have a sit")
    elif piz==2:
        print("Your Not Spicy Italian Pizza Order is on its way. Have a sit")
elif pizza==3:
    if piz==1:
     print("Your Chicken Pizza Rustica Order is on its way. Have a sit")
    elif piz==2:
        print("Your Pizza Rustica Order is on its way. Have a sit")
elif pizza==4:
    if piz==1:
     print("Your Extra gooey Mac & Cheese pizza Order is on its way. Have a sit")
    elif piz==2:
        print("Your Mac & Cheese Piazza Order is on its way. Have a sit")
if pizza<=4:        
  print("Thanks for Ordering")
else:
    print("You haven't selected a valid option :(.\n")
    print("Try Again :(")        