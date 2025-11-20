# Landscaper

## You are starting a landscaping business, but all you have are your teeth.
## Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.
## As you cut grass, and accumulate money... You may chose to purchase new lawncutting tools! These tools will increase your income per lawn!

# I'll be using tupples to store values for the tools available and tool price as those will remain fixed values
toolsAvailable = ("teeth", "rusty scissors", "push lawnmower", "battery-powered lawnmower", "students")
toolPrice = (0, 25, 50, 250, 500)
toolEfficiency = (5, 10, 20, 35, 50)
# Tools owned, however, will be set as a list since there can be many of each kind owned.
toolsOwned = [1, 0, 0, 0, 0]
money = 0

def store():
  global money
  global toolsAvailable
  global toolPrice
  global toolEfficiency
  global toolsOwned

  print("\nWelcome to the landscaping store!")
  print("Simply say a number to make a selection.")

  for index in range(1, len(toolsOwned)):
    print(str(index) + " - " + toolsAvailable[index] + " : $" + str(toolPrice[index]) + " (" + str(toolsOwned[index]) + " owned)")

  print("5 - Exit Shop")
  print("\nYou have $" + str(money) + ".")
  print("What would you like to do?")
  user_input = input("> ")

  for index in range(1, len(toolsOwned)):
    if user_input == str(index): ## Valid Input
      if money >= toolPrice[index]: ## Purchase
        money -= toolPrice[index]
        toolsOwned[index] += 1
      
      else: ## Too Broke
        print("Sorry, but it looks like you cant afford that!")
        store()
    
    elif user_input == "5":
      print("Thanks for stopping by!")

    else: ## Invalid Input
      print("Sorry, I didn't quite get that...")
      store()

store()