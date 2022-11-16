#ANOTHER PIZZA CODE - A 774 LINE CODE
#YAY ._.

pizza_count_top = 1
pizza_count_on = 1
pizza_count_ol = 1
izza_count_che = 1
piz = 0
ex1 = 'Cheese'
ex2 = 'with extra Mushrooms'
ex3 = 'with extra Olives'
ex4 = 'with extra Cheese'
ex5 = 'with extra Onoins'
t1 = 'small sized pizza'
t2 = 'medium sized pizza'
t3 = 'normal sized pizza'
t4 = 'big sized pizza'
t5 = 'jumbo sized pizza'
p1 = 'pepperoni and cheese'
p2 = 'pepperoni and onion'
p3 = 'pepperoni and olives'
p4 = 'pepperoni and mushroom'
p5 = 'cheese and olives'
p6 = 'cheese and mushrooms'
p7 = 'olives and mushrooms'
p8 = 'cheese and onions'
p9 = 'olives and onions'
p0 = 'mushroom and onion'
print('Make your order:\n'.title())
pizza ={'pazza':[t1,t2,t3,t4,t5]}
for pi in pizza['pazza']:
    piz=piz + 1
    print(str(piz)+ '.',pi.title())
count = 0
numb = 0
l1 = 1
l2 = 2
av_tops= {'toping' : ['cheese','mushrooms','olives','extra cheese','onoins']}
Or=int(input('\nYour Order:'))
if Or<=5:
    if Or==0:
        print('Error :(, Wrong Input')
    else:
     print('\nChoose Your Topping: '.upper())
     toppings=[' \npepperoni and cheese', ' pepperoni and onion', ' pepperoni and olives', ' pepperoni and mushroom', ' cheese and olives', ' cheese and mushrooms', ' olives and mushrooms', ' cheese and onions', ' olives and onions', 'mushroom and onion']
     for topping in toppings:
       count=count + 1
       print(str(count)+ '.',topping.title())
     tp=int(input('\nYour Desired Topping:'))
     if tp<=10:
        if tp==0:
            print('Error :(, Wrong Input')
        else:
         print('Need more Toppings:'.upper())
         print('1. Yes')
         print('2. No')
         ned=int(input("\nChoose 1 or 2('Yes or No'):"))
         if ned == l1:
           for top in av_tops['toping']:
            numb = numb + 1
            print(str(numb)+ '.',top.title() +' Topping')
           Op=int(input('Which Topping, Do you need:'))
           if Op<=5:
             print('\nNo need to worry, I gotcha :)')
         elif ned == l2:
          print('\nOkay :)')
         else:
          print("Select a valid option :(" ) 
     else:
      print('Select a more valid option :(')   
else:
    print("You haven't selected a valid option :(")
if Or==1:
    if tp==1:
        if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p1+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p1+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p1+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p1+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p1+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t1.title()+' with '+p1+' will be ready soon')
    elif tp==2:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p2+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p2+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p2+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p2+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p2+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
                print('Your '+t1.title()+' with '+p2+' will be ready')
    elif tp==3:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p3+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p3+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p3+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p3+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
           print('Your',+t1.title(),+ 'with '+p3+' will soon be ready')
    elif tp==4:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p4+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p4+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p4+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p4+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p4+' will soon be ready')
    elif tp==5:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p5+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p5+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p5+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p5+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p5+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p5+' will soon be ready')    
    elif tp==6:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p6+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p6+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p6+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p6+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p6+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p6+' will soon be ready')    
    elif tp==7:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p7+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p7+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p7+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p7+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p7+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p7+' will soon be ready')    
    elif tp==8:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p8+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p8+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p8+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p8+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p8+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p8+' will soon be ready')    
    elif tp==9:
          if ned==l1:
            if Op==1:
              print('Your '+t1.title()+' with '+p9+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p9+' topping and '+ex2+' will be ready soon')
            elif Op==3:
                print('Your '+t1.title()+' with '+p9+' topping and '+ex3+' will be ready soon')
            elif Op==4:
                print('Your '+t1.title()+' with '+p9+' topping and '+ex4+' will be ready soon')
            elif Op==5:
                print('Your '+t1.title()+' with '+p9+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t1.title()+' with '+p9+' will soon be ready')    
    elif tp==10:
        if ned==l1:
            if Op==1:
               print('Your '+t1.title()+' with '+p0+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t1.title()+' with '+p0+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t1.title()+' with '+p0+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t1.title()+' with '+p0+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t1.title()+' with '+p0+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
          print('Your '+t1.title()+' with '+p0+' will soon be ready')    
elif Or==2:
    if tp==1:
        if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p1+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p1+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p1+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p1+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p1+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
         print('Your '+t2.title()+' with '+p1+' will soon be ready')    
    elif tp==2:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p2+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p2+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p2+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p2+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p2+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t2.title()+' with '+p2+' will soon be ready')    
    elif tp==3:
        if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p3+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p3+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p3+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p3+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
           print('Your '+t2.title()+' with '+p3+' will soon be ready')    
    elif tp==4:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p4+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p4+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p4+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p4+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p4+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t2.title()+' with '+p4+' will soon be ready')    
    elif tp==5:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p5+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p5+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p5+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p5+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p5+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t2.title()+' with '+p5+' will soon be ready')    
    elif tp==6:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p6+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p6+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p6+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p6+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p6+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t2.title()+' with '+p6+' will soon be ready')    
    elif tp==7:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p7+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p7+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p7+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p7+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p7+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t2.title()+' with '+p7+' will soon be ready')    
    elif tp==8:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p8+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p8+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p8+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p8+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p8+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t2.title()+' with '+p8+' will soon be ready')    
    elif tp==9:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p9+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p9+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p9+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p9+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p9+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
             print('Your '+t2.title()+' with '+p9+' will soon be ready')    
    elif tp==10:
          if ned==l1:
            if Op==1:
               print('Your '+t2.title()+' with '+p0+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t2.title()+' with '+p0+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t2.title()+' with '+p0+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t2.title()+' with '+p0+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t2.title()+' with '+p0+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t2.title()+' with '+p0+' will soon be ready')    
