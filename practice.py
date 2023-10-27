import random

menu_items = [
    ["Rice", 30],
    ["Tea", 10],
    ["Pizza", 50],
    ["Burger", 40],
    # Add more items as needed
]

orders = []

def generate_order_id():
    return ''.join(str(random.randint(0, 9)) for _ in range(5))

while True:
    print("\nMain Menu:")
    print("1. Create New Order")
    print("2. View Orders")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        order_id = generate_order_id()
        order_items = []

        print("\nMenu:")
        for i, item in enumerate(menu_items, start=1):
            print(f"{i}. {item[0]} - ${item[1]}")

        item_number = input("Enter item number to add (0 to finish): ")
        
        while not item_number.isdigit() or not (1 <= int(item_number) <= len(menu_items)):
            print("Invalid item number. Please try again.")
            item_number = input("Enter item number to add (0 to finish): ")
        
        item_number = int(item_number)

        while True:
            if item_number == 0:
                break

            quantity = input(f"Enter quantity for {menu_items[item_number - 1][0]}: ")

            while not quantity.isdigit():
                print("Invalid quantity. Please try again.")
                quantity = input(f"Enter quantity for {menu_items[item_number - 1][0]}: ")

            quantity = int(quantity)

            order_items.append({"itemnumber": item_number, "quantity": quantity})
            item_number = input("Enter item number to add (0 to finish): ")

            while not item_number.isdigit() or not (0 <= int(item_number) <= len(menu_items)):
                print("Invalid item number. Please try again.")
                item_number = input("Enter item number to add (0 to finish): ")

            item_number = int(item_number)

        order = {"Orderid": order_id, "items": order_items}
        orders.append(order)
        print(f"Order {order_id} created successfully!")

    elif choice == "2":
        for order in orders:
            order_id = order["Orderid"]
            items = order["items"]
            total_price = sum(menu_items[item["itemnumber"] - 1][1] * item["quantity"] for item in items)

            print(f"\nOrder ID: {order_id}")
            print("Items:")
            for item in items:
                item_name = menu_items[item["itemnumber"] - 1][0]
                quantity = item["quantity"]
                print(f"{item_name} x{quantity}")
            print(f"Total Price: ${total_price}")

    elif choice == "3":
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please try again.")
