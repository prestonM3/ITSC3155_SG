class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert money.")

        dollar = int(input("How many dollars?: "))
        quarter = int(input("How many quarters?: "))
        nickel = int(input("How many nickels?: "))
        dime = int(input("How many dimes?: "))

        if dollar < 0 or quarter < 0 or nickel < 0 or dime < 0:
            print("Invalid amount, cant have negative amounts.")
            return 0

        total = (
            dollar * 1.00 +
            quarter * 0.25 +
            nickel * 0.05 +
            dime * 0.10
        )

        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded if applicable.")
            return False
        
        if coins > cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change")
        
        if coins == cost:
            print("No change.")

        return True
