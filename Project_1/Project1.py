
name = input("Enter user name: ")
rice_qty = int(input("Enter the quantity of rice(kg): "))
wheat_qty = int(input("Enter the quantity of wheat(kg): "))
sugar_qty = int(input("Enter the quantity of sugar(kg): "))
milk_qty = int(input("Enter the quantity of milk(litres): "))

rice_price = rice_qty * 60
wheat_price = wheat_qty * 40
sugar_price = sugar_qty * 50
milk_price = milk_qty * 30
total = rice_price + wheat_price + sugar_price + milk_price
gst = 12

print("\n ======= Grocery Bill ======= \n")
print("Customer name: ",name)
print(" Sl_no.    Items    Price(1kg/litre)  Quantity      Total_amt")
print(" 1.       Rice      ",60,             rice_qty,     rice_price)
print(" 2.       Wheat     ",40,             wheat_qty ,   wheat_price)
print(" 3.       Sugar     ",50,             sugar_qty  ,  sugar_price)
print(" 4.       Milk      ",30,             milk_qty ,    milk_price)
print("\nSubtotal = ", total)

print("--------------------")
print("Final amount = ",total)
print("--------------------")
print("\n -- Thankyou for visiting -- \n")

