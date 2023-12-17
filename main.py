import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the 'products' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

def add_product(name, quantity, price):
    cursor.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    conn.commit()
    print(f"{name} added to the inventory.")

def display_inventory():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    
    if not products:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product(name, quantity, price)
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
