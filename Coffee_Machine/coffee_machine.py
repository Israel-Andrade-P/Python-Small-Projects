from data import MENU

resources = {"water":300, "milk":200, "coffee":100}
money = 0

def get_report():
    return f"Water: {resources['water']}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")    

def check_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True


def proccess_coins():
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def get_order():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino) ")
        if user_input == "report":
            print(get_report())
            continue
        elif user_input == "off":
            print("Goodbye!")
            break
        elif user_input in MENU:
            menu = MENU[user_input]
            if check_resource(menu["ingredients"]):
                payment = proccess_coins()
                if is_transaction_successful(payment, menu["cost"]):
                    make_coffee(user_input ,MENU[user_input]["ingredients"])
                    continue
            else:
                continue
        else:
            print(f"Sorry, we don't have {user_input} in our menu.")
            continue

get_order()
            



 



