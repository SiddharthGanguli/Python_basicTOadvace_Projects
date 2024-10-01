# Menu dictionary
menu = {
    "Pasta": 150,
    "Pizza": 200,
    "Burger": 250,
    "Coffee": 50,
    "Salad": 70
}

# Initial welcome message
print("----:Welcome to Our Restaurant:----")
print("Our Menu Card : -----")

# Display the menu
for key, value in menu.items():
    print(f"{key} = ₹ {value}")

# Initialize total bill
bill = 0

# First order
item1 = input("Sir! Please order something from our Restaurant: ")
item1=item1.capitalize()

if item1 in menu:
    print(f"Your order is {item1} and the price is ₹ {menu[item1]} ")
    bill += menu[item1]
    print(f"Your {item1} is successfully added to your order.")
else:
    print(f"Sorry sir, {item1.capitalize()} is not available in our restaurant.")

# Asking for more orders
while True:
    another_order = input("Sir, would you like to add anything else to your order? (yes/no): ").lower()
    
    if another_order in ["yes", "y"]:
        # Take another order
        item2 = input("Sir! Please order something from our Restaurant: ")
        item2=item2.capitalize()
        if item2.capitalize() in menu:
            print(f"Your order is {item2} and the price is ₹ {menu[item2]}")
            bill += menu[item2]
            print(f"Your {item2} is successfully added to your order.")
        else:
            print(f"Sorry sir, {item2.capitalize()} is not available in our restaurant.")
    elif another_order in ["no", "n"]:
    
        # Exit the loop and print the total bill
        print(f"Thank you for your order! Your total bill is ₹ {bill} ")
        break
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.")