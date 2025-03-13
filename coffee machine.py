print('welcome to the coffee machine')
coffe_available=True
while coffe_available:
    user_input=input('what would you like a latte , an expresso or a cappuccino \n').lower()
    # it's time to define the function for calculations of resources


    # defining the preset coffe machine data (I have modified this to make the project work and will change it back once I learn the trick from the solution):-
    preset_data={
        'water':300,
        'milk':200,
        'coffee':100,
        'money':'0 dollars'
    }

    latte={
        'water': 200,
        'coffee': 24,
        'milk':150
    }

    expresso={
        'water':50,
        'coffee':18
    }

    cappuccino={
        'water':250,
        'coffee':24,
        'milk':100,
    }
    money_quarter=int(input('how many quarters would you like to pay: '))
    money_dime=int(input('how many dimes would you like to pay: '))
    money_nickel=int(input('how many nickles would you like to pay: '))
    money_pennies=int(input('how many pennies would you like to pay: '))
    # now it's time for the currency above in the code:
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    pennie = 0.01
    total=money_pennies*pennie+money_dime*dime+money_quarter*quarter+money_nickel*nickel
    # now the real code starts
    if user_input=='report':
        print(preset_data)
    # the condition for latte has been done sucessfully
    if user_input=='latte' and preset_data['milk']-latte['milk']!=0 and  preset_data['coffee']-latte['coffee']!=0 and preset_data['water']-latte['water']!=0:
        if total==5:
            print('here is your latte ☕')
        elif total>5:
            change=total-5
            print(f'here is your change of {change}')
            print('here is your latte ☕')
        else:
            print('not enough money to give a cup of coffee')
    # time for expresso

    if user_input=='expresso'and preset_data['coffee']-expresso['coffee']!=0 and  preset_data['water']-expresso['water']!=0:
        if total==10:
            print(f'here is your {user_input} ☕')
        elif total>10:
            change=total-10
            print(f'here is your change of {change}')
            print(f'here is your {user_input} ☕')
        else:
            print('sorry not enough money to give you a cup of coffee')
    # now for cuppachino:
    if user_input=='cappuccino'and preset_data['milk']-cappuccino['milk']!=0 and  preset_data['coffee']-cappuccino['coffee']!=0 and  preset_data['water']-cappuccino['water']!=0:
            if total==15:
                print(f'here is your {user_input} ☕')
            elif total>15:
                change=total-15
                print(f'here is your change of {change}')
                print(f'here is your {user_input} ☕')
            else:
                print('sorry not enough money to give you a cup of coffee')
