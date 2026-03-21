from controller import customer_controller, product_controller, order_controller, report_controller
from view import menu_view


def run():
    """
    Main function that runs the order management system.
    Initializes all in-memory databases and handles the main menu loop.
    Returns:
        None
    """
    # Initialize in-memory databases as empty dictionaries
    customers_db = {}
    products_db = {}
    orders_db = {}
    order_counter = 1  # Auto-increments to generate unique order IDs

    running = True

    while running:
        # View shows menu and returns the selected option
        option = menu_view.show_menu()

        # ------------------------------------------
        # OPTION 1 — Register customer
        # ------------------------------------------
        if option == "1":
            menu_view.clean_screen()
            # View collects input
            customer_id, name, email = menu_view.get_customer_input()

            # Controller validates and saves
            success, message, customers_db = customer_controller.register_customer(
                customers_db, customer_id, name, email
            )

            # View shows result
            menu_view.show_customer_result(success, message)

        # ------------------------------------------
        # OPTION 2 — Register product
        # ------------------------------------------
        elif option == "2":
            menu_view.clean_screen()
            # View collects input
            product_id, product_name, unit_price = menu_view.get_product_input()

            # If input was invalid (None), skip
            if product_id is None:
                pass
            else:
                # Controller validates and saves
                success, message, products_db = product_controller.register_product(
                    products_db, product_id, product_name, unit_price
                )

                # View shows result
                menu_view.show_product_result(success, message)

        # ------------------------------------------
        # OPTION 3 — Create order
        # ------------------------------------------
        elif option == "3":
            menu_view.clean_screen()
            # View collects input
            order_id, customer_id, product_id, quantity = menu_view.get_order_input()

            # If input was invalid (None), skip
            if order_id is None:
                pass
            else:
                # Generate order ID automatically
                generated_order_id = f"ORD-{order_counter}"

                # Controller validates and saves
                success, message, orders_db = order_controller.create_order(
                    orders_db, customers_db, products_db,
                    generated_order_id, customer_id, product_id, quantity
                )

                # View shows result
                menu_view.show_order_result(success, message)

                # Only increment counter if order was created successfully
                if success:
                    order_counter += 1

        # ------------------------------------------
        # OPTION 4 — Show orders
        # ------------------------------------------
        elif option == "4":
            menu_view.clean_screen()
            # View asks how to search
            search_option = menu_view.show_search_order_menu()

            if search_option == "1":
                # Show all orders
                success, message, all_orders = order_controller.get_all_orders(
                    orders_db, customers_db
                )

                if success:
                    menu_view.display_all_orders(all_orders, customers_db)
                else:
                    menu_view.show_order_error(message)

            elif search_option == "2":
                # Search by ID
                order_id = menu_view.get_order_id_input()

                success, message, order = order_controller.get_single_order(
                    orders_db, customers_db, order_id
                )

                if success:
                    customer_name = customers_db[order["customer_id"]]["name"]
                    menu_view.display_single_order(order_id, order, customer_name)
                else:
                    menu_view.show_order_error(message)

        # ------------------------------------------
        # OPTION 5 — Show daily income
        # ------------------------------------------
        elif option == "5":
            menu_view.clean_screen()
            # Controller calculates total income
            total_income = report_controller.calculate_daily_income(orders_db)

            # View displays it
            menu_view.display_income(total_income)

        # ------------------------------------------
        # OPTION 6 — Generate report
        # ------------------------------------------
        elif option == "6":
            menu_view.clean_screen()
            # Controller builds the report
            report, message = report_controller.generate_report(
                orders_db, customers_db
            )

            # View shows report or error
            if report:
                menu_view.show_report(report)
            else:
                menu_view.show_report_error(message)

        # ------------------------------------------
        # OPTION 0 — Exit
        # ------------------------------------------
        elif option == "0":
            print("\nGoodbye! System closed.")
            running = False

        else:
            print("✗ Invalid option. Please try again.")


# Entry point
if __name__ == "__main__":
    run()