elif Or==3:
    if tp==1:
        if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p1+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p1+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p1+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p1+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p1+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t3.title()+' with '+p1+' will soon be ready')  
    elif tp==2:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p2+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p2+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p2+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p2+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p2+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p2+' will soon be ready')
    elif tp==3:
        if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p3+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p3+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p3+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p3+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t3.title()+' with '+p3+' will soon be ready')
    elif tp==4:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p4+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p4+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p4+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p4+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p4+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p4+' will soon be ready')
    elif tp==5:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p5+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p5+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p5+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p5+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p5+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p5+' will soon be ready')
    elif tp==6:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p6+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p6+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p6+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p6+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p6+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p6+' will soon be ready')
    elif tp==7:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p7+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p7+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p7+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p7+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p7+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p7+' will soon be ready')
    elif tp==8:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p8+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p8+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p8+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p8+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p8+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p8+' will soon be ready')
    elif tp==9:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p9+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p9+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p9+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p9+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p9+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p9+' will soon be ready')
    elif tp==10:
          if ned==l1:
            if Op==1:
               print('Your '+t3.title()+' with '+p0+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t3.title()+' with '+p0+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t3.title()+' with '+p0+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t3.title()+' with '+p0+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t3.title()+' with '+p0+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t3.title()+' with '+p0+' will soon be ready')
elif Or==4:
    if tp==1:
        if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p1+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p1+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p1+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p1+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p1+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t4.title()+' with '+p1+' will soon be ready')
    elif tp==2:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p2+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p2+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p2+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p2+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p2+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
           print('Your '+t4.title()+' with '+p2+' will soon be ready')
    elif tp==3:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p3+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p3+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p3+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p3+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p3+' will soon be ready')
    elif tp==4:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p4+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p4+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p4+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p4+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p4+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p4+' will soon be ready')
    elif tp==5:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p5+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p5+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p5+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p5+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p5+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p5+' will soon be ready')
    elif tp==6:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p6+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p6+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p6+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p6+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p6+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p6+' will soon be ready')
    elif tp==7:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p7+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p7+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p7+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p7+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p7+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p7+' will soon be ready')
    elif tp==8:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p8+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p8+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p8+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p8+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p8+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p8+' will soon be ready')
    elif tp==9:
          if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p9+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p9+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p9+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p9+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p9+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t4.title()+' with '+p9+' will soon be ready')
    elif tp==10:
        if ned==l1:
            if Op==1:
               print('Your '+t4.title()+' with '+p0+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t4.title()+' with '+p0+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t4.title()+' with '+p0+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t4.title()+' with '+p0+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t4.title()+' with '+p0+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t4.title()+' with '+p0+' will soon be ready')
elif Or==5:
    if tp==1:
        if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p1+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p1+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p1+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p1+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p1+' topping and '+ex5+' will be ready soon')
        elif ned==l2:
            print('Your '+t5.title()+' with '+p1+' will soon be ready')
    elif tp==2:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p2+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p2+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p2+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p2+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p2+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p2+' will soon be ready')
    elif tp==3:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p3+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p3+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p3+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p3+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p3+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p3+' will soon be ready')
    elif tp==4:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p4+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p4+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p4+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p4+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p4+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p4+' will soon be ready')
    elif tp==5:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p5+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p5+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p5+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p5+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p5+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p5+' will soon be ready')
    elif tp==6:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p6+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p6+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p6+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p6+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p6+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p6+' will soon be ready')
    elif tp==7:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p7+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p7+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p7+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p7+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p7+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p7+' will soon be ready')
    elif tp==8:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p8+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p8+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p8+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p8+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p8+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p8+' will soon be ready')
    elif tp==9:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p9+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p9+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p9+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p9+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p9+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p9+' will soon be ready')
    elif tp==10:
          if ned==l1:
            if Op==1:
               print('Your '+t5.title()+' with '+p0+' topping and added '+ex1+' will be ready soon')
            elif Op==2:
               print('Your '+t5.title()+' with '+p0+' topping and '+ex2+' will be ready soon')
            elif Op==3:
               print('Your '+t5.title()+' with '+p0+' topping and '+ex3+' will be ready soon')
            elif Op==4:
               print('Your '+t5.title()+' with '+p0+' topping and '+ex4+' will be ready soon')
            elif Op==5:
               print('Your '+t5.title()+' with '+p0+' topping and '+ex5+' will be ready soon')
          elif ned==l2:
            print('Your '+t5.title()+' with '+p0+' will soon be ready')