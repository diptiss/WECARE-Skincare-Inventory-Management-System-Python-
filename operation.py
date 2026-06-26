from read import care_list # Importing the product list from the read module
from write import invoice_sell, invoice_buy # Functions to generate invoices

"""
This module handles the real-world scenario in the system like selling products to customers
and restocking them from suppliers. It updates quantities, manages free item offers,
and prints the final cart as invoice.
"""

def sell_products():
    """Handles the selling process: user input, stock update, and invoice creation."""
    try:
        customer_name = input("Customer's full name: ")  # Ask for customer's name
        customer_email = input("Email Address: ") # Ask for email
        shopping_cart = [] # To hold items being sold in this transaction

        while True:
            product_id = int(input("Enter product ID: ")) # Ask for product ID
            quantity = int(input("Enter quantity: ")) # Ask for quantity
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue

            for product in care_list:
                if product['ID'] == product_id:
                    free_items = quantity // 3 # For every 3, 1 is free
                    total_given = quantity + free_items

                    if product['Quantity'] >= total_given:
                        product['Quantity'] -= total_given
                        # Add to cart with brand and free items
                        shopping_cart.append({
                            "Product": product['Product Name'],
                            "Brand": product['Brand'],
                            "Quantity": quantity,
                            "Price": product['Price'] * 2, # Selling price
                            "Free": free_items
                        })
                        print("We've added " + str(quantity) + " " + product['Product Name'] + " to your order. You'll receive " + str(free_items) + " free of charge. Thank you!")
                    else:
                        print("We don’t have enough stock. Only " + str(product['Quantity']) + " left.")
                    break
            else:
                print("Invalid Product ID") # If ID didn't match any product

            add_more = input("Do you want to add more products? (y/n): ")
            if add_more.lower() != 'y':
                break

        if shopping_cart:
            invoice_sell(customer_name, customer_email, shopping_cart) # Generate invoice
        else:
            print("No items purchased.")

    except ValueError:
        print("No product found with that ID. Please try again.") # Error for invalid input type

        
def restock_products():
    """Manages restocking which adds quantity to existing products and generates invoice."""
    try:
        supplier_name = input("Enter supplier name: ") # Ask for supplier's name
        supplier_email = input("Enter supplier email: ") # Ask for supplier's email
        shopping_cart = [] # Holds items restocked

        while True:
            product_id = int(input("Enter product ID to restock: ")) # Ask for product ID
            restock_quantity = int(input("Enter quantity to restock: "))  # Ask for quantity
            if restock_quantity <= 0:
                print("Quantity must be a positive number.") # Prevent negatives or 0
                continue
                

            for product in care_list:
                if product['ID'] == product_id:
                    product['Quantity'] += restock_quantity
                    print("Restocked " + product['Product Name'] + ". New quantity: " + str(product['Quantity']))

                    # Add to the purchase cart
                    shopping_cart.append({
                        "Product": product['Product Name'],
                        "Brand": product['Brand'],
                        "Quantity": restock_quantity,
                        "Price": product['Price']
                    })
                    break
            else:
                print("Invalid Product ID")

            more = input("Restock more products? (y/n): ") # Ask if supplier wants to continue
            if more.lower() != 'y':
                break

        if shopping_cart:
            invoice_buy(supplier_name, supplier_email, shopping_cart) # Generate purchase invoice

    except ValueError:
        print("Invalid input. Please enter numbers only.") # Error for non-numeric entries
