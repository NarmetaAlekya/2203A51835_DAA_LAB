
def input_products():
    products = {}
    n = int(input("Enter the number of products: "))
    for _ in range(n):
        name = input("Enter product name: ")
        price = int(input(f"Enter price for {name}: "))
        products[name] = price
    return products
def sort_by_price_desc(products):
    items = list(products.items()) 
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:  
                items[i], items[j] = items[j], items[i]  
    return items
def display_sorted_products(sorted_products):
    for product, price in sorted_products:
        print(f"{product}: ${price}")
products = input_products()
sorted_products = sort_by_price_desc(products)
display_sorted_products(sorted_products)
