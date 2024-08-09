def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
prices = []
n = int(input("Enter the number of prices: "))
print("Enter the prices:")
for _ in range(n):
    price = float(input())
    prices.append(price)
sorted_prices = bubble_sort(prices)
print("Prices Sorted:", sorted_prices)
