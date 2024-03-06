class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
    
    def __str__(self):
        category_display = self.category_name.center(30, "*") + "\n"
        for transaction in self.ledger:
            category_display += f"{transaction['description'][:23]:23}" + f"{transaction['amount']:>7.2f}" + "\n"
        category_display += f"Total: {self.get_balance():.2f}"
        return category_display
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(transaction['amount'] for transaction in self.ledger)
    
    def transfer(self, amount, destination_budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_budget_category.category_name}")
            destination_budget_category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    # Calculate total spent in each category
    spent_amounts = [sum(abs(item["amount"]) for item in category.ledger if item["amount"] < 0) for category in categories]

    # Calculate percentage rounded down to the nearest 10
    total_spent = sum(spent_amounts)
    spent_percentages = [(int(amount / total_spent * 100) // 10) * 10 for amount in spent_amounts]

    # Create the bar chart substrings
    header = "Percentage spent by category\n"
    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        chart += ''.join(' o ' if percent >= value else '   ' for percent in spent_percentages)
        chart += " \n"

    footer = "    " + "-" * (3 * len(categories) + 1) + "\n"
    # Use category names instead of descriptions
    category_names = [category.category_name for category in categories]
    max_length = max(len(name) for name in category_names)
    # Format category names
    footer += '\n'.join("    " + ''.join((name[i] if i < len(name) else ' ').center(3) for name in category_names) + " " for i in range(max_length))
    
    return (header + chart + footer).rstrip("\n")

# Testing the function with sample data
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)

print(create_spend_chart([food, clothing]))