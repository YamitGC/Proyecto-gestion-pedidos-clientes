# ------------------------------------------
# VIEW: MAIN MENU
# ------------------------------------------

def show_menu():
    """
    Displays the main menu options to the user.
    Returns:
        str: option selected by the user
    """
    print("\n====== MENU ======")
    print("1. Register customer")
    print("2. Register product")
    print("3. Create order")
    print("4. Show orders")
    print("5. Show daily income")
    print("6. Generate report")
    print("0. Exit")
    return input("Select an option: ")


# ------------------------------------------
# VIEW: CUSTOMER
# ------------------------------------------

def get_customer_input():
    """
    Asks the user for customer data.
    Returns:
        tuple: (customer_id, name, email)
    """
    print("\n--- Register Customer ---")
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    return customer_id, name, email


def show_customer_result(success, message):
    """
    Displays the result of a customer registration.
    Params:
        success (bool): whether it was successful
        message (str): message to display
    Returns:
        str: the message shown
    """
    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ Error: {message}")
    return message


# ------------------------------------------
# VIEW: PRODUCT
# ------------------------------------------

def get_product_input():
    """
    Asks the user for product data.
    Returns:
        tuple: (product_id, product_name, unit_price)
               returns (None, None, None) if price is invalid
    """
    print("\n--- Register Product ---")
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")

    try:
        unit_price = float(input("Enter unit price: "))
    except ValueError:
        print("✗ Error: Price must be a number")
        return None, None, None

    return product_id, product_name, unit_price


def show_product_result(success, message):
    """
    Displays the result of a product registration.
    Params:
        success (bool): whether it was successful
        message (str): message to display
    Returns:
        str: the message shown
    """
    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ Error: {message}")
    return message


# ------------------------------------------
# VIEW: ORDER INPUT
# ------------------------------------------

def get_order_input():
    """
    Asks the user for order data.
    Returns:
        tuple: (order_id, customer_id, product_id, quantity)
               returns (None, None, None, None) if quantity is invalid
    """
    print("\n--- Create Order ---")
    order_id = input("Enter order ID: ")
    customer_id = input("Enter customer ID: ")
    product_id = input("Enter product ID: ")

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("✗ Error: Quantity must be a number")
        return None, None, None, None

    return order_id, customer_id, product_id, quantity


def show_order_result(success, message):
    """
    Displays the result of an order creation.
    Params:
        success (bool): whether it was successful
        message (str): message to display
    Returns:
        str: the message shown
    """
    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ Error: {message}")
    return message


# ------------------------------------------
# VIEW: CONSULT ORDERS
# ------------------------------------------

def show_search_order_menu():
    """
    Asks the user how they want to consult orders.
    Returns:
        str: option selected by user
    """
    print("\n--- Consult Orders ---")
    print("1. Show all orders")
    print("2. Search order by ID")
    return input("Select an option: ")


def get_order_id_input():
    """
    Asks the user for an order ID to search.
    Returns:
        str: the order ID entered
    """
    return input("Enter order ID to search: ")


def display_single_order(order_id, order, customer_name):
    """
    Displays one order in a formatted way.
    Params:
        order_id (str): the order ID
        order (dict): the order data
        customer_name (str): the customer's name
    Returns:
        str: the order_id displayed
    """
    product_name = order["product"][1]  # index 1 of the product tuple

    print(f"""
----------------------------------------
Order ID:  {order_id}
Customer:  {customer_name}
Product:   {product_name}
Quantity:  {order["quantity"]}
Total:     ${order["total"]}
----------------------------------------""")

    return order_id


def display_all_orders(orders_db, customers_db):
    """
    Displays all orders in a formatted way.
    Params:
        orders_db (dict): all orders
        customers_db (dict): all customers
    Returns:
        int: number of orders displayed
    """
    print("\n===== ALL ORDERS =====")

    for order_id, order in orders_db.items():
        customer_name = customers_db[order["customer_id"]]["name"]
        display_single_order(order_id, order, customer_name)

    return len(orders_db)


def show_order_error(message):
    """
    Displays an error message for order consultation.
    Params:
        message (str): error message
    Returns:
        str: the message shown
    """
    print(f"✗ {message}")
    return message


# ------------------------------------------
# VIEW: DAILY INCOME
# ------------------------------------------

def display_income(total_income):
    """
    Displays the total income generated during the day.
    Params:
        total_income (float): total income calculated by the controller
    Returns:
        float: the total income displayed
    """
    print("\n--- DAILY INCOME ---")
    print(f"Total generated: ${total_income}")
    return total_income


# ------------------------------------------
# VIEW: REPORT
# ------------------------------------------

def show_report(report):
    """
    Displays the full daily report.
    Params:
        report (dict): the complete report dictionary
    Returns:
        str: confirmation message
    """
    print("\n====== DAILY REPORT ======")
    print(f"Total orders:  {report['total_orders']}")
    print(f"Total income:  ${report['total_income']}")

    print("\n--- Orders by Customer ---")

    for customer_name, customer_orders in report["orders_by_customer"].items():
        print(f"\n👤 {customer_name}")

        for order_id, order in customer_orders.items():
            product_name = order["product"][1]
            print(f"""
  Order ID:  {order_id}
  Product:   {product_name}
  Quantity:  {order['quantity']}
  Total:     ${order['total']}""")

    return "Report displayed"


def show_report_error(message):
    """
    Displays an error message when report cannot be generated.
    Params:
        message (str): error message
    Returns:
        str: the message shown
    """
    print(f"✗ {message}")
    return message
