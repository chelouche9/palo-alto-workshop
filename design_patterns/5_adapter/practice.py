# You have an e-commerce shop and you want to sell another brand's products
# Create an adapter to mitigate between your product and the external product (get_data())
class MyProduct:
    def __init__(self, price, color, name):
        self.price = price
        self.color = color
        self.name = name
    
    def get_data(self):
        return {
            'price': self.price,
            'color': self.color,
            'name': self.name
        }

class ExternalProduct:
    def __init__(self, value, shade, title):
        self.value = value
        self.shade = shade
        self.title = title
    
    def get_data(self):
        return {
            'value': self.value,
            'shade': self.shade,
            'title': self.title
        }

# Create the adapter class here


my_shirt = MyProduct(10, 'blue', 'Shirt')
print(my_shirt.get_data())

external_shirt = ExternalProduct(12, 'black', 'Pants')
print(external_shirt.get_data())