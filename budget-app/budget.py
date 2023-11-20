class Category:
      # Executed when the class is being initiated
      def __init__(self, name):
            # Instance variables
            self.name = name
            self.ledger = []
      
      # Deposit method
      def deposit(self, amount, description=""):
            self.ledger.append({"amount": amount, "description": description})
            
      # Withdraw method
      def withdraw(self, amount, description=""):
            if self.check_funds(amount):
                  self.ledger.append({"amount": -amount, "description": description}) 
                  return True
            else:
                  return False        

      # Check funds method
      def check_funds(self, amount):
            if amount > self.get_balance():
                  return False
            else:
                  return True

      # Get_balance method
      def get_balance(self):
            running_total = 0
            for x in self.ledger:
                  running_total += x["amount"]
            return round(running_total, 2)
      
      # Transfer method
      def transfer(self, amount, category):
            if self.check_funds(amount):
                  self.withdraw(amount, f"Transfer to {category.name}")
                  category.deposit(amount, f"Transfer from {self.name}")
                  return True
            else:
                  return False
            
      # Controls what is returns when the class object is represented as a string
      def __str__(self):
            width = 30
            line_break = "\n"
            
            def generate_title():
                  asterisk = "*"
                  padding = width - len(self.name)
                  left_padding = padding // 2
                  right_padding = padding - left_padding
                  title = asterisk * left_padding + self.name + asterisk * right_padding
                  return title + line_break
            
            def generate_ledger_item(item):
                  description = item["description"][:23]
                  amount = str("{:.2f}".format(item["amount"]))[:7]
                  ledger_item_string = f"{description}{amount.rjust(width - len(description))}\n"
                  return ledger_item_string
            
            def generate_ledger_item_string():
                  lines = [generate_ledger_item(item) for item in self.ledger]
                  return "".join(lines)
            
            
            title = generate_title()
            ledger_items = generate_ledger_item_string()
            t = "{:.2f}".format(self.get_balance())
            total = f"Total: {t}"
            
            result = f"{title}{ledger_items}{total}"
            return result

business = Category("business")
food = Category("food")
entertainment = Category("entertainment")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# takes a list of categories and returns a string that is a bar chart
def create_spend_chart(categories):
      
      # find total amount spent across categories
      def calculate_total_spent():
            total_spent = 0
            for category in categories:
                  total_spent += calculate_amount_spent_in_category(category)
            return total_spent
      
      # calculate total spent by a given category
      def calculate_amount_spent_in_category(category):
            spent = sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0)
            return spent
      
      # calculate percentage spent by each category
      percentages = []
      for category in categories:
            percentage = calculate_amount_spent_in_category(category) / calculate_total_spent() * 100
            percentages.append(percentage)
            
      print("percentages", percentages)
            
      # Create bar chart string
      # Title
      chart = "Percentage spent by category\n"
      
      # y axis and bars
      for value in range(100, -1, -10):
        chart += str(value).rjust(3) + "| "
        for percentage in percentages:
            chart += "o" if percentage >= value else " "
            chart += "  "  # Add spacing between bars
        chart += "\n"
      
      # x axis and category names
      # x axis dashes line
      chart += "    " + "---" * len(categories) + "-\n"
      
      # find the longest category name to know how big the loop range should be
      max_len = max(len(category.name) for category in categories)
      
      # for the length of the longest category name, add beginning five spaces (plus one space before first letter), then each letter followed by a space
      for i in range(max_len):
            chart += "     "
            for category in categories:
                  # if there is a letter available (i < length of category name), add that letter, followed by two spaces
                  if i < len(category.name):
                        if i == 0:
                              chart += category.name[i].capitalize()
                        else:
                              chart += category.name[i]
                        chart += "  "
                        
                  # if there is no letter available (i > length of category name), add three spaces
                  else:
                        chart += "   "
            if i < max_len - 1:
                  chart += "\n"
      
      print(repr(chart))
      return chart

print(create_spend_chart([business, food, entertainment]))
