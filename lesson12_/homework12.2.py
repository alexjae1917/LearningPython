class Product():

    def __init__(self,name: str, price: int,type: str,country: str):
        self.name = name
        self.price = price
        self.type = type
        self.country = country

    def __str__(self):
        return f'{self.name} price: {self.price}'


class Purchaser():

    def __init__(self, first_name: str, last_name: str, patronymic: str, phone_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.first_name} {self.last_name}, phone number: {self.phone_number}'


class Order():

    def __init__(self, purchaser: Purchaser):
        self.purchaser = purchaser
        self.cart = {}
        self.total = 0

    def __str__(self):
        return f'{self.purchaser}\n{dict(self.cart)}'

    def add_item(self, item: Product, count: int):
        self.cart[item] = count

    def del_item(self, item: Product):
        for product,cnt in self.cart.items():
            if product == item:
                self.cart.pop(product)

    def get_total(self):
        self.total = 0
        for product, cnt in self.cart.items():
            self.total += (product.price * cnt)
        return self.total


user1 = Purchaser('Vasiliy','Vasiliev','Ivanovich',380975641020)
user2 = Purchaser('Ivan','Fedorov','Petrovich',380872649011)
user3 = Purchaser('Alexander','Makarov','Alexeevich',3809645342)

zebra = Product('Zebra DS', 2500, 'scaner', 'USA')
xprinter = Product('XPC 58 H', 3500, 'printer','China')
hpc = Product ('HPC 16s', 2100, 'cashbox', 'Lithuania')

cart1 = Order(user1)
cart2 = Order(user2)
cart3 = Order(user3)

cart1.add_item(zebra,5)
cart1.add_item(xprinter,4)
cart2.add_item(hpc,2)

print(cart1.get_total())

