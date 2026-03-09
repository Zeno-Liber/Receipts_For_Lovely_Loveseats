# First item in our catalogue
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# First item's price in USD
lovely_loveseat_price = 254.00

# Second item in our catalogue
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Second item's price
stylish_settee_price = 180.50

# Third item in our catalogue
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Third item's price
luxurious_lamp_price = 52.15

# Variable for sales tax percentage
sales_tax = .088

# Data for our first customer: subtotal and item list
customer_one_total = 0
customer_one_itemization = ""

# First customer's purchases
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculating the customers final total
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Formatting for customer's receipt
print("Customer One Items: " + customer_one_itemization)
print("Customer One Total: " , customer_one_total)