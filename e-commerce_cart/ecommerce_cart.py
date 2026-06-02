class Cart:

    def __init__(self, product_name=None, price=0, quantity=0):

        self.__product_name = product_name
        self.__price = price
        self.__quantity = quantity

    # Getters
    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_quantity(self, quantity):
        self.__quantity = quantity

    # Add Product
    def add_product(self):

        product_name = input("Enter Product Name: ")
        price = int(input("Enter Product Price: "))
        quantity = int(input("Enter Quantity: "))

        product = Cart(product_name, price, quantity)

        cart_data.append(product)

        print("Product Added Successfully")


    # Remove Product
    def remove_product(self):

        name = input("Enter Product Name to Remove: ")

        for product in cart_data:

            if product.get_product_name() == name:

                cart_data.remove(product)

                print("Product Removed Successfully")

                return

        print("Product Not Found")

    # Update Quantity
    def update_quantity(self):

        name = input("Enter Product Name: ")

        for product in cart_data:

            if product.get_product_name() == name:

                quantity = int(input("Enter New Quantity: "))

                product.set_quantity(quantity)

                print("Quantity Updated Successfully")

                return

        print("Product Not Found")

    # Generate Bill
    def generate_bill(self):

        total = 0

        print("\n===== BILL =====")

        for product in cart_data:

            amount = product.get_price() * product.get_quantity()

            print(product.get_product_name(),
                  product.get_quantity(),
                  "x",
                  product.get_price(),
                  "=",
                  amount)

            total = total + amount

        print("Total Bill =", total)

        return total

    # Apply Discount
    def apply_discount(self):

        total = self.generate_bill()

        discount = int(input("Enter Discount Percentage: "))

        final_amount = total - (total * discount / 100)

        print("Final Amount =", final_amount)

    # Save Order History
    def save_order_history(self):

        total = self.generate_bill()

        order_history.append(total)

        print("Order Saved Successfully")

    def search(self):
        key=input("enter the product for search:")
        for product in cart_data:
            if product.get_product_name()==key:
                print("product found")
                return product


# Main Program
if __name__ == "__main__":

    cart_data = []

    order_history = []

    obj = Cart()

    while True:

        print("\n===== E-COMMERCE CART =====")

        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Generate Bill")
        print("5. Apply Discount")
        print("6. Save Order History")
        print("7. search")
        print("8. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:

            obj.add_product()

        elif choice == 2:

            obj.remove_product()

        elif choice == 3:

            obj.update_quantity()

        elif choice == 4:

            obj.generate_bill()

        elif choice == 5:

            obj.apply_discount()

        elif choice == 6:

            obj.save_order_history()

        elif choice == 7:

            obj.search()
        elif choice == 8:
            print("Thank You")

            break

        else:

            print("Invalid Choice")