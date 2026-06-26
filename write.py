import datetime # Used to add date and time to invoices
from read import care_list # Brings in the product list for updating stock

"""
This module handles everything related to invoices and saving changes.
It prints invoices to the screen, writes them to text files, and updates the stock file
when a transaction (sale or restock) is completed.
"""

def invoice_sell(name, email, cart_items):
    """Generates a sale invoice, prints it, and saves it as a text file."""
    subtotal = 0 # Holds the total before VAT
    total_free_items = 0 # Tracks how many free items were given out

    print("") # Empty line for spacing
    print("======================================================================")
    print("                   WECARE SKINCARE                          ")
    print("----------------------------------------------------------------------")
    print(" Customer Name: " + name)
    print(" Customer Email: " + email)
    print("----------------------------------------------------------------------")
    print("Item\t\tBrand\t\tQty\tFree\tPrice\tTotal")
    print("----------------------------------------------------------------------")

    # Loop through each item in the cart to calculate totals
    for item in cart_items:
        line_total = item['Quantity'] * item['Price']
        subtotal += line_total
        total_free_items += item['Free']
         # Print each line of the invoice in the terminal
        print(item['Product'] + "\t" +item['Brand']+ "\t" +str(item['Quantity']) + "\t" + str(item['Free']) + "\t\t" + str(item['Price']) + "\t" + str(line_total))

    vat = int(subtotal * 0.13)  # Calculates 13% VAT
    grand_total = subtotal + vat # Final bill

    print("----------------------------------------------------------------------")
    print("Subtotal                               :     " + str(subtotal))
    print("13% VAT                                :      " + str(vat))
    print("Total Amount                           :     " + str(grand_total))
    print("Free Items Given                       :        " + str(total_free_items))
    print("======================================================================")
    print("             THANK YOU FOR USING WECARE! HOPE TO SEE YOU AGAIN                  ")
    print("======================================================================")

    # save to file
    now = datetime.datetime.now()
    uniqueValue = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    time_str = str(now.hour) + ":" + str(now.minute)

    file = open("invoice_sell.txt", "w")
    file.write("======================================================================\n")
    file.write("                    WECARE SKINCARE                            \n")
    file.write("----------------------------------------------------------------------\n")
    file.write(" Invoice Date: " + uniqueValue + "  Time: " + time_str + "\n")
    file.write(" Customer Name: " + name + "\n")
    file.write("----------------------------------------------------------------------\n")
    file.write("Product\t\tBrand\t\tQty\tFree\tUnit Price\tTotal\n")
    file.write("----------------------------------------------------------------------\n")

    for item in cart_items:
        line_total = item['Quantity'] * item['Price']
        file.write(item['Product'] + "\t" + item['Brand'] + "\t" + str(item['Quantity']) + "\t" + str(item['Free']) + "\t" + str(item['Price']) + "\t" + str(line_total) + "\n")

    file.write("----------------------------------------------------------------------\n")
    file.write("Subtotal                              :     " + str(subtotal) + "\n")
    file.write("13% VAT                               :      " + str(vat) + "\n")
    file.write("Total Amount                          :     " + str(grand_total) + "\n")
    file.write("Free Items Given                      :        " + str(total_free_items) + "\n")
    file.write("======================================================================\n")
    file.write("               THANK YOU FOR USING WECARE! HOPE TO SEE YOU AGAIN                    \n")
    file.write("======================================================================\n")



def invoice_buy(name, email, cart_items):
    """Generates a purchase invoice and saves it as a text file."""
    total_amount = 0

    print("")
    print("======================================================================\n")
    print("                         WECARE SKINCARE                             ")
    print("----------------------------------------------------------------------")
    print(" Supplier Name: " + name)
    print(" Supplier Email: " + email)
    print("----------------------------------------------------------------------")
    print("Product\t\tBrand\t\tQuantity\tUnit Price\tTotal")
    print("----------------------------------------------------------------------")

    # Process each product being restocked
    for item in cart_items:
        line_total = item['Quantity'] * item['Price']
        total_amount += line_total
        print(item['Product'] + "\t" + item['Brand'] + "\t" + str(item['Quantity']) + "\t\t\t" + str(item['Price']) + "\t" + str(line_total))

    print("-----------------------------------------------------------------------")
    print("Total Purchase Amount              :     " + str(total_amount))
    print("=======================================================================")
    print("               THANK YOU FOR RESTOCKING!                      ")
    print("=======================================================================")

    now = datetime.datetime.now()
    date_time = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute)

    file = open("invoice_buy.txt", "w") # Create the restock invoice file
    file.write("======================================================================\n")
    file.write("                   WECARE SKINCARE\n")
    file.write("----------------------------------------------------------------------\n")
    file.write(" Invoice Date & Time: " + date_time + "\n")
    file.write(" Supplier Name: " + name + "\n")
    file.write(" Supplier Email: " + email + "\n")
    file.write("----------------------------------------------------------------------\n")
    file.write("Product\t\tBrand\t\tQuantity\tUnit Price\tTotal\n")
    file.write("----------------------------------------------------------------------\n")

    for item in cart_items:
        line_total = item['Quantity'] * item['Price']
        file.write(item['Product'] + "\t" + item['Brand'] + "\t" + str(item['Quantity']) + "\t\t\t" + str(item['Price']) + "\t" + str(line_total)+"\n")

    file.write("----------------------------------------------------------------------\n")
    file.write("Total Purchase Amount              :     " + str(total_amount) + "\n")
    file.write("======================================================================\n")
    file.write("           THANK YOU FOR RESTOCKING!                      \n")
    file.write("======================================================================\n")

def update_stock():
    """Updates the products.txt file with the latest quantities."""
    file = open("products.txt", "w")  # Overwrite file with new stock levels
    for product in care_list:
        # Combine product details into one line
        line = product["Product Name"] + ", " + product["Brand"] + ", " + str(product["Quantity"]) + ", " + str(product["Price"]) + ", " + product["Origin"]
        file.write(line) # Save to file
