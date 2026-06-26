#importing function to display product table, selling and restocking, and save update
from read import show_products_table
from operation import sell_products, restock_products
from write import update_stock

"""
This is the main menu of the WECARE skincare system.
It presents a simple menu where the user can choose to view products,
sell products to customers, restock items from suppliers, or exit the program.
"""
def options():
    """Displays the main menu and performs actions based on user input."""
    while True:
        print("\n===== YOU ARE AT WECARE  =====") # welcome text
        print("How can we help you today?") 
        print("1. Display Products") #option to view products
        print("2. Sell Products") #option to sell to customers
        print("3. Restock Products") #option to add new stock
        print("4. Exit") #option to save and exit

        choice = input("Enter a number (1-4): ") #users choice

        if choice == "1":
            show_products_table() #show product details
        elif choice == "2":
            sell_products() # selling process
        elif choice == "3":
            restock_products() #restocking process
        elif choice == "4":
            update_stock() #save updated stock to file
            print("Thank you for choosing WECARE SKINCARE system.") #exit message
            break
        else:
            print("Please enter numbers only.(1-4)") #handle invalid inputs

options() #to run main menu loop
