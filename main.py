class Items:
    pay_rate = 0.85
    all = []

    def __init__(self, product, price, amount):
        self.product = product
        self.price = price
        self.amount = amount

    def calculate_total_price(self):
        '''получение общей стоимости конкретного товара в магазине'''
        return self.price * self.amount

    def apply_discount(self):
        '''применение установленной скидки для конкретного товара'''
        self.price *= self.pay_rate
        return self.price


item1 = Items("Смартфон", 10000, 20)
item2 = Items("Ноутбук", 20000, 5)

Items.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
