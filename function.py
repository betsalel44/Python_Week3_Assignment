def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = discount_percent / 100
        final_price = price - (price * discount_amount)
        return final_price
    else:
        return price


try:    
    price = float(input("Please enter the original price of the product: "))
    discount_percent = float(input("Please enter the discount: "))
    final_price = calculate_discount(price, discount_percent)
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
    