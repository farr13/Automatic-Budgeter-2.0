class History:
    """This class holds information used to track the payment history of the user"""
    def __init__(self, amount_spent, description, category_name, date):
        self.amount_spent = amount_spent
        self.description = description
        self.category_name = category_name
        self.date = date
    