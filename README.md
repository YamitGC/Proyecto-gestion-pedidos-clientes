# Customer Order Management System

A console-based Python application for managing customers, products, and orders. Built following the **MVC (Model-View-Controller)** architectural pattern with in-memory storage.

---

## Features

- Register and manage customers
- Register and manage products
- Create orders with automatic ID generation and total calculation
- Query all orders or search by ID
- Calculate total daily income
- Generate a full daily report grouped by customer

---

## Project Structure

```
Proyecto-gestion-pedidos-clientes/
│
├── main.py                         # Entry point — main loop and flow control
│
├── models/
│   ├── customer_model.py           # Customer data operations
│   ├── order_model.py              # Order data operations
│   └── product_model.py            # Product data operations
│
├── controller/
│   ├── customer_controller.py      # Customer business logic & validation
│   ├── order_controller.py         # Order business logic & validation
│   ├── product_controller.py       # Product business logic & validation
│   └── report_controller.py        # Income calculation & report generation
│
└── view/
    └── menu_view.py                # All console input/output functions
```

---

## Architecture

This project implements the MVC pattern across three layers:

```
User → View (input)
     → Main (routing)
     → Controller (validation & logic)
     → Model (data storage)
     → Controller
     → Main
     → View (output)
     → User
```

| Layer | Responsibility |
|---|---|
| **Model** | Stores and retrieves data using in-memory dictionaries |
| **View** | Handles all `input()` and `print()` interactions with the user |
| **Controller** | Validates data, applies business rules, and coordinates between model and view |
| **Main** | Runs the menu loop and routes each option to the correct controller/view calls |

> **Note:** There is no database or file persistence. All data lives in memory for the duration of the session.

---

## Getting Started

### Requirements

- Python 3.10 or higher
- No external dependencies required

### Run the application

```bash
python main.py
```

---

## Menu Options

```
====== MENU ======
1. Register customer
2. Register product
3. Create order
4. Show orders
5. Show daily income
6. Generate report
0. Exit
```

### Option 1 — Register Customer
Prompts for a customer ID, full name, and email. Validates that all fields are provided and that the ID is not already taken.

### Option 2 — Register Product
Prompts for a product ID, name, and unit price. Validates that the price is a positive number and that the ID is not already taken.

### Option 3 — Create Order
Prompts for a customer ID, product ID, and quantity. The order ID is generated automatically (`ORD-1`, `ORD-2`, ...). The total is calculated as `unit_price × quantity`. Validates that the customer and product both exist.

### Option 4 — Show Orders
Offers two sub-options:
1. Display all registered orders
2. Search for a specific order by its ID

### Option 5 — Show Daily Income
Sums the totals of all registered orders and displays the result.

### Option 6 — Generate Report
Produces a complete summary including total number of orders, total income, and all orders grouped by customer.

---

## Data Models

### Customer
```python
customers_db[customer_id] = {
    "name": str,
    "email": str
}
```

### Product
```python
products_db[product_id] = (product_id, product_name, unit_price)  # tuple
```

### Order
```python
orders_db[order_id] = {
    "customer_id": str,
    "product": (product_id, product_name, unit_price),
    "quantity": int,
    "total": float
}
```

---

## Example Session

```
====== MENU ======
1. Register customer
Select an option: 1

--- Register Customer ---
Enter customer ID: C001
Enter customer name: Alice Smith
Enter customer email: alice@example.com
✓ Customer 'Alice Smith' registered successfully

Select an option: 2

--- Register Product ---
Enter product ID: P001
Enter product name: Laptop
Enter unit price: 999.99
✓ Product 'Laptop' registered successfully

Select an option: 3

--- Create Order ---
Enter customer ID: C001
Enter product ID: P001
Enter quantity: 2
✓ Order 'ORD-1' created. Total: $1999.98

Select an option: 5

--- DAILY INCOME ---
Total generated: $1999.98
```

---

## Limitations

- Data is **not persisted** between sessions — all records are lost when the program exits.
- No multi-user support.
- No file or database backend.
