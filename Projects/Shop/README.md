# 🛒 SuperShop Management System (CLI)

A simple command-line based shopping application implemented in Python using Object-Oriented Programming principles. It supports seller and customer roles, product management, cart operations, and basic order handling.

---

## 📦 Features

### 👤 Authentication
- Create and login as **Seller** or **Customer**
- Email uniqueness check for account creation
- Password confirmation during signup

### 🧑‍💼 Seller Features
- Add new products to the shop
- Update quantity of existing products
- Remove products
- View personal product list

### 🧑‍🤝‍🧑 Customer Features
- View available products in shop
- Add items to cart
- Remove items from cart
- View cart with total price
- Confirm and make payment (clear cart)

---

## 🗂️ File Structure

```bash
Shop/
├── _1_Person.py       # Abstract base class for users
├── _2_Seller.py       # Seller class with product management
├── _3_Shop.py         # Shop class to manage available items
├── _4_Item.py         # Item class representing a product
├── _5_Customer.py     # Customer class with cart and order logic
├── _6_Order.py        # Order class to manage cart and total price
├── main.py            # Main application runner and logic
└── README.md



## ▶️ How to Run
#### 🧰 Prerequisites
    Python 3.x

## 🚀 Run the application
    python main.py

## 📋 Usage Instructions
###🔐 On Start
    - Choose whether you already have an account
    - Select role: Seller or Customer
    - Log in or create a new account

## 🧑 Seller Panel
    1. Add Product
    2. Remove Product
    3. See Products
    4. Exit
