
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items(): # item = bread, ham, etc # amount = 3, 12, etc
            if self.machine_resources[item] < amount: # check resources against actual recipe amounts
                print(f"Sorry there is not enough {item}.")
                return False
        return True 

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount 
        
        print(f"{sandwich_size} sandwich is ready. Bon appet")
        """Deduct the required ingredients from the resources.
           Hint: no output"""