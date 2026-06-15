import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    option = ""

    while option != "off":
        # 1. Prompt user "What would you like? (small/ medium/ large/ off/ report)"
        option = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        valid_options = ["small", "medium", "large", "off", "report"]

        # handle off now since it wont render immediately in variable 
        if option == "off":
            break
        
        # handle not valid option 
        if option not in valid_options:
            print("Option invalid.")
            continue
        
        # handle report 
        if option == "report":
            print(sandwich_maker_instance.machine_resources)
            continue

        ingredients = recipes[option]["ingredients"]  # ingredient variable 
        cost = recipes[option]["cost"]  # sandwich cost variable

        # 2. Check that the resources are sufficient 
        if not sandwich_maker_instance.check_resources(ingredients):
            continue

        # 3. Process the inserted coins
        coins = cashier_instance.process_coins()

        # 4. Has the transaction been successful
        if not cashier_instance.transaction_result(coins, cost):
            continue

        # 5. Make sandwich
        sandwich_maker_instance.make_sandwich(option, ingredients)


if __name__ == "__main__":
    main()
