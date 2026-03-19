# Order and Customer Management System

## Description

This project is a Python application that manages customers and orders using a separate structure in three main files:

- `main.py`
- `view.py`
- `controller.py`

Each file has a specific responsibility within the system.

---

# ▶️ `main.py` — Program control

## 🔹 What's inside?

In this file we mainly find:

### 1. Main loop (`while`)

```python
while True:
```

- Keeps the program running continuously
- Only stops when the user chooses to exit

---

### 2. Menu call

```python
option = show_menu()
```

- Call a function from `view.py`
- Shows available options
- Saves the option chosen by the user

---

### 3. Conditional structure (`if/elif`)

```python
if option == "1": 
# create client
elif option == "2": 
# create order
```

- Control what action to execute
- Depending on the option: 
- Calls `controller` functions 
- Use `view` to request or display data

---

### 4. Connection between layers

Typical example:

```python
data = request_customer_data()
create_customer(data)
```

👉 Here's what happens:
- `view` → get data
- `controller` → processes that data

---

## 🧠 Summary of `main.py`

- Control the flow of the program
- Manage the menu
- Decide which function to execute
- Connect `view` and `controller`

---

# 🖥️ `view.py` — Input and output

## 🔹 What's inside?

This file contains functions related to console interaction.

---

### 1. Menu function

```python
def show_menu(): 
print("1. Create client") 
print("2. Create order") 
return input("Select an option: ")
```

👉 Show options and return selection

---

### 2. Functions to request data

```python
def request_customer_data(): 
name = input("Name: ") 
phone = input("Phone: ") 
return {"name": name, "phone": phone}
```

👉 Returns data in structure (dictionary)

---

### 3. Functions to display results

```python
def display_message(msg): 
print(msg)
```

or

```python
def show_order(order): 
print(request)
```

---

## 🧠 Summary of `view.py`

- Use `input()` → to receive data
- Use `print()` → to display data
- Does not contain complex logic
- Only communicates with the user

---

# ⚙️ `controller.py` — System logic

## 🔹 What's inside?

Here is the actual logic of the program.

---

### 1. Data structures

```python
clients = []
orders = []
```

👉 Lists are used to store information

---

### 2. Function to create client

```python
def create_client(data): 
clients.append(data)
```

👉 Save the client to the list

---

### 3. Function to create order

```python
def create_order(data): 
orders.append(data)
```

👉 Save orders

---

### 4. Query functions

```python
def list_customers(): 
return clients
```

👉 Return data to `main`

---

### 5. Data processing

May include:

- Validations
- Searches
- Customer ↔ order relationship

---

## 🧠 Summary of `controller.py`

- Contains the system logic
- Manage data
- Execute actions
- Does not interact directly with the user

---

# 🔄 Complete system flow

```text
User → view (input) 
→ main (decides) 
→ controller (process) 
→ main 
→ view (print) 
→ User
```

---


👉 This is a basic implementation of the MVC pattern in Python.
