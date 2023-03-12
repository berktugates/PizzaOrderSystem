# Required libraries
import csv
import datetime

class Decorator():
    def __init__(self,description,price):
        self.description=description
        self.price=price

    def price(self):
        return f"The amount you will pay: {self.price}"  

    def description(self):
        return f"{self.description}"  


# I inherited the pizza superclass from the Decorator class.

class Pizza(Decorator):
    def __init__(self,name,price,description,type_of_sauce):
        self.name=name
        self.price=price
        self.description=description
        self.type_of_sauce=type_of_sauce


# I created subclasses of pizza

class ClassicPizza(Pizza):
    def __init__(self, name, price, description, type_of_sauce):
        super().__init__(name, price, description, type_of_sauce)

class Margherita(Pizza):
    def __init__(self, name, price, description, type_of_sauce):
        super().__init__(name, price, description, type_of_sauce)

class TurkishPizza(Pizza):
    def __init__(self, name, price, description, type_of_sauce):
        super().__init__(name, price, description, type_of_sauce)
    
class Plain(Pizza):
    def __init__(self, name, price, description, type_of_sauce):
        super().__init__(name, price, description, type_of_sauce)
    

# I inherited the sauce superclass from the Decorator class.

class Sauce(Decorator):
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description=description
    
# I created subclasses of sauce

class Olive(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)    

class Mushroom(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)        

class GoatCheese(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)        

class Meat(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)       

class Onion(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)        

class Corn(Sauce):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)        

# I create sauce objects

olive = Olive("Olive",10,"Sauce : Olive")
mushroom = Mushroom("Mushroom",15,"Sauce : Mushroom")
goat_cheese = GoatCheese("Goat Cheeese",30, "Sauce : Goat Cheese")
meat = Meat("Meat",50,"Sauce : Meat")
onion = Onion("Onion",20,"Sauce : Onion")
corn = Corn("Corn",25,"Sauce : Corn")

# Müşteri bilgilerini alıyorum.
class Customer():
    def __init__(self,name,surname,order_description):
        self.name=name
        self.surname=surname
        self.order_description=order_description

class Customer_Payment(Customer):
    def __init__(self, name, surname, order_description,card_no,card_pass):
        super().__init__(name, surname, order_description)
        self.card_no=card_no
        self.card_pass=card_pass

def main():
    print("* Please select a pizza base:\n\n 1: Classic Pizza\n 2: Margherita Pizza\n 3: Turkish Pizza\n 4: Plain Pizza\n\n *  Sauce of your choice:\n\n 11: Olive\n 12: Mushroom\n 13: Goat Cheese\n 14: Meat\n 15: Onion\n 16: Corn ")
    pizza_selection=int(input("Please select the pizza you want to order:"))
    sauce_selection=int(input("Please select the sauce you want to choose:"))
    if 0<pizza_selection<5 and 10<sauce_selection<17:
        if pizza_selection == 1:
            classic_pizza = ClassicPizza("Classic Pizza",140,"Pizza Type : Classic Pizza",sauce_selection)
            total_price = classic_pizza.price
        elif pizza_selection == 2:
            margherita_pizza = Margherita("Margherita Pizza",150,"Pizza Type : Margherita Pizza",sauce_selection)
            total_price = margherita_pizza.price
        elif pizza_selection == 3:
            turkish_pizza = TurkishPizza("Turkish Pizza",270,"Pizza Type : Turkish Pizza",sauce_selection)
            total_price = turkish_pizza.price
        elif pizza_selection == 4:
            plain_pizza = Plain("Plain Pizza",120,"Pizza Type : Plain Pizza",sauce_selection)
            total_price = plain_pizza.price

    else:
        return f"Hatalı seçim yaptınız."

    
main()