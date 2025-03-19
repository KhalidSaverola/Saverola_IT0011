class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ₱{self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self):
        try:
            item_id = input("Enter item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return
            
            name = input("Enter item name: ").strip()
            description = input("Enter item description: ").strip()
            price = float(input("Enter item price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self):
        item_id = input("Enter the ID of the item to update: ").strip()
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        
        try:
            name = input("Enter new item name: ").strip()
            description = input("Enter new item description: ").strip()
            price = float(input("Enter new item price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_item(self):
        item_id = input("Enter the ID of the item to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item not found.")
    
    def menu(self):
        while True:
            print("\nItem Management Menu:")
            print("[C] - Create Item")
            print("[R] - Read Items")
            print("[U] - Update Item")
            print("[D] - Delete Item")
            print("[Q] - Quit")
            
            choice = input("Enter your choice: ").strip().upper()
            if choice == 'Q':
                print("Exiting program. Goodbye! Made by Khalid Saverola")
                break
            elif choice == 'C':
                self.create_item()
            elif choice == 'R':
                self.read_items()
            elif choice == 'U':
                self.update_item()
            elif choice == 'D':
                self.delete_item()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()
