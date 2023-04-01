#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## food ordering app (final project)


# In[2]:


class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = id(self) # Generate unique ID for each item
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for item in self.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                break

    def view_food_items(self):
        for item in self.food_items:
            print(f"Food ID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")

    def remove_food_item(self, food_id):
        for item in self.food_items:
            if item.food_id == food_id:
                self.food_items.remove(item)
                break

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def view_menu(self, food_items):
        for item in food_items:
            print(f"Food ID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")

admin = Admin("admin", "password")
user = User("user", "password")

# Example usage:
admin.add_food_item("Pizza", "Large", 15.99, 0.2, 10)
admin.add_food_item("Burger", "Regular", 5.99, 0, 5)
admin.view_food_items()
admin.edit_food_item(1, "Pizza", "Medium", 12.99, 0.1, 5)
admin.view_food_items()
admin.remove_food_item(2)
admin.view_food_items()

user.view_menu(admin.food_items)


# In[1]:


class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def register(self):
        # Get user input for registration
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter a password: ")
        print("Registration successful!")

    def login(self):
        # Get user input for login
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self.email and password == self.password:
            print("Login successful!")
        else:
            print("Login failed. Please try again.")

    def place_order(self):
        # Display food menu and get user input for selected items
        food_menu = {
            1: {"name": "Tandoori Chicken (4 pieces)", "price": 240},
            2: {"name": "Vegan Burger (1 Piece)", "price": 320},
            3: {"name": "Truffle Cake (500gm)", "price": 900}
        }
        print("Select food items by entering an array of numbers.")
        print("For example, [2, 3] to order Vegan Burger and Truffle Cake.")
        selected_items = input("Enter your selection: ")
        selected_items = list(map(int, selected_items.strip("[]").split(",")))
        # Display selected items and get user input for order confirmation
        print("You have selected the following items:")
        total_price = 0
        for item in selected_items:
            print(f"{food_menu[item]['name']} [INR {food_menu[item]['price']}]")
            total_price += food_menu[item]['price']
        confirm_order = input(f"Total price is INR {total_price}. Confirm order? (y/n): ")
        if confirm_order.lower() == "y":
            self.order_history.append(selected_items)
            print("Order placed successfully!")
        else:
            print("Order cancelled.")

    def order_history(self):
        if not self.order_history:
            print("No order history.")
        else:
            for i, order in enumerate(self.order_history, start=1):
                print(f"Order {i}: {order}")

    def update_profile(self):
        # Get user input for profile update
        print("Current profile:")
        print(f"Full name: {self.full_name}")
        print(f"Phone number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        update_field = input("Enter the field you want to update: ")
        new_value = input("Enter the new value: ")
        if update_field == "full name":
            self.full_name = new_value
        elif update_field == "phone number":
            self.phone_number = new_value
        elif update_field == "email":
            self.email = new_value
        elif update_field == "address":
            self.address = new_value
        else:
            print("Invalid field. Please try again.")
            return
        print("Profile updated successfully!")


# In[ ]:





# In[ ]:




