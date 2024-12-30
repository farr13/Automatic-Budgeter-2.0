class Category:
    """
    This class stores the information for a specific budgeting category
    """
    def __init__(self, name, money_allocated):
        self.name = name
        self.money_allocated = money_allocated 
    
    def change_allocation(self, amount):
        """ Changes allocation of money for the specified category

         amount: money subtracted from category total
        """
        self.money_allocated - amount