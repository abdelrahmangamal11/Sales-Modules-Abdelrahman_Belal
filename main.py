from customer import Customer
from product import Product
from sales import SaleOrder

customers = []
products = []
sale_orders = []
invoices = []

def menu():
    print("\n--- Main System Menu ---")
    print("1. Create Customer")
    print("2. Create Product")
    print("3. Create Sale Order")
    print("4. Confirm Sale Order")
    print("5. Cancel Sale Order")
    print("6. Create Invoice from Sale Order")
    print("7. Confirm Invoice")
    print("8. Cancel Invoice")
    print("9. Show All Customers")
    print("10. Show All Products")
    print("11. Show All Sale Orders")
    print("12. Show All Invoices")
    print("0. Exit")
    return input("Select an option: ")

# CREATE FUNCTIONS

def create_customer():
    name = input("Customer name: ")
    email = input("Customer email: ")
    phone = input("Customer phone: ")
    c = Customer(name, email, phone)
    customers.append(c)
    print(f"Created: {c}")


def create_product():
    name = input("Product name: ")
    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("Enter a valid number for price.")
    desc = input("Description: ")
    p = Product(name, price, desc)
    products.append(p)
    print(f"Created: {p}")


def create_sale_order():
    if not customers:
        print("No customers available. Create a customer first.")
        return

    if not products:
        print("No products available. Create a product first.")
        return

    print("Select Customer by ID:")
    for c in customers:
        print(f"{c.id}. {c.name}")

    try:
        cid = int(input("Customer ID: "))
    except ValueError:
        print("Invalid input.")
        return

    customer = next((c for c in customers if c.id == cid), None)
    if not customer:
        print("Invalid Customer ID")
        return

    so = SaleOrder(customer)
    sale_orders.append(so)

    print("Adding lines to Sale Order (enter 0 to stop)")
    while True:
        print("Available products:")
        for p in products:
            print(f"{p.id}. {p.name} - {p.price}")

        try:
            pid = int(input("Product ID (0 to finish): "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if pid == 0:
            break

        product = next((p for p in products if p.id == pid), None)
        if not product:
            print("Invalid product ID")
            continue

        try:
            qty = int(input("Quantity: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        so.add_line(product.name, qty, product.price)

    print(f"Created Sale Order: {so}")

# SALE ORDER WORKFLOW

def confirm_sale_order():
    if not sale_orders:
        print("No sale orders available.")
        return

    print("Sale Orders:")
    for i, so in enumerate(sale_orders, start=1):
        print(f"{i}. {so}")

    try:
        idx = int(input("Select Sale Order to confirm/post: "))
    except ValueError:
        print("Invalid input.")
        return

    if idx < 1 or idx > len(sale_orders):
        print("Invalid selection.")
        return

    so = sale_orders[idx-1]
    so.confirm()
    print(f"Sale Order posted: {so}")

def cancel_sale_order():
    if not sale_orders:
        print("No sale orders available.")
        return

    print("Sale Orders:")
    for i, so in enumerate(sale_orders, start=1):
        print(f"{i}. {so}")

    try:
        idx = int(input("Select Sale Order to cancel: "))
    except ValueError:
        print("Invalid input.")
        return

    if idx < 1 or idx > len(sale_orders):
        print("Invalid selection.")
        return

    so = sale_orders[idx-1]
    so.cancel()
    print(f"Sale Order canceled: {so}")

# INVOICE WORKFLOW

def create_invoice():
    if not sale_orders:
        print("No sale orders available.")
        return

    print("Sale Orders:")
    for i, so in enumerate(sale_orders, start=1):
        print(f"{i}. {so}")

    try:
        idx = int(input("Select Sale Order to confirm and create invoice: "))
    except ValueError:
        print("Invalid input.")
        return

    if idx < 1 or idx > len(sale_orders):
        print("Invalid selection.")
        return

    so = sale_orders[idx-1]
    invoice = so.confirm()  # logic returns invoice
    invoices.append(invoice)

    print(f"Invoice created: {invoice}")

def confirm_invoice():
    if not invoices:
        print("No invoices available.")
        return

    print("Invoices:")
    for i, inv in enumerate(invoices, start=1):
        print(f"{i}. {inv}")

    try:
        idx = int(input("Select Invoice to confirm/post: "))
    except ValueError:
        print("Invalid input.")
        return

    if idx < 1 or idx > len(invoices):
        print("Invalid selection.")
        return

    inv = invoices[idx-1]
    inv.confirm()
    print(f"Invoice posted: {inv}")

def cancel_invoice():
    if not invoices:
        print("No invoices available.")
        return

    print("Invoices:")
    for i, inv in enumerate(invoices, start=1):
        print(f"{i}. {inv}")

    try:
        idx = int(input("Select Invoice to cancel: "))
    except ValueError:
        print("Invalid input.")
        return

    if idx < 1 or idx > len(invoices):
        print("Invalid selection.")
        return

    inv = invoices[idx-1]
    inv.cancel()
    print(f"Invoice canceled: {inv}")

# SHOW LISTS

def show_all(list_items):
    if not list_items:
        print("Nothing to show.")
    else:
        for item in list_items:
            print(item)

# MAIN LOOP

def main():
    while True:
        choice = menu()

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_product()
        elif choice == "3":
            create_sale_order()
        elif choice == "4":
            confirm_sale_order()
        elif choice == "5":
            cancel_sale_order()
        elif choice == "6":
            create_invoice()
        elif choice == "7":
            confirm_invoice()
        elif choice == "8":
            cancel_invoice()
        elif choice == "9":
            show_all(customers)
        elif choice == "10":
            show_all(products)
        elif choice == "11":
            show_all(sale_orders)
        elif choice == "12":
            show_all(invoices)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
