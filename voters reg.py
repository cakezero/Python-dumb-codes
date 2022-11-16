#CODE ABOUT VOTER'S REGISTRATION :) - A 25 LINE CODE

card=input("Have you registered for your voter's card (PVC) before?(y/n): ")
l1 = "y"
l2 = "n"
if card == l1:
    val=input("Is it still valid?(y/n): ")
    if val==l1:
        print("There is no need for you to be here.\nHave a nice day :).")
elif card==l2:
     year=int(input("Enter, Which Year were you born: "))
     if year <= 2004:
      first=input("What is your First Name: ")
      lasst=input("What is your Last Name: ")
      month=input("Enter, Which month were you born: ")
      day=int(input("Enter, Which day were you born: "))
      print('Hurray, You are old enough to vote. :~)\n')
      
      print('Head to the main building to get your biometrics captured. \nIf you have gotten your biometrics captured, please head to the ICT to check if your PVC is ready.')
      age=2022-year  
      print(" ")
      print(lasst, first,"-> Was born in",day,"/",month,"/",year, "\nAnd is",age,"years old. :)")
     else:
      print("Sorry :~(, Try again when you're older")

      print("Ask your parents what year you were born.") 
print('\nThanks for choosing INEC :~)')