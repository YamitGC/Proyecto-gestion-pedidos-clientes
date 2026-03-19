# controller/report_controller.py

from models import order_model


def calculate_daily_income(orders_db):
    """
    Sums all order totals to get daily income.
    Params:
        orders_db (dict): all registered orders
    Returns:
        float: total income of the day
    """
    total_income = 0

    for order_id, order in orders_db.items():
        total_income += order_model.get_order_total(order)

    return total_income


def group_orders_by_customer(orders_db, customers_db):
    """
    Groups all orders under their customer's name.
    Params:
        orders_db (dict): all registered orders
        customers_db (dict): all registered customers
    Returns:
        dict: orders grouped by customer name
    """
    grouped = {}

    for order_id, order in orders_db.items():
        customer_id = order["customer_id"]
        customer_name = customers_db[customer_id]["name"]

        # Create group for customer if it does not exist yet
        if customer_name not in grouped:
            grouped[customer_name] = {}

        # Add order inside that customer's group
        grouped[customer_name][order_id] = order

    return grouped


def generate_report(orders_db, customers_db):
    """
    Builds the full daily report.
    Params:
        orders_db (dict): all registered orders
        customers_db (dict): all registered customers
    Returns:
        tuple: (dict or None, str)
               dict -> complete report, None if no orders
               str  -> result message
    """
    if not orders_db:
        return None, "No orders registered to generate report"

    total_income = calculate_daily_income(orders_db)
    grouped = group_orders_by_customer(orders_db, customers_db)

    report = {
        "total_orders": len(orders_db),
        "total_income": total_income,
        "orders_by_customer": grouped
    }

    return report, "Report generated successfully"
