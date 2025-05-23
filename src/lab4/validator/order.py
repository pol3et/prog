import re
from collections import Counter
from enum import Enum

class ErrorType(Enum):
    ADDRESS = 1
    PHONE = 2

class DeliveryPriority(Enum):
    MAX = 0
    MIDDLE = 1
    LOW = 2

class Order:
    """Represents a customer order, parses and validates order data, and provides formatted output and error reporting.

    Parses an order line, validates address and phone, and provides formatted representations and error details.
    """
    def __init__(self, order_line: str):
        """Initialize an Order from a semicolon-separated string.

        Args:
            order_line (str): The raw order line string.

        Raises:
            ValueError: If the order format is invalid.
        """
        parts = order_line.strip().split(';')
        if len(parts) != 6:
            raise ValueError(f"Invalid order format: {order_line}")
        
        self.order_number = parts[0]
        self.products = parts[1]
        self.customer_name = parts[2]
        self.delivery_address = parts[3]
        self.phone_number = parts[4]
        self.priority_str = parts[5]
        
        self.errors = self.validate()
    
    def validate(self):
        """Validate the delivery address and phone number.

        Returns:
            list[tuple[ErrorType, str]]: List of error type and value pairs.
        """
        errors = []
        
        if not self.delivery_address:
            errors.append((ErrorType.ADDRESS, "no data"))
        elif not self._is_valid_address(self.delivery_address):
            errors.append((ErrorType.ADDRESS, self.delivery_address))
        
        if not self.phone_number:
            errors.append((ErrorType.PHONE, "no data"))
        elif not self._is_valid_phone(self.phone_number):
            errors.append((ErrorType.PHONE, self.phone_number))
        
        return errors
    
    def _is_valid_address(self, address: str) -> bool:
        """Check if the address is valid (must have 4 non-empty parts separated by dots).

        Args:
            address (str): The address string.

        Returns:
            bool: True if valid, False otherwise.
        """
        parts = address.split('.')
        return len(parts) == 4 and all(part.strip() for part in parts)
    
    def _is_valid_phone(self, phone: str) -> bool:
        """Check if the phone number matches the required pattern.

        Args:
            phone (str): The phone number string.

        Returns:
            bool: True if valid, False otherwise.
        """
        pattern = r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$'
        return bool(re.match(pattern, phone))
    
    def is_valid(self) -> bool:
        """Return True if the order has no validation errors.

        Returns:
            bool: True if valid, False otherwise.
        """
        return len(self.errors) == 0
    
    def get_country(self) -> str:
        """Extract the country from the delivery address.

        Returns:
            str: The country name, or empty string if not available.
        """
        if not self.delivery_address:
            return ""
        parts = self.delivery_address.split('.')
        return parts[0].strip() if len(parts) > 0 else ""
    
    def get_formatted_products(self) -> str:
        """Return a formatted string of products with counts if repeated.

        Returns:
            str: The formatted product list.
        """
        product_list = [p.strip() for p in self.products.split(',')]
        counter = Counter(product_list)
        formatted_products = []
        
        for product, count in counter.items():
            if count > 1:
                formatted_products.append(f"{product} x{count}")
            else:
                formatted_products.append(product)
        
        return ", ".join(formatted_products)
    
    def get_formatted_address(self) -> str:
        """Return a formatted delivery address (without country).

        Returns:
            str: The formatted address string.
        """
        if not self.delivery_address:
            return ""
        
        parts = self.delivery_address.split('.')
        if len(parts) < 4:
            return self.delivery_address
        
        return f"{parts[1].strip()}. {parts[2].strip()}. {parts[3].strip()}"
    
    def to_output_string(self) -> str:
        """Return the order as a semicolon-separated output string.

        Returns:
            str: The formatted output string.
        """
        return f"{self.order_number};{self.get_formatted_products()};{self.customer_name};{self.get_formatted_address()};{self.phone_number};{self.priority_str}"
    
    def get_error_strings(self) -> list[str]:
        """Return a list of error strings for this order.

        Returns:
            list[str]: List of error strings for output.
        """
        return [f"{self.order_number};{error_type.value};{error_value}" for error_type, error_value in self.errors]
