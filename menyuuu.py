from uuid import uuid4

class Basket:
    def __init__(self):
        self.__id = uuid4()
        self.products = []

    def get_id(self):
        return self.__id

    def menu(self):
        return """
        1. Mahsulot qo'shish
        2. Savatni ko'rish
        3. Umumiy narxni hisoblash
        4. Mahsulotni olib tashlash
        5. Savatni tozalash
        6. Mahsulot miqdorini yangilash
        7. Chiqish
        """

    def add(self, product, price, quantity):
        self.products.append({"product": product, "price": price, "quantity": quantity})
        return f"{product} ({quantity} dona) savatga qo'shildi"

    def show(self):
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']}: {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def calc(self):
        summa = sum(i["price"] * i["quantity"] for i in self.products)
        return f"Umumiy narx: {summa} USD"

    def remove(self, product, quantity=1):
        for i in self.products:
            if i["product"] == product:
                if i["quantity"] > quantity:
                    i["quantity"] -= quantity
                else:
                    self.products.remove(i)
                return f"{product} ({quantity} dona) savatdan olib tashlandi"
        return f"{product} savatda topilmadi"

    def clear(self):
        self.products = []
        return "Savat tozalandi"

    def update_quantity(self, product, new_quantity):
        for i in self.products:
            if i["product"] == product:
                i["quantity"] = new_quantity
                return f"{product} miqdori {new_quantity} dona qilib yangilandi"
        return f"{product} savatda topilmadi"


basket = Basket()
print(basket.menu())
