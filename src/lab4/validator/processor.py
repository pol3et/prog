from .order import Order, DeliveryPriority


class OrderProcessor:
    """Processes orders from an input file, validates and sorts them, and writes valid and invalid orders to output files.

    Reads orders, validates them, sorts valid orders by country and priority, and outputs results to files.
    """
    def __init__(self, input_file, valid_output_file, invalid_output_file):
        """Initialize the processor with file paths.

        Args:
            input_file (str): Path to the input file with raw orders.
            valid_output_file (str): Path to the output file for valid orders.
            invalid_output_file (str): Path to the output file for invalid orders.
        """
        self.input_file = input_file
        self.valid_output_file = valid_output_file
        self.invalid_output_file = invalid_output_file
        self.valid_orders = []
        self.invalid_orders = []
    
    def process(self):
        """Process all orders: read, validate, sort, and write outputs."""
        self._read_orders()
        self._sort_valid_orders()
        self._write_valid_orders()
        self._write_invalid_orders()
    
    def _read_orders(self):
        """Read orders from the input file and classify as valid or invalid."""
        with open(self.input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    try:
                        order = Order(line)
                        if order.is_valid():
                            self.valid_orders.append(order)
                        else:
                            self.invalid_orders.append(order)
                    except ValueError as e:
                        print(f"Skipping invalid order: {e}")
    
    def _sort_valid_orders(self):
        """Sort valid orders by country (Russia first) and delivery priority."""
        def sort_key(order):
            country_key = self._country_sort_key(order.get_country())
            try:
                priority_key = DeliveryPriority[order.priority_str].value
            except (KeyError, ValueError):
                priority_key = 3
            return (country_key, priority_key)
        
        self.valid_orders.sort(key=sort_key)
    
    def _country_sort_key(self, country):
        """Return a sorting key for the country, prioritizing Russia-related names.

        Args:
            country (str): The country name.

        Returns:
            tuple: Sorting key tuple (0 or 1, country name).
        """
        russia_names = ["россия", "россий", "russia", "russian"]
        
        country_lower = country.lower()
        for name in russia_names:
            if name in country_lower:
                return (0, country)
        
        return (1, country)
    
    def _write_valid_orders(self):
        """Write all valid orders to the valid output file."""
        with open(self.valid_output_file, 'w', encoding='utf-8') as file:
            for order in self.valid_orders:
                file.write(order.to_output_string() + '\n\n')
    
    def _write_invalid_orders(self):
        """Write all invalid orders and their errors to the invalid output file."""
        with open(self.invalid_output_file, 'w', encoding='utf-8') as file:
            all_errors = []
            
            for order in self.invalid_orders:
                for error_type, error_value in order.errors:
                    all_errors.append((order.order_number, error_type, error_value))
            
            all_errors.sort(key=lambda x: x[1].value, reverse=True)
            
            for order_number, error_type, error_value in all_errors:
                error_string = f"{order_number};{error_type.value};{error_value}"
                file.write(error_string + '\n\n') 