#handling date time
import datetime

"""
This part of the program is used to load product data from a text file.
It reads each line, extracts the product details, and stores them as dictionaries
inside a list called 'care_list'. This data is then used throughout the system
to display products, manage operations, and generate invoices.
"""

# reads .txt file
file = open("products.txt", 'r')

# reads each line of .txt file in a list
f = file.readlines()

# to close file after reading
file.close()

# empty list to store product
care_list = []

# initializing product id
product_id = 1

for line in f:
    parts = line.split(', ') # Split line into individual product attributes

    # dictionary of product details
    product_dict = {
        "ID": product_id,
        "Product Name": parts[0],
        "Brand": parts[1],
        "Quantity": int(parts[2]),
        "Price": int(parts[3]),
        "Origin": parts[4]
    }

    care_list.append(product_dict) #Add the product to the main list
    product_id += 1 #increament of product id

# Print the product info
def show_products_table():
    print("================================================================================")
    print("ID  | Product Name      | Brand        | Qty | Price | Origin")
    print("================================================================================")

    # Loop through each product and format the data for display
    for p in care_list:
        selling_price = p['Price'] * 2 # Selling price is calculated as double the base price

        # Convert fields to string
        id = str(p['ID'])
        name = p['Product Name']
        brand = p['Brand']
        quantity = str(p['Quantity'])
        price = str(selling_price)
        origin = p['Origin']

        #manual padding
        line = id
        while len(line) < 5:
            line += " "

        line += name
        while len(line) < 25:
            line += " "

        line += brand
        while len(line) < 42:
            line += " "

        line += quantity
        while len(line) < 52:
            line += " "

        line += price
        while len(line) < 61:
            line += " "

        line += origin

        print(line)

    print("================================================================================")
