# Grocery bill calculator using basics of python
name = input("Enter user name: ")
rice_qty = int(input("Enter the quantity of rice(kg): "))
wheat_qty = int(input("Enter the quantity of wheat(kg): "))
sugar_qty = int(input("Enter the quantity of sugar(kg): "))
milk_qty = int(input("Enter the quantity of milk(litres): "))

rice_price = rice_qty * 60
wheat_price = wheat_qty * 40
sugar_price = sugar_qty * 50
milk_price = milk_qty * 30
sub_total = rice_price + wheat_price + sugar_price + milk_price
gst = 0.05 * sub_total

print("\n======= Grocery Bill =======\n")
print("Customer name:", name)
print("-" * 65)
print(f"{'Sl No':<8}{'Item':<10}{'Price':<12}{'Quantity':<12}{'Total':<10}")
print("-" * 65)

print(f"{1:<8}{'Rice':<10}{60:<12}{rice_qty:<12}{rice_price:<10}")
print(f"{2:<8}{'Wheat':<10}{40:<12}{wheat_qty:<12}{wheat_price:<10}")
print(f"{3:<8}{'Sugar':<10}{50:<12}{sugar_qty:<12}{sugar_price:<10}")
print(f"{4:<8}{'Milk':<10}{30:<12}{milk_qty:<12}{milk_price:<10}")

print("-" * 65)
print("Subtotal =", sub_total)
print("GST =", gst)
print("-" * 65)

total = sub_total + gst

print("Final Amount =", total)
print("-" * 65)
print("Thank you for visiting!")