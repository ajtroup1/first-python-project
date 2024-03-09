#Raul's Taco Joint

import os #imports cls
from datetime import datetime
os.system('cls')

#initialize primary menu choice to access while loop
primaryMenuChoice = -1

#receive customer's name
name = input('Name for order: ')

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time
formattedDateTime = current_datetime.strftime("%m/%d/%Y %I:%M %p")

#define cost for each meat item
chicken = 9.00
carneAsada = 10.00
alPastor = 9.50
vegetarian = 8.00
carnitas = 10.50
barbacoa = 11.00

custTotal = 0

while primaryMenuChoice != 0:
    primaryMenuChoice = input("Shopping for "+name+".\n\nRaul's menu:\n\t1 - Tacos\n\t2 - Burritos\n\t3 - House Specialties\n\t4 - Bowls\n\t5 - Nachos\n\t6 - Check Out\n\t0 - Exit\n\n(Current total: ${:.2f})\n\nMenu Choice: ".format(custTotal)) #use double quotes to include apostraphe

    #dont convert primaryMenuChoice to int read below

    os.system('cls')
    #handle for each menu choice. price scales flat between each option
    if primaryMenuChoice == '1': #Taco code
        inc = .5  # inc is the price increase for getting a different type of menu item like taco, burrito, etc
        itemChoice = input("Raul's Tacos (3 per order):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n\t0 - Back\n\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        #keeping primaryMenuChoice a string allows error handling for if user inputs string. if it was an int and user input a string, it would return error. now, it routes to else statement
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        elif itemChoice == '0':
            os.system('cls')
            continue
        else:
            input('Invalid input, press Enter to continue...')
            os.system('cls')
            continue
    elif primaryMenuChoice == '2': #Burrito code
        inc = 1
        itemChoice = input("Raul's Burritos:\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada (${:.2f})\n\t3 - Al Pastor (${:.2f})\n\t4 - Vegetarian (${:.2f})\n\t0 - Back\n\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        elif itemChoice == '0':
            os.system('cls')
            continue
        else:
            input('Invalid input, press Enter to continue...')
            os.system('cls')
            continue
    elif primaryMenuChoice == '3': #House code
        itemChoice = input("Raul's House Specialties:\n\t1 - Fajita Quesadilla ($11.50)\n\t2 - Shrimp Enchilada ($12.00)\n\t3 - Tamales ($8.50)\n\t4 - Gordita ($9.50)\n\t0 - Back\n\n")
        if itemChoice == '1':
            custTotal += 11.5
        elif itemChoice == '2':
            custTotal += 12
        elif itemChoice == '3':
            custTotal += 8.5
        elif itemChoice == '4':
            custTotal += 9.5
        elif itemChoice == '0':
            os.system('cls')
            continue
        else:
            input('Invalid input, press Enter to continue...')
            os.system('cls')
            continue
    elif primaryMenuChoice == '4': #Bowls code
        inc = 0 #bowls are base price
        itemChoice = input("Raul's Bowls (comes with rice, lettuce, pico de gallo, beans):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n\t0 - Back\n\n".format(chicken, carneAsada, alPastor, vegetarian))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        elif itemChoice == '0':
            os.system('cls')
            continue
        else:
            input('Invalid input, press Enter to continue...')
            os.system('cls')
            continue
    elif primaryMenuChoice == '5': #Nachos Code
        inc = 1.5
        itemChoice = input("Raul's Nachos (comes with chips, salsa, peppers, jalapenos, olives, sour cream):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n\t0 - Back\n\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        elif itemChoice == '0':
            os.system('cls')
            continue
        else:
            input('Invalid input, press Enter to continue...')
            os.system('cls')
            continue
    elif primaryMenuChoice == '6': #check out condition
            print('Your current total is: ${:.2f}'.format(custTotal))
            confirmCheckout = 'z'
            while confirmCheckout.lower() != 'y' or confirmCheckout.lower() !='n':
                confirmCheckout = input('Would you like to checkout (y/n)? ')
                if confirmCheckout == 'y':
                    cash = 0
                    while cash < custTotal:
                        os.system('cls')
                        print(name+"'s order on ("+str(formattedDateTime)+")\n\nYour current total: ${:.2f} // Current amout paid: ${:.2f}".format(custTotal, cash))
                        cash += int(input('Enter cash amount paid: '))
                        if cash >= custTotal:
                            os.system('cls')
                            print('Your change is: ${:.2f}'.format(cash - custTotal))
                            input("\nThanks for shopping at Raul's Taco Joint, "+name+"!\n\nPress Enter to continue...")
                            primaryMenuChoice = 0
                elif confirmCheckout == 'n':
                    primaryMenuChoice = -1 #reset
                    break
    elif primaryMenuChoice == '0': #break / exit condition
        os.system('cls')
        input("Exiting app, press Enter to continue...")
        break
    else:
        #error handle here. user should input value 1 -> 5
        input('Invalid input, press Enter to continue')
        os.system('cls')
        continue

    os.system('cls')

#testing
    #note: even tho itemChoice is only defined within the if statement, it can exist outside, like in the below print
#print('you chose item: '+itemChoice)