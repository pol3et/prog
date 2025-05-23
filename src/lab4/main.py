import os
from .validator.processor import OrderProcessor


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'data', 'orders.txt')
    valid_output_file = os.path.join(script_dir, 'data', 'order_country.txt')
    invalid_output_file = os.path.join(script_dir, 'data', 'non_valid_orders.txt')
    
    processor = OrderProcessor(input_file, valid_output_file, invalid_output_file)
    processor.process()
    
    print(f"Processing complete!")
    print(f"Valid orders saved to: {valid_output_file}")
    print(f"Invalid orders saved to: {invalid_output_file}")

if __name__ == "__main__":
    main() 