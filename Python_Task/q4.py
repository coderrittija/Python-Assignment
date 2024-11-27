cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"The seller made a profit of {profit:.2f}.")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"The seller incurred a loss of {loss:.2f}.")
else:
    print("There is no profit or loss. The selling price is equal to the cost price.")