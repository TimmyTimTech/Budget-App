class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        if amount > 0:
            self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount, payee):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {payee.name}")
            payee.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = f"*************{self.name:^14}*************\n"
        output += "date       || description               || amount\n"
        for item in self.ledger:
            output += f"{item['date']:<10} || {item['description']:<23} || {item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

#function to create the chart.
def create_spend_chart(categories):
    total_withdrawals = sum([category.get_balance() for category in categories if category.get_balance() < 0])
    percentages = [round(-category.get_balance() / total_withdrawals * 100, 2) for category in categories if category.get_balance() < 0]
    chart = "Percentage spent by category\n"
    chart += "100|           \n"
    chart += " 90|           \n"
    chart += " 80|           \n"
    chart += " 70|           \n"
    for i in range(60, -46, -10):
        line = str(i).ljust(3) + "| "
        for percentage in percentages:
            if i <= percentage < i + 10:
                line += "o "
            else:
                line += " "
        line += "\n"
        chart += line
    chart += "   -30 -20 -10    \n"
    chart += "    " + " ".join([category.name[0] for category in categories]) + "\n"
    chart += "    " + " ".join([category.name[1] for category in categories]) + "\n"
    chart += "    " + " ".join([category.name[2] for category in categories]) + "\n"
    chart += "    " + " ".join([category.name[3] for category in categories]) + "\n"
    chart += "    " + " ".join([category.name[4] for category in categories]) + "\n"
    return chart

