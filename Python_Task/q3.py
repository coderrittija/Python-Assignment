quantity = int(input("Enter the quantity of items: "))
price_item = float(input("Enter the price per item: "))
total_expenses = quantity * price_item
if total_expenses > 5000:
    total_expenses *= 0.9
print(f"Total expenses: Rs. {total_expenses}")