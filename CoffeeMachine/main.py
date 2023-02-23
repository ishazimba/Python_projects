MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0

def coins():
  total=int(input("How many quarters? "))*0.25
  total+= int(input("How many dime? ")) *0.10
  total+=int(input("How many nickel? "))*0.05
  total+=int(input("How many penny? "))*0.01
  return total

def confirm_transaction(user_payment, drink_cost):
  change=0
  if user_payment>=drink_cost:
    change= user_payment-drink_cost
    global profit
    profit+=drink_cost
    print(f"Here is your change: {change}")
    return True
  else:
    print("Sorry the money is not enough. Here is your refund")
    return False

def check_resources(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"​Sorry there is not enough {item}.")
      return False
    return True

def make_coffee(drink_name, order_ingredient):
  for item in order_ingredient:
    resources[item]-=order_ingredient[item]
  print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on=True
while is_on:
  user_input=input("What would you like? 'Espresso', 'Latte', 'Cappuccino': ").lower()
  cost=0
  if user_input=="off":
    is_on=False
  elif user_input=="report":
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${profit}")

  else:
    drink=MENU[user_input] #coffee ko details
    if check_resources(drink["ingredients"]):

      print("Please insert coins. ")

      #print(drink["cost"]) #drink ko cost nikalcha
      payment=coins()
      if confirm_transaction(payment, drink["cost"]):
        make_coffee(user_input,drink["ingredients"] )












