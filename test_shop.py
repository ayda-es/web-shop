from shop import Product, find_by_name

products = [
    Product("101", "Laptop", 25000000),
    Product("102", "Mouse", 500000)
]

result = find_by_name(products, "lap")

assert len(result) == 1
assert result[0].name == "Laptop"