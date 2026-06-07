### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items(): # item = bread, ham, etc # amount = 3, 12, etc
            if self.machine_resources[item] < amount: # check resources against actual recipe amounts
                print(f"Sorry there is not enough {item}.")
                return False
        return True 
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        print("Please Insert Money.")

        large = int(input("How many large Dollars?: "))
        half = int(input("How many half Dollars?: "))
        quarter = int(input("How many quarters Dollars?: "))
        nickel = int(input("How many nickels Dollars?: "))

        # negative check
        if large < 0 or half < 0 or quarter < 0 or nickel < 0:
            print("Invalid amount, cant have negative amounts.")
            return 0

        total = (large * 1.00) + (half * .50) + (quarter * .25)+ (nickel * .05)
        return total
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        if coins < cost: 
            print("Sorry that's not enough money. Money refunded if applicable. ")
            return False
        
        if coins > cost: 
            change = coins - cost
            print(f"Here is ${change:.2f} in change")
        
        if coins == cost: 
            print("No change.")

        return True
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount 
        
        print(f"{sandwich_size} sandwich is ready. Bon appet")
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine = SandwichMachine(resources) # initialized with resources 
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
        print(sandwichMachine.machine_resources)
        continue

    ingredients = recipes[option]["ingredients"] # ingredient variable 
    cost = recipes[option]["cost"] # sandwich cost variable w

    # 2. Check that the resources are sufficient 
    if not sandwichMachine.check_resources(ingredients):
        continue

    # 3. Process the inserted coins
    coins = sandwichMachine.process_coins()

    # 4. Has the transaction been successful
    if not sandwichMachine.transaction_result(coins, cost):
        continue

    # 5. Make sandwich
    sandwichMachine.make_sandwich(option, ingredients)



