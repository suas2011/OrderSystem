#OrderSystem
import random

print('MAIN MENU')
print('='*10)
print('1-Pizza')
print('2-Burger')
print('3-Sweets')
print('4-Exit')
choice=int(input('enter your choice from [1-4]: '))
if choice==1:
    print('Pizza Menu\n')
    print('1-Small')
    print('2-Medium')
    print('3-Large')
    print('4-Main Menu')
    pchoice=int(input('enter your choice: '))
    if pchoice==1:
        srate=400
        n=0
        total=0
        n=int(input('\nenter how many small pizzaz you want? :'))
        total=n * srate
        print('\nYour order is processed!')
        print('One Small Pizza Rate is: ',srate)
        print('Total Small Pizza Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif pchoice==2:
        mrate=600
        n=0
        total=0
        n=int(input('\nenter how many medium pizzaz you want? :'))
        total=n * mrate
        print('\nYour order is processed!')
        print('One Medium Pizza Rate is: ',mrate)
        print('Total Medium Pizza Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))

    elif pchoice==3:
        lrate=1200
        n=0
        total=0
        n=int(input('\nenter how many large pizzaz you want? :'))
        total=n * lrate
        print('\nYour order is processed!')
        print('One Large Pizza Rate is: ',lrate)
        print('Total Large Pizza Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif pchoice==4:
        print('MAIN MENU')
        print('='*10)
        print('1-Pizza')
        print('2-Burger')
        print('3-Sweets')
        print('4-Exit')
        choice=int(input('enter your choice from [1-4]: '))
    else:
     print('Invalid Pizza Choices!')
   
elif choice==2:
    print('Burger Menu\n')
    print('1-Zinger')
    print('2-Egg Burger')
    print('3-Plain Burger')
    print('4-Main Menu')
    bchoice=int(input('enter your choice: '))

    if bchoice==1:
        zrate=280
        n=0
        total=0
        n=int(input('\nenter how many Zinger Burgers you want? :'))
        total=n * zrate
        print('\nYour order is processed!')
        print('One Zinger is: ',zrate)
        print('Total Zinger Burgers Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))

    elif bchoice==2:
        egrate=100
        n=0
        total=0
        n=int(input('\nenter how many Egg Burgers you want? :'))
        total=n * egrate
        print('\nYour order is processed!')
        print('One Egg Burger is: ',egrate)
        print('Total Egg Burgers Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif bchoice==3:
        prate=60
        n=0
        total=0
        n=int(input('\nenter how many Plain Burgers you want? :'))
        total=n * prate
        print('\nYour order is processed!')
        print('One Plain Burger is: ',prate)
        print('Total Plain Burgers Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif bchoice==4:
        print('MAIN MENU')
        print('='*10)
        print('1-Pizza')
        print('2-Burger')
        print('3-Sweets')
        print('4-Exit')
        choice=int(input('enter your choice from [1-4]: '))
    else:
        print('Invalid Burger Choice!')
elif choice==3:
    print('Sweet|Dessert Menu\n')
    print('1-Gulab Jamun')
    print('2-Rass Malaye')
    print('3-Brownies')
    print('4-Chocolate Fudge Cake')
    print('5-Main Menu')
    sdchoice=int(input('enter your choice: '))
    if sdchoice==1:
        gjrate=100
        gwt=150
        n=0
        total=0
        n=int(input('\nenter how many Packs of Gulab Jamun you want? :'))
        total=n * gjrate
        totalgj=gwt * n
        print('\nYour order is processed!')
        print('One Pack of Gulab Jamun is: ',gwt,'Grams')
        print('One Pack of Gulab Jamun Rate is: ',gjrate)
        print('Total Weight of Gulab Jamun for ',n,'Packs',totalgj)
        print('Total Packs Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif sdchoice==2:
        rmrate=150
        rwt=200
        n=0
        total=0
        n=int(input('\nenter how many Packs of Rass Malayai you want? :'))
        total=n * rmrate
        totalrm=rwt * n
        print('\nYour order is processed!')
        print('One Pack of Rass Malayai is: ',rwt,'Grams')
        print('One Pack of Rass Malayai Rate is: ',rmrate)
        print('Total Weight of Rass Malayai for ',n,'Packs',totalrm)
        print('Total Packs Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif sdchoice==3:
        brrate=120
        brwt=50
        n=0
        total=0
        n=int(input('\nenter how many Packs of Brownie you want? :'))
        total=n * brrate
        totalbr=brwt * n
        print('\nYour order is processed!')
        print('One Pack of Brownie is: ',brwt,'Grams')
        print('One Pack of Brownie Rate is: ',brrate)
        print('Total Weight of Brownie for ',n,'Packs',totalbr)
        print('Total Packs Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif sdchoice==4:
        ccfrate=800
        ccfwt="2.50 Pounds"
        n=0
        total=0
        n=int(input('\nenter how many Choco Fudge Cakes you want? :'))
        total=n * ccfrate
        totalccf=ccfrate * n
        print('\nYour order is processed!')
        print('One Pack of Brownie is: ',ccfwt)
        print('One Pack of Brownie Rate is: ',ccfrate)
        print('Total Weight of Brownie for ',n,'Packs',totalccf)
        print('Total Packs Ordered ',n)
        print('Total Amount to be paid: ',total)
        print('\nYour Order # is: ',random.randint(100,200+25))
    elif sdchoice==5:
        print('MAIN MENU')
        print('='*10)
        print('1-Pizza')
        print('2-Burger')
        print('3-Sweets')
        print('4-Exit')
        choice=int(input('enter your choice from [1-4]: '))
elif choice==4:
    print('Thanks for using the Order System!')
    exit()
else:
 print('Invalid Choice!')
