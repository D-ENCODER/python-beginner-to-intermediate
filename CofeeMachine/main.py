class CoffeeMachine:
    def __init__(self):
        self.money = 0
        self.water = 500
        self.milk = 250
        self.coffee = 200

    def report(self):
        print("Water: " + str(self.water))
        print("Money: " + str(self.money))
        print("Milk: " + str(self.milk))
        print("Coffee: " + str(self.coffee))

    def cappuccino(self, money):
        if self.requirements(money_needed=3, money_given=money, water=250, milk=100, coffee=24) == 1:
            return 0
        self.money += 3.0
        self.water -= 250
        self.coffee -= 24
        self.milk -= 100
        print("Cappuccino is ready !!!")
        if (money - 3.0) != 0:
            print("Change: " + str(money - 3.0))

    def espresso(self, money):
        if self.requirements(money_needed=1.5, money_given=money, water=50, coffee=18) == 1:
            return 0
        self.money += 1.5
        self.water -= 50
        self.coffee -= 18
        print("Espresso is ready !!!")
        if (money - 1.5) != 0:
            print("Change: " + str(money - 1.5))

    def latte(self, money):
        if self.requirements(money_needed=2.5, money_given=money, water=200, milk=150, coffee=24) == 1:
            return 0
        self.money += 2.5
        self.water -= 200
        self.coffee -= 24
        self.milk -= 150
        print("Latte is ready !!!")
        if (money - 2.5) != 0:
            print("Change: " + str(money - 2.5))

    def requirements(self, money_needed=0.0, money_given=0.0, water=0, milk=0, coffee=0):
        if money_given < money_needed:
            print("Less Money !!!")
            return 1
        elif self.water < water:
            print("Water needed !!!")
            return 1
        elif self.coffee < coffee:
            print("Coffee needed !!!")
            return 1
        elif self.milk < milk:
            print("Milk needed !!!")
            return 1
        return 0


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            coffee_machine.report()
        elif choice == "espresso":
            money = float(input("Enter the money: "))
            coffee_machine.espresso(money)
        elif choice == "latte":
            money = float(input("Enter the money: "))
            coffee_machine.latte(money)
        elif choice == "cappuccino":
            money = float(input("Enter the money: "))
            coffee_machine.cappuccino(money)
        elif choice == "Off" or choice == "off":
            print("Shutting Down See ya !!!")
            break
        else:
            print("Invalid Choice !!!")
