# Function to input products and prices
def input_products():
    products = {}
    n = int(input("Enter the number of products: "))
    for _ in range(n):
        name = input("Enter product name: ")
        price = int(input(f"Enter price for {name}: "))
        products[name] = price
    return products

# Function to sort the dictionary by prices in descending order
def sort_by_price_desc(products):
    items = list(products.items())  # Convert dictionary to list of tuples
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:  # Compare based on the second item in the tuple (price)
                items[i], items[j] = items[j], items[i]  # Swap if the current price is less than the next one
    return items

# Function to display sorted products
def display_sorted_products(sorted_products):
    for product, price in sorted_products:
        print(f"{product}: ${price}")

# Input products and prices
products = input_products()

# Sort the products by price in descending order
sorted_products = sort_by_price_desc(products)

# Display the sorted products
print("\nSorted products by price (descending):")
display_sorted_products(sorted_products)
