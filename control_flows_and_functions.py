def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        return price - discount_amount
    else:
        return price
try:
 original_price = float (input("enter the original price:"))
 discount = float (input("enter the discount percentage:"))
 final_price = calculate_discount (original_price, discount)

 print (f"the final price after discount is {final_price:.2f}")
except ValueError:
 print ("Error Encountered")
