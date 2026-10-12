"""
shopping_cart.py
Week 5 Practical Exercise: ShoppingCart Class
"""

class ShoppingCart:
    def __init__(self):
        # Initialize an independent collection for each cart instance
        self.items = []

    def add_item(self, product_name: str, price: float, quantity: int = 1) -> None:
        """Adds a product with its price and quantity to the cart."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Update quantity if product already exists, otherwise append
        for item in self.items:
            if item["name"].lower() == product_name.lower():
                item["quantity"] += quantity
                return

        self.items.append({
            "name": product_name,
            "price": price,
            "quantity": quantity
        })

    def remove_item(self, product_name: str) -> None:
        """Extension: Removes an item by name from the cart."""
        self.items = [
            item for item in self.items 
            if item["name"].lower() != product_name.lower()
        ]

    def calculate_total(self) -> float:
        """Calculates and returns the total cost of all items in the cart."""
        return sum(item["price"] * item["quantity"] for item in self.items)


if __name__ == "__main__":
    # Cart 1 instance
    cart_alice = ShoppingCart()
    cart_alice.add_item("Notebook", 4.50, quantity=3)
    cart_alice.add_item("Pen", 1.50, quantity=2)

    # Cart 2 instance (demonstrating independent state)
    cart_bob = ShoppingCart()
    cart_bob.add_item("Headphones", 49.99, quantity=1)
    cart_bob.add_item("USB Cable", 8.00, quantity=2)

    print(f"Alice's Cart Total: ${cart_alice.calculate_total():.2f}")
    print(f"Bob's Cart Total  : ${cart_bob.calculate_total():.2f}")