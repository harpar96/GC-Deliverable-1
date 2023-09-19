# Constants for fruit prices
FRUIT_PRICES = {
    "Apple": 2,
    "Grape": 1,
    "Orange": 3
}

# Tax rate
TAX_RATE = 0.05

# Initialize variables
total_items = {fruit: 0 for fruit in FRUIT_PRICES}
total_cost = 0

# Get user's name
name = input("Enter your name: ")

# Display fruit options and get user's choices
while True:
    print(f"\nHello, {name}! Here are the fruit options and prices:")
    print("Fruit\t\tPrice")
    for fruit, price in FRUIT_PRICES.items():
        print(f"{fruit}\t\t${price}")

    choice = input("Enter the fruit you want to buy (or 'done' to finish): ").capitalize()

    if choice == "Done":
        break

    if choice in FRUIT_PRICES:
        quantity = int(input(f"How many {choice}s would you like to buy? "))
        total_items[choice] += quantity
        total_cost += FRUIT_PRICES[choice] * quantity
        print(f"You bought {quantity} {choice}(s).")
    else:
        print("Invalid choice. Please try again.")

    # Display fruits bought so far
    print(f"\nFruits you have bought so far, {name}:")
    for fruit, quantity in total_items.items():
        if quantity > 0:
            print(f"{fruit}: {quantity}")

    # Ask if user wants to buy more
    more_fruit = input("Do you want to buy more fruit, {name}? (yes/no): ").lower()
    if more_fruit == "no":
        break

# Calculate subtotal, tax, and total
subtotal = sum(FRUIT_PRICES[fruit] * total_items[fruit] for fruit in FRUIT_PRICES)
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display receipt
print(f"\nReceipt for {name}:")
for fruit, quantity in total_items.items():
    if quantity > 0:
        print(f"{fruit}: {quantity} @ ${FRUIT_PRICES[fruit]} each")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
