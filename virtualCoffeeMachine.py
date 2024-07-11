# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
        },
        "cost": 60,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 30,
        },
        "cost": 70,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 40,
        },
        "cost": 80,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}
money = 0
coffee_maker = False


def money_checker():
    print("Please insert the money:")
    ten_ruppee_notes = int(input("Insert the Ten Rupee notes: "))
    twenty_ruppee_notes = int(input("Insert the Twenty Rupee notes: "))
    fifty_ruppee_notes = int(input("Insert the Fifty Rupee notes:  "))
    hundred_ruppee_notes = int(input("Insert the Hundred Rupee coins: "))
    user_coin_cost = ((ten_ruppee_notes * 10) + (twenty_ruppee_notes * 20) + (fifty_ruppee_notes * 50) + (hundred_ruppee_notes * 100))
    return user_coin_cost

logo = '''
              .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    ..  `:-===-===-===-===-===-:'
      .-._:                   :
        -.__.               ,' 
    ,--------"-------------'--------.
     `"--._                   _.--"'
            `""-------------""'


'''
print(logo)
statement = "----------ALL YOU NEED IS COFFEE!----------"
print(f"\t\t\t\t{statement}\t\t\t\t")
print("\n\n\n\n")
s = "WELCOME TO COFFEE MACHINE"
print(f"\t\t{s}\t\t")
print("\n\n\n")
while not coffee_maker:
    user_choice = input("What coffee do you want to order\n 1. espresso  :60/-\n 2. latte  :70/-\n 3. cappuccino  :80/-\n")
    if user_choice == "4":
        print(resources)
    elif user_choice == "1":
        if resources["water"] >= 50 and resources["coffee"] >= 20:
            user_money = money_checker()
            if user_money == 60:
                print("Take your coffee☕ \n!!Have a nice day!!")
            elif user_money > 60:
                user_change = round((user_money - 60), 2)
                print(f"Take your coffee☕,\nYour change is {user_change}\n!!Have a nice day!!")
            money += 60
            resources["amount"] = money
            resources["water"] -= 50
            resources["coffee"] -= 20
            if user_money < 60:
                print("Your transaction is failed and your money is refunded successfully")
        else:
            print("Sorry resources are not enough")
            coffee_maker = False
    elif user_choice == "2":
        if resources["water"] >= 200 and resources["coffee"] >= 30 and resources["milk"] >= 150:
            user_money = money_checker()
            if user_money == 70:
                print("Take your coffee☕,!!Have a nice day!!")
            elif user_money > 70:
                user_change = round((user_money - 70), 2)
                print(f"Take your coffee☕,\nYour change is {user_change} \n Have a nice day")
            money += 70
            resources["amount"] = money
            resources["water"] -= 200
            resources["coffee"] -= 30
            resources["milk"] -= 150
            if user_money < 70:
                print("Your transaction is failed and your money is refunded successfully")
        else:
            print("Sorry resources are not enough")
            coffee_maker = False

    elif user_choice == "3":
        if resources["water"] >= 250 and resources["coffee"] >= 40 and resources["milk"] >= 100:
            user_money = money_checker()
            if user_money == 80:
                print("Take your coffee☕,\n!!Have a nice day!!")
            elif user_money > 80:
                user_change = round((user_money - 80), 2)
                print("Take your coffee☕,")
                print("Your change is",user_change)
                print("!!Have a nice day!!")
            money += 80
            resources["amount"] = money
            resources["water"] -= 250
            resources["coffee"] -= 35
            resources["milk"] -= 100
            if user_money < 80:
                print("Your transaction is failed and your money is refunded successfully")
        else:
            print("Sorry resources are not enough")
            coffee_maker = False
    else:
        print("Please enter valid choice.")
        coffee_maker = False