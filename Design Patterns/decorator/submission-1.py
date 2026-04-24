class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.coffee = decoratedCoffee

    def getCost(self):
        return self.coffee.getCost()

class MilkDecorator(CoffeeDecorator):
    # Implement the Milk decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return 0.5 + self.coffee.getCost()

class SugarDecorator(CoffeeDecorator):
    # Implement the Sugar decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return 0.2 + self.coffee.getCost()

class CreamDecorator(CoffeeDecorator):
    # Implement the Cream decorator
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return 0.7 + self.coffee.getCost()

