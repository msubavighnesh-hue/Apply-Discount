def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    return price * (1 - discount / 100)


# Input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate
final_price = apply_discount(price, discount)

# Output
print("\n--- Price Details ---")
print("Original Price:", price)
print("Discount:", discount, "%")
print("Final Price:", final_price)