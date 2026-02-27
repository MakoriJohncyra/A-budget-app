class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """Add a deposit to the ledger"""
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        """Add a withdrawal (negative amount) to the ledger if funds are available"""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """Calculate current balance based on ledger entries"""
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def transfer(self, amount, category):
        """Transfer amount to another category"""
        if self.check_funds(amount):
            # Withdraw from current category
            self.withdraw(amount, f"Transfer to {category.name}")
            # Deposit to destination category
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        """Check if amount is available in balance"""
        return amount <= self.get_balance()
    
    def __str__(self):
        """Format the category for printing"""
        # Title line with category name centered between *
        title = f"{self.name:*^30}\n"
        
        # Ledger entries
        items = ""
        for item in self.ledger:
            # Description: max 23 characters
            description = item["description"][:23]
            
            # Amount: 2 decimal places, right-aligned, max 7 characters
            amount = f"{item['amount']:.2f}"
            
            # Calculate spacing
            items += f"{description:<23}{amount:>7}\n"
        
        # Total line
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total


def create_spend_chart(categories):
    """Create a bar chart showing spending percentages by category"""
    
    # Calculate total spent and percentages
    total_spent = 0
    category_spent = {}
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:  # Only count withdrawals (negative amounts)
                spent += abs(item["amount"])
        category_spent[category.name] = spent
        total_spent += spent
    
    # Calculate percentages (rounded down to nearest 10)
    percentages = {}
    for name, spent in category_spent.items():
        if total_spent > 0:
            percentage = int((spent / total_spent) * 100)
            # Round down to nearest 10
            percentage = (percentage // 10) * 10
        else:
            percentage = 0
        percentages[name] = percentage
    
    # Build the chart
    chart = "Percentage spent by category\n"
    
    # Y-axis from 100 down to 0
    for i in range(100, -1, -10):
        # Y-axis label
        chart += f"{i:>3}| "
        
        # Bars for each category
        for category in categories:
            if percentages[category.name] >= i:
                chart += "o  "
            else:
                chart += "   "
        
        chart += "\n"
    
    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Category names vertically
    # Find the longest category name
    max_len = max(len(category.name) for category in categories)
    
    # Write names vertically
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
    
    return chart


# Example usage and testing
if __name__ == "__main__":
    # Test the Category class
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    
    print(food)
    print()
    print(clothing)
    print()
    
    # Test the create_spend_chart function
    entertainment = Category('Entertainment')
    entertainment.deposit(500, 'initial deposit')
    entertainment.withdraw(75.50, 'movies')
    
    categories = [food, clothing, entertainment]
    print(create_spend_chart(categories))


