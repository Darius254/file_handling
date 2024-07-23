import csv  # Import the csv module to handle CSV file operations
import os  # Import the os module to handle file system operations

CSV_FILE = 'products.csv'  # Define the name of the CSV file to store product data

# Function to initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):  # Check if the CSV file does not exist
        with open(CSV_FILE, 'w', newline='') as file:  # Open the file in write mode
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerow(['Name', 'Price', 'Quantity'])  # Write the header row

# Function to read products from the CSV file
def read_products():
    products = []  # Initialize an empty list to store products
    try:
        with open(CSV_FILE, 'r', newline='') as file:  # Open the file in read mode
            reader = csv.DictReader(file)  # Create a CSV reader object
            for row in reader:  # Iterate over each row in the CSV file
                products.append(row)  # Append each product to the list
    except FileNotFoundError:
        print("Error: File not found.")  # Handle file not found error
    except csv.Error:
        print("Error: Incorrect data format.")  # Handle CSV format error
    return products  # Return the list of products

# Function to write products to the CSV file
def write_products(products):
    try:
        with open(CSV_FILE, 'w', newline='') as file:  # Open the file in write mode
            writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Quantity'])  # Create a CSV writer object
            writer.writeheader()  # Write the header row
            writer.writerows(products)  # Write all products to the file
    except csv.Error:
        print("Error: Could not write to file.")  # Handle CSV write error

# Function to add a product
def add_product(name, price, quantity):
    products = read_products()  # Read the existing products
    products.append({'Name': name, 'Price': price, 'Quantity': quantity})  # Add the new product
    write_products(products)  # Write the updated list back to the file

# Function to view all products
def view_products():
    products = read_products()  # Read the existing products
    if not products:  # Check if the product list is empty
        print("No products found.")  # Print a message if no products are found
    else:
        for product in products:  # Iterate over each product
            print(f"Name: {product['Name']}, Price: {product['Price']}, Quantity: {product['Quantity']}")  # Print product details

# Function to update a product
def update_product(name, new_price, new_quantity):
    products = read_products()  # Read the existing products
    updated = False  # Initialize a flag to check if the product was found
    for product in products:  # Iterate over each product
        if product['Name'] == name:  # Check if the product name matches
            product['Price'] = new_price  # Update the product price
            product['Quantity'] = new_quantity  # Update the product quantity
            updated = True  # Set the flag to True
            break  # Exit the loop once the product is found
    if updated:  # Check if the product was updated
        write_products(products)  # Write the updated list back to the file
        print(f"Product '{name}' updated successfully.")  # Print a success message
    else:
        print(f"Product '{name}' not found.")  # Print a message if the product was not found

# Function to delete a product
def delete_product(name):
    products = read_products()  # Read the existing products
    products = [product for product in products if product['Name'] != name]  # Filter out the product to be deleted
    write_products(products)  # Write the updated list back to the file
    print(f"Product '{name}' deleted successfully.")  # Print a success message

# Main function to handle user interaction
def main():
    initialize_csv()  # Initialize the CSV file

    while True:
        print("\nProduct Management System")  # Print the menu title
        print("1. Add Product")  # Print the option to add a product
        print("2. View Products")  # Print the option to view products
        print("3. Update Product")  # Print the option to update a product
        print("4. Delete Product")  # Print the option to delete a product
        print("5. Exit")  # Print the option to exit

        choice = input("Enter your choice: ")  # Get the user's choice
        if choice == '1':  # If the user chooses to add a product
            name = input("Enter product name: ")  # Get the product name
            price = input("Enter product price: ")  # Get the product price
            quantity = input("Enter product quantity: ")  # Get the product quantity
            add_product(name, price, quantity)  # Add the product
        elif choice == '2':  # If the user chooses to view products
            view_products()  # View the products
        elif choice == '3':  # If the user chooses to update a product
            name = input("Enter product name to update: ")  # Get the product name to update
            new_price = input("Enter new price: ")  # Get the new price
            new_quantity = input("Enter new quantity: ")  # Get the new quantity
            update_product(name, new_price, new_quantity)  # Update the product
        elif choice == '4':  # If the user chooses to delete a product
            name = input("Enter product name to delete: ")  # Get the product name to delete
            delete_product(name)  # Delete the product
        elif choice == '5':  # If the user chooses to exit
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Print a message for invalid input

if __name__ == "__main__":
    main()  # Call the main function to start the program
