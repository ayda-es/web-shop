class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price

def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]

def total(prices):
    return sum(prices) # wip 1
# wip 2
# A
# A

def apply_discount(price, percent):
    percent = max(min(percent, 100), 0)
    return price * (100 - percent) / 100

def add_tax(price, rate=0.15):
    return price * (1 + rate)

def apply_coupon(price):
    return max(price - 5, 0)

def search_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]

def format_price(price):
    return f"{price:,} Toman"

def list_names(products):
    return [p.name for p in products]

def count_products(products):
    return len(products)

def sort_by_price(products):
    return sorted(products, key=lambda p: p.price)

def in_stock(stock, sku):
    return stock.get(sku, 0) > 0
