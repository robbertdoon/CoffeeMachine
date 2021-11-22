from coffee_data import MENU, resources, profit


def check_resources(drink):
    counter = 0
    nr_of_ingredients = len(MENU[drink]['ingredients'])
    for i in MENU[drink]['ingredients']:
        ingredient = i
        amount = MENU[drink]['ingredients'][ingredient]
        if resources[ingredient] >= amount:
            counter += 1

    # als genoeg resources, dan moet je maken
    if counter == nr_of_ingredients:
        enough_money = insert_coins(drink)
        if enough_money:
            for i in MENU[drink]['ingredients']:
                ingredient = i
                amount = MENU[drink]['ingredients'][ingredient]
                resources[ingredient] -= amount
            # print(counter)
            print(f'Here is your {drink.title()}. Enjoy!')
        # else:
        #     print('Sorry that\'s not enough money. Money refunded.')
    # niet genoeg resources
    else:
        for i in MENU[drink]['ingredients']:
            ingredient = i
            amount = MENU[drink]['ingredients'][ingredient]
            if resources[ingredient] < amount:
                print(f'Sorry, there is not enough {ingredient}.')
            # print(resources)


def insert_coins(drink):
    global profit
    print('Please insert coins.')
    price = MENU[drink]['cost']

    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickles = float(input('How many nickles?: '))
    pennies = float(input('How many pennies?: '))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"You inserted ${format(total, '.2f')}")

    change = total - price

    if total >= price:
        profit += price
        if total > price:
            print(f"Here is ${format(change, '.2f')} change.")
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


is_turned_on = True

while is_turned_on:

    choice = input(' What would you like? (espresso/latte/cappuccino): ')

    # turn machine off
    if choice == 'off':
        print('Machine turning off...')
        is_turned_on = False
    # check resources
    elif choice == 'report':
        for i in resources:
            if i == 'water' or i == 'milk':
                print(f'{i}: {resources[i]}ml')
            elif i == 'coffee':
                print(f'{i}: {resources[i]}gr')
        print(f"money: ${format(profit, '.2f')}")
    # check for correct choice
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        check_resources(choice)
    # any other choice
    else:
        print(f'{choice} is not a valid choice, try again.')