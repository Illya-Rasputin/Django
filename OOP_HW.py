import math


class Money:
    def __init__(self, whole=0, cents=0):
        self.whole = whole
        self.cents = cents
        self.normalize()

    def normalize(self):
        self.whole += self.cents // 100
        self.cents %= 100

    def set_whole(self, value):
        self.whole = value

    def set_cents(self, value):
        self.cents = value
        self.normalize()

    def get_whole(self):
        return self.whole

    def get_cents(self):
        return self.cents

    def print_money(self):
        print(f"{self.whole}.{self.cents:02d}")

    def decrease(self, whole, cents):
        total = self.whole * 100 + self.cents - whole * 100 - cents
        self.whole = total // 100
        self.cents = total % 100


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def decrease_price(self, whole, cents):
        self.price.decrease(whole, cents)

    def print_product(self):
        print(f"Product: {self.name}, price: ", end="")
        self.price.print_money()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.length() < other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def print_circle(self):
        print(f"Radius: {self.radius}, circumference: {self.length():.2f}")

class Airplane:
    def __init__(self, airplane_type, passengers, max_passengers):
        self.airplane_type = airplane_type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __add__(self, count):
        result = Airplane(
            self.airplane_type,
            self.passengers,
            self.max_passengers
        )

        result.passengers += count

        if result.passengers > result.max_passengers:
            result.passengers = result.max_passengers

        return result

    def __sub__(self, count):
        result = Airplane(
            self.airplane_type,
            self.passengers,
            self.max_passengers
        )

        result.passengers -= count

        if result.passengers < 0:
            result.passengers = 0

        return result

    def __iadd__(self, count):
        self.passengers += count

        if self.passengers > self.max_passengers:
            self.passengers = self.max_passengers

        return self

    def __isub__(self, count):
        self.passengers -= count

        if self.passengers < 0:
            self.passengers = 0

        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def print_airplane(self):
        print(f"{self.airplane_type}: {self.passengers}/{self.max_passengers} passengers")

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def print_flat(self):
        print(f"Flat: {self.area} m², {self.price} UAH")


# Short checks
money = Money(100, 50)
money.set_whole(200)
money.set_cents(75)
money.decrease(10, 25)
print("Money:", end=" ")
money.print_money()

product = Product("Laptop", Money(25000, 50))
product.decrease_price(1000, 50)
product.print_product()

circle = Circle(5)
circle += 3
print("Circle:", end=" ")
circle.print_circle()
print("Circle comparison:", Circle(5) < Circle(10))

airplane = Airplane("Boeing 737", 100, 180)
airplane += 30
airplane -= 20
print("Airplane:", end=" ")
airplane.print_airplane()
print("Airplane comparison:", airplane < Airplane("Airbus A320", 120, 200))

flat1 = Flat(50, 1500000)
flat2 = Flat(70, 2000000)
print("Flat 1:", end=" ")
flat1.print_flat()
print("Flat comparison:", flat1 != flat2 and flat1 < flat2)