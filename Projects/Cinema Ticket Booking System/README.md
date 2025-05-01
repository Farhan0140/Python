# 🎟️ Cinema Ticket Booking System (CLI)

A command-line based movie ticket booking system built in Python using Object-Oriented Programming (OOP). It features admin and customer roles, seat selection, coupon discounts, and order history.


## 📸 Preview
![Image](https://github.com/user-attachments/assets/1e73db93-a098-4e03-95ca-cfbb68a7284a)


---

## 📦 Features

### 👤 Authentication
- Create and login as **Admin** or **Customer**
- Email uniqueness check for account creation
- Password confirmation during signup

### 🧑‍💼 Admin Features
- Add new movies with full details
- Update or remove existing movies
- Manage customers (view/remove)
- Add and remove discount coupons
- View all customer information

### 🧍 Customer Features
- View available movies and showtimes
- View 2D seat availability
- Book seats and add to cart
- Apply coupon codes for discounts
- View cart and pay using wallet
- View previous orders

---

## 🗂️ File Structure

```bash
Cinema Ticket Booking System/
├── main.py                  # Entry point for the application
├── _1_user.py               # Abstract base class for Admin/Customer
├── _2_admin.py              # Admin logic and features
├── _3_cinema.py             # Main Cinema class managing users and movies
├── _4_movie.py              # Movie class
├── _5_Sits.py               # Seat map logic
├── _6_customer.py           # Customer logic and cart system
├── _7_order.py              # Ticket class for storing booking info and Cart and past order management
└── README.md
```

---

## ▶️ How to Run
#### 🧰 Prerequisites
    Python 3.x

## 🚀 Run the application
    python main.py

## 📋 Usage Instructions
### 🔐 On Start
    - Choose whether you already have an account
    - Select role: Admin or Customer
    - Log in or create a new account

## 🧑 Admin Panel
    1. Update Info
    2. Add Movie
    3. Remove Movie
    4. Update Movie Info
    5. Show Movies
    6. Add Coupon
    7. Remove Coupon
    8. View Coupons
    9. Remove Customer
    10. View Customers Info
    11. Exit

## 🧍 Customer Panel
    1. Update Info
    2. View Movie List
    3. Book Ticket
    4. View Available Seats
    5. Check Balance
    6. Cash In
    7. View Cart
    8. Pay Bill
    9. View Previous Orders
    10. Exit

---

## 📚 OOP Concepts Used
    - Inheritance (Customer, Admin ← User)
    - Encapsulation (private wallet, password, seat structure)
    - Composition (Customer has Cart, Movie has Seats, etc.)
