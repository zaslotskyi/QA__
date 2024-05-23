class Grocery:

    def __init__(self, product_name: str, price: int, count: int):
        self.product_name = product_name
        self.price = price
        self.count = count

    def add_product(self, quantity: int):
        """
        method adds the specified number of products to the total number
        :param quantity: the number of products to add
        :return: total number of products
        """
        self.count += quantity

    def total_price_of_product(self):
        """
        method calculates the total price of the product
        :return: total price
        """

        total_price = self.price * self.count

        return total_price

    @staticmethod
    def purchase_opportunity(price_per_unit: int, amount: int):
        """
        The method calculates how much it will cost to purchase the specified number of products
        :param price_per_unit: the price of one product
        :param amount: quantity of the product to be purchased
        :return: the purchase price
        """

        final_price = price_per_unit * amount

        return f'To buy {amount} products, you need {final_price} hryvnias'


apple = Grocery('apple', 10, 20)
print(apple.count)
apple.add_product(4)
print(apple.count)
print(Grocery.purchase_opportunity(10, 30))

lemon = Grocery('lemon', 5, 30)
print(lemon.total_price_of_product())
