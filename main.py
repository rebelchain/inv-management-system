from datetime import datetime, date

class Product:
    """Base blueprint for a product in the inventory."""
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def price(self) -> float:
        """Getter: Output the price of the product."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Setter: Update the price of the product."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


    @property
    def stock(self) -> int:
        """Getter: Output the stock quantity of the product."""
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        """Setter: Update the stock quantity of the product."""
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    def __str__(self) -> str:
        """String representation of the product."""
        return f"Product {self.name:<15}, Rp{self.price:>10.2f}, Stock: {self.stock}"






class PerishableProduct(Product):
    """Subclass of Product for perishable items with an expiration date."""

    def __init__(self, name: str, price: float, stock: int, expiry_date_str: str):

        super().__init__(name, price, stock)

        self.expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()

    def is_expired(self) -> bool:
        """Check if the product is expired."""
        return date.today() > self.expiry_date


    def __str__(self) -> str:
        """Overriding Method: Overlays the parent's print format to add extensive information about the product."""

        base_string = super().__str__()

        status = "Expired" if self.is_expired() else "Valid"

        return f"{base_string} | Exp: {self.expiry_date}  [{status}]"
















if __name__ == "__main__":

    print("=== Test 1: Product Inventory create normal object ===")
    laptop = Product("Laptop", 15000000.0, 10)
    mouse = Product("Mouse", 150000.0, 50)

    print(laptop)
    print(mouse)

    print("\n=== Test 2: Buy product and reduce stock ===")

    laptop.stock -= 2  # Buying 2 laptops
    print(laptop)

    print("\n=== Test 3: Test Data Validation ===")

    try:
        error_product = Product("ErrorProduct", -100.0, 5)  # Invalid price
    except ValueError as e:
        print(f"Error: {e}")

    try:
        mouse.stock -= 100
    except ValueError as e:
        print(f"Error: {e}")