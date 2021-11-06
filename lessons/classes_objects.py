"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""


    # Attribute definitions
    size: str
    toppings: int
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        self.size = size
        self.toppings = toppings



    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * .75

        if self.extra_cheese:
            total += 1

        total *= tax
        
        return total

a_Pizza = Pizza("large", 3)
a_Pizza.size = "large"
a_Pizza.toppings = 3

print(Pizza)
print(a_Pizza)
print(a_Pizza.size)
print(f"Price ${a_Pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price ${another_pizza.price(1.05)}")