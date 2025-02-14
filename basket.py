class Basket:
    def __init__(self):
        self.products = []

    def add(self, product, price, quantity):
        self.products.append({"product": product, "price": price, "quantity": quantity})
        return f"{product} ({quantity} savatga qo'shildi"

    def show(self): 
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']}: {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def calc(self):
        summa = 0
        for i in self.products:
            summa += i["price"] * i["quantity"]
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






# class Avto:
#     def __init__(self,name,year,km = 10):
#         self.name = name
#         self.year = year
#         self.__km = km

#         def get_km(self):
#             return self.__km
        

# a = Avto("Camaro",2024,10)
# a.__km = 0
# a.year = 2024
# a.familiya = "sagatov"
# print(a.familiya)