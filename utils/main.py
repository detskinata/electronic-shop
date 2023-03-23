import csv


class Items:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name) -> str:
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls) -> list | str:
        item = []
        with open('items.csv', encoding='windows-1251') as f:
            file_reader = csv.DictReader(f)
            for i in file_reader:
                name_csv = i['name']
                price_csv = int(i['price'])
                quantity_csv = int(i['quantity'])
                item = cls.all.append(cls(name_csv, price_csv, quantity_csv))
            return item

    @staticmethod
    def is_integer(num) -> bool:
        return int(num) == num

    def __repr__(self) -> str:
        return f"{self.name}, {self.price}, {self.amount}"

    def __str__(self) -> str:
        return f"{self.name}"

Items.instantiate_from_csv()  # создание объектов из данных файла
print(len(Items.all))  # в файле 5 записей с данными по товарам
#
# print(Items.is_integer(5))
# print(Items.is_integer(5.0))
# print(Items.is_integer(5.5))

item1 = Items("Смартфон", 10000, 20)
print(item1)