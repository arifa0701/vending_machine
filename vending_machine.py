#Vending Machine
print("Welcome to X's vending machine \n")
print("Product price and code:")
print("Lays 2 AED 111")
print("Salad 1.50 AED 222")
print("Coke 5 AED 333")
print("KitKat 2 AED 444")
print("Coffee 5 AED 555")
print("Tea 2 AED 666")

# Step 2: Creating variables for product prices and stock levels
products = {
    111: {"name": "Lays", "price": 2, "stock": 5},
    222: {"name": "Salad", "price": 1.5, "stock": 3},
    333: {"name": "Coke", "price": 5, "stock": 2},
    444: {"name": "KitKat", "price": 2, "stock": 0},
    555: {"name": "Coffee", "price": 5, "stock": 1},
    666: {"name": "Tea", "price": 2, "stock": 3}
}

# Step 3: Loop until a valid product is selected
while True:
    print("\nType a product code to continue...")
    
    try:
        userCode = int(input())
    except ValueError:
        print("Invalid input. Please enter a numeric product code.")
        continue  # Loop back to ask again

    # Step 4 and Step 5: Check the user's selection
    if userCode in products:
        product = products[userCode]
        if product["stock"] <= 0:
            print(f"Sorry, {product['name']} is out of stock. Please select another product.")
        else:
            print(f"You have selected {product['name']}. Pay {product['price']:.2f} AED.")
            break  # Valid selection; exit the loop
    else:
        print("Invalid code. Please try again.")

# Step 6: Accept payment
amount_inserted = 0.0
while amount_inserted < product["price"]:
    try:
        insert = float(input(f"Insert money (Remaining: {product['price'] - amount_inserted:.2f} AED): "))
        if insert <= 0:
            print("Please insert a positive amount.")
            continue
        amount_inserted += insert

        if amount_inserted >= product["price"]:
            print("Sufficient balance.")
        else:
            print("Insufficient balance. Please insert more money.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Step 7: Calculate and return change if needed
change = amount_inserted - product["price"]
print(f"Dispensing {product['name']}...")
product["stock"] -= 1  # Deduct the item from stock
if change > 0:
    print(f"Returning change: {change:.2f} AED")
print("Thank you for your purchase!")

