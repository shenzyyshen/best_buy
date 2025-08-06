from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n--- Welcome to Best Buy ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Available Products:")
            for idx, product in enumerate(store.get_all_products(), start=1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            shopping_list = []
            products = store.get_all_products()

            print("\nWhich products would you like to order? (type 0 to finish)")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")

            while True:
                selection = input("Enter product number): 1-3 ")
                if selection == "0":
                    break
                try:
                    index = int(selection) - 1
                    if index < 0 or index >= len(products):
                        print("Invalid product number.")
                        continue
                    quantity = int(input("Enter quantity: "))
                    shopping_list.append((products[index], quantity))
                except ValueError:
                    print("Please enter valid numbers.")

            try:
                total_cost = store.order(shopping_list)
                print(f"\nOrder placed successfully. Total cost: {total_cost} dollars.")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
