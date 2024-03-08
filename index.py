#Raul's Taco Joint
#very hungry when i made this mmmmm yummy

import os #imports cls

#initialize primary menu choice to access while loop
primaryMenuChoice = -1

#receive customer's name
name = input('Name for order: ')

os.system('cls')

#define cost for each meat item
chicken = 9.00
carneAsada = 10.00
alPastor = 9.50
vegetarian = 8.00
carnitas = 10.50
barbacoa = 11.00

custTotal = 0

while primaryMenuChoice != 0:
    primaryMenuChoice = input("Raul's menu:\n\t1 - Tacos\n\t2 - Burritos\n\t3 - House Specialties\n\t4 - Bowls\n\t5 - Nachos\n\t0 - Exit\n\n(Current total: ${:.2f})\n\nMenu Choice: ".format(custTotal)) #use double quotes to include apostraphe

    #dont convert primaryMenuChoice to int read below

    os.system('cls')
    #handle for each menu choice. price scales flat between each option
    if primaryMenuChoice == '1': #Taco code // keeping primaryMenuChoice a string allows error handling for if user inputs string. if it was an int and user input a string, it would return error. now, it routes to else statement
        inc = .5  # inc is the price increase for getting a different type of menu item like taco, burrito, etc
        itemChoice = input("Raul's Tacos (3 per order):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        else:
            input('Invalid input, press Enter to continue...')
            continue
    elif primaryMenuChoice == '2': #Burrito code
        inc = 1
        itemChoice = input("Raul's Burritos:\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada (${:.2f})\n\t3 - Al Pastor (${:.2f})\n\t4 - Vegetarian (${:.2f})\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        else:
            input('Invalid input, press Enter to continue...')
            continue
    elif primaryMenuChoice == '3': #House code
        itemChoice = input("Raul's House Specialties:\n\t1 - Fajita Quesadilla ($11.50)\n\t2 - Shrimp Enchilada ($12.00)\n\t3 - Tamales ($8.50)\n\t4 - Gordita ($9.50)\n")
        if itemChoice == '1':
            custTotal += 11.5
        elif itemChoice == '2':
            custTotal += 12
        elif itemChoice == '3':
            custTotal += 8.5
        elif itemChoice == '4':
            custTotal += 9.5
        else:
            input('Invalid input, press Enter to continue...')
            continue
    elif primaryMenuChoice == '4': #Bowls code
        inc = 0 #bowls are base price
        itemChoice = input("Raul's Bowls (comes with rice, lettuce, pico de gallo, beans):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n".format(chicken, carneAsada, alPastor, vegetarian))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        else:
            input('Invalid input, press Enter to continue...')
            continue
    elif primaryMenuChoice == '5': #Nachos Code
        inc = 1.5
        itemChoice = input("Raul's Nachos (comes with chips, salsa, peppers, jalapenos, olives, sour cream):\n\t1 - Chicken (${:.2f})\n\t2 - Carne Asada(${:.2f})\n\t3 - Al Pastor(${:.2f})\n\t4 - Vegetarian(${:.2f})\n".format(chicken + inc, carneAsada + inc, alPastor + inc, vegetarian + inc))
        if itemChoice == '1':
            custTotal += chicken + inc
        elif itemChoice == '2':
            custTotal += carneAsada + inc
        elif itemChoice == '3':
            custTotal += alPastor + inc
        elif itemChoice == '4':
            custTotal += vegetarian + inc
        else:
            input('Invalid input, press Enter to continue...')
            continue
    elif primaryMenuChoice == '0': #break / exit condition
        os.system('cls')
        input("Exiting app, press Enter to continue...")
        break
    else:
        #error handle here. user should input value 1 -> 5
        input('Invalid input, press Enter to continue')
        os.system('cls')
        continue
    
    #reset menu choice
    
    print('Current Total: ${:.2f}'.format(custTotal))
    input("Press Enter to continue...")

    os.system('cls')

#testing
    #note: even tho itemChoice is only defined within the if statement, it can exist outside, like in the below print
#print('you chose item: '+itemChoice)