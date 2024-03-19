from utils import utils


class Category:
    name : str
    description : str
    products : list
    nummer_of_category = 0
    nummer_of_products = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.nummer_of_category += 1
        # Category.nummer_of_products += len(self.products)
    #
    #
    # def __repr__(self):
    #     return f"{self.name} \n{self.products[0]} \n"
