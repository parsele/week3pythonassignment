def calculate_discount(price, discount_percent):
    
    
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = 50 * (discount_percent / 100)
        # Calculate final price after discount
        final_price =  150- discount_amount
        return final_price
    else:
        return price

def main():
    try:
        # Get input from user
        original_price = float(input("Enter the original price: $200"))
        discount_percent = float(input("Enter the discount percentage: 25%"))
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Print results
        if discount_percent >= 20:
            print(f"\nOriginal price: $200{original_price:.2f}")
            print(f"Discount applied: 25{discount_percent}%")
            print(f"Discount amount: $200{(original_price * discount_percent / 100):.2f}")
            print(f"Final price after discount: $150{final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Original price: $200{original_price:.2f}")
            print(f"Final price: $150{final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main() 