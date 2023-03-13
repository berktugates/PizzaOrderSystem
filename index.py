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


# The Pizza superclass is inherited from the decorator class

class Pizza(Decorator):
    def __init__(self,name,price,description,type_of_sauce):
        self.name=name
        self.price=price
        self.description=description
        self.type_of_sauce=type_of_sauce


# Subclasses of Pizza class were created

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
    

# The Sauce superclass is inherited from the decorator class

class Sauce(Decorator):
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description=description
    
# Subclasses of sos class created

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

# Sauce objects created

olive = Olive("Olive",10,"Sauce : Olive")
mushroom = Mushroom("Mushroom",15,"Sauce : Mushroom")
goat_cheese = GoatCheese("Goat Cheeese",30, "Sauce : Goat Cheese")
meat = Meat("Meat",50,"Sauce : Meat")
onion = Onion("Onion",20,"Sauce : Onion")
corn = Corn("Corn",25,"Sauce : Corn")

# Customer information received
class Customer():
    def __init__(self,tc,name,surname,order_description):
        self.tc=tc
        self.name=name
        self.surname=surname
        self.order_description=order_description

class Customer_Payment(Customer):
    def __init__(self,tc, name, surname, order_description,card_no,card_pass):
        super().__init__(tc,name, surname, order_description)
        self.card_no=card_no
        self.card_pass=card_pass

def main():
    print("* Please select a pizza base:\n\n 1: Classic Pizza\n 2: Margherita Pizza\n 3: Turkish Pizza\n 4: Plain Pizza\n\n *  Sauce of your choice:\n\n 11: Olive\n 12: Mushroom\n 13: Goat Cheese\n 14: Meat\n 15: Onion\n 16: Corn ")
    pizza_selection=int(input("Please select the pizza you want to order:"))
    sauce_selection=int(input("Please select the sauce you want to choose:"))
    if 0<pizza_selection<5 and 10<sauce_selection<17:
        if pizza_selection == 1:
            classic_pizza = ClassicPizza("Classic Pizza",140,"Pizza Type : Classic Pizza",sauce_selection)
            if sauce_selection == 11:
                total_price = int(classic_pizza.price) + int(olive.price)
            elif sauce_selection == 12:
                total_price = int(classic_pizza.price) + int(mushroom.price)
            elif sauce_selection == 13:
                total_price = int(classic_pizza.price) + int(goat_cheese.price)
            elif sauce_selection == 14:
                total_price = int(classic_pizza.price) + int(meat.price)
            elif sauce_selection == 15:
                total_price = int(classic_pizza.price) + int(onion.price)
            elif sauce_selection == 16:
                total_price = int(classic_pizza.price) + int(corn.price)                    
        elif pizza_selection == 2:
            margherita_pizza = Margherita("Margherita Pizza",150,"Pizza Type : Margherita Pizza",sauce_selection)
            if sauce_selection == 11:
                total_price = int(margherita_pizza.price) + int(olive.price)
            elif sauce_selection == 12:
                total_price = int(margherita_pizza.price) + int(mushroom.price)
            elif sauce_selection == 13:
                total_price = int(margherita_pizza.price) + int(goat_cheese.price)
            elif sauce_selection == 14:
                total_price = int(margherita_pizza.price) + int(meat.price)
            elif sauce_selection == 15:
                total_price = int(margherita_pizza.price) + int(onion.price)
            elif sauce_selection == 16:
                total_price = int(margherita_pizza.price) + int(corn.price)
        elif pizza_selection == 3:
            turkish_pizza = TurkishPizza("Turkish Pizza",270,"Pizza Type : Turkish Pizza",sauce_selection)
            if sauce_selection == 11:
                total_price = int(turkish_pizza.price) + int(olive.price)
            elif sauce_selection == 12:
                total_price = int(turkish_pizza.price) + int(mushroom.price)
            elif sauce_selection == 13:
                total_price = int(turkish_pizza.price) + int(goat_cheese.price)
            elif sauce_selection == 14:
                total_price = int(turkish_pizza.price) + int(meat.price)
            elif sauce_selection == 15:
                total_price = int(turkish_pizza.price) + int(onion.price)
            elif sauce_selection == 16:
                total_price = int(turkish_pizza.price) + int(corn.price)
        elif pizza_selection == 4:
            plain_pizza = Plain("Plain Pizza",120,"Pizza Type : Plain Pizza",sauce_selection)
            if sauce_selection == 11:
                total_price = int(plain_pizza.price) + int(olive.price)
            elif sauce_selection == 12:
                total_price = int(plain_pizza.price) + int(mushroom.price)
            elif sauce_selection == 13:
                total_price = int(plain_pizza.price) + int(goat_cheese.price)
            elif sauce_selection == 14:
                total_price = int(plain_pizza.price) + int(meat.price)
            elif sauce_selection == 15:
                total_price = int(plain_pizza.price) + int(onion.price)
            elif sauce_selection == 16:
                total_price = int(plain_pizza.price) + int(corn.price)

    else:
        return f"Hatalı seçim yaptınız!"

# User information received.  
    customer_name = Customer(input("Please enter your TC number:"),input("Please enter your name:"),input("Please enter your surname:"),input("Please enter your order description:"))
    customer_payment = Customer_Payment(customer_name.tc,customer_name.name,customer_name.surname,customer_name.order_description,input("Please enter your card number:"),input("Please enter your card password:"))
    customer_info = ["TC:"+customer_name.tc,"Name:"+customer_name.name,"Surname:"+customer_name.surname,"Order Description:"+customer_name.order_description,"Card-No"+customer_payment.card_no,"Card-Password"+customer_payment.card_pass]
# The fee to be paid by the customer is printed on the screen  
    print(f"Fee you have to pay: {total_price}. Enjoy your meal!")

# Data was written to csv file
    csvFile = open("Orders_Database.csv","w",newline='') 
    writer = csv.writer(csvFile,delimiter='|')
    writer.writerow(customer_info)


main()