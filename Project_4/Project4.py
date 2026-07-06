menu = (
    (1, "Butter Chicken", 280),
    (2, "Paneer Butter Masala", 220),
    (3, "Litti Chokha", 150),
    (4, "Samosa", 25),
    (5, "Chole Bhature", 120),
    (6, "Masala Dosa", 140),
    (7, "Biryani", 250),
    (8, "Gulab Jamun", 40)
)

cart = []
customer = {}
unique_items = set()


def show_menu():
    print("\n========== MENU ==========")
    print("ID\tItem\t\t\tPrice")
    for item in menu:
        print(item[0], "\t", item[1], "\t\t₹", item[2])


def place_order():
    global customer

    if customer == {}:
        customer["name"] = input("Enter Customer Name: ")

        while True:
            mobile = input("Enter Mobile Number: ")
            if mobile.isdigit() and len(mobile) == 10:
                customer["mobile"] = mobile
                break
            else:
                print("Invalid Mobile Number!")

    try:
        item_id = int(input("Enter Item ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    found = False

    for item in menu:
        if item[0] == item_id:
            found = True

            try:
                qty = int(input("Enter Quantity: "))
                if qty < 1:
                    print("Quantity must be greater than 0")
                    return
            except ValueError:
                print("Invalid Quantity!")
                return

            total = item[2] * qty

            cart.append({
                "item": item[1],
                "price": item[2],
                "qty": qty,
                "total": total
            })

            unique_items.add(item[1])

            print("Item Added Successfully!")
            break

    if not found:
        print("Invalid Item ID!")


def view_cart():
    if len(cart) == 0:
        print("Cart is Empty")
        return

    print("\n====== YOUR CART ======")

    for item in cart:
        print(item["item"], "x", item["qty"], "= ₹", item["total"])


def remove_item():
    if len(cart) == 0:
        print("Cart is Empty")
        return

    name = input("Enter Item Name to Remove: ")

    removed = False

    for item in cart:
        if item["item"].lower() == name.lower():
            cart.remove(item)
            removed = True
            print("Item Removed Successfully!")
            break

    unique_items.clear()

    for item in cart:
        unique_items.add(item["item"])

    if not removed:
        print("Item Not Found")


def generate_bill():
    if len(cart) == 0:
        print("Cart is Empty")
        return None

    subtotal = 0

    print("\n==========================")
    print("Restaurant Bill")
    print("==========================")
    print("Customer :", customer["name"])

    for item in cart:
        print(item["item"], "x" + str(item["qty"]), "₹", item["total"])
        subtotal += item["total"]

    gst = subtotal * 0.05
    final_bill = subtotal + gst

    print("--------------------------")
    print("Subtotal : ₹", subtotal)
    print("GST (5%) : ₹", round(gst, 2))
    print("Final Bill : ₹", round(final_bill, 2))
    print("Thank You!")
    print("Visit Again ❤️")

    return round(final_bill, 2)


def save_order():
    if len(cart) == 0:
        print("No Order to Save")
        return

    total = generate_bill()

    file = open("orders.txt", "a")

    file.write("Customer : " + customer["name"] + "\n")

    for item in cart:
        file.write(item["item"] + " x" + str(item["qty"]) + "\n")

    file.write("Total : " + str(total) + "\n")
    file.write("-------------------------\n")

    file.close()

    print("Order Saved Successfully!")


def view_previous_orders():
    try:
        file = open("orders.txt", "r")
        print("\n====== PREVIOUS ORDERS ======\n")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No Previous Orders Found!")


def main():
    while True:
        print("\n====== RESTAURANT ORDERING SYSTEM ======")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Generate Bill")
        print("6. Save Order")
        print("7. View Previous Orders")
        print("8. Exit")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                show_menu()

            elif choice == 2:
                place_order()

            elif choice == 3:
                view_cart()

            elif choice == 4:
                remove_item()

            elif choice == 5:
                generate_bill()

            elif choice == 6:
                save_order()

            elif choice == 7:
                view_previous_orders()

            elif choice == 8:
                print("Thank You! Visit Again ❤️")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only!")


main()
