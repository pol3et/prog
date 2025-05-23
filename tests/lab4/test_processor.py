import unittest
import os
import tempfile
from src.lab4.validator import OrderProcessor

class TestOrderProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.input_file = os.path.join(self.temp_dir.name, 'test_orders.txt')
        self.valid_output_file = os.path.join(self.temp_dir.name, 'test_valid_orders.txt')
        self.invalid_output_file = os.path.join(self.temp_dir.name, 'test_invalid_orders.txt')
    
    def tearDown(self):
        self.temp_dir.cleanup()
    
    def test_process_orders(self):
        test_data = [
            "87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX",
            "56342;Хлеб, Молоко, Хлеб, Молоко;Смирнова Мария Леонидовна;Германия. Бавария. Мюнхен. Мариенплац;+4-989-234-56;LOW",
            "90385;Макароны, Сыр, Макароны, Сыр;Николаев Николай;;+1-416-123-45-67;LOW"
        ]
        
        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(test_data))
        
        processor = OrderProcessor(self.input_file, self.valid_output_file, self.invalid_output_file)
        processor.process()
        
        self.assertTrue(os.path.exists(self.valid_output_file))
        self.assertTrue(os.path.exists(self.invalid_output_file))
        
        with open(self.valid_output_file, 'r', encoding='utf-8') as f:
            valid_content = f.read()
        
        self.assertIn("87459", valid_content)
        self.assertIn("Молоко x2, Яблоки x2, Хлеб", valid_content)
        
        with open(self.invalid_output_file, 'r', encoding='utf-8') as f:
            invalid_content = f.read()
        
        self.assertIn("56342;2;+4-989-234-56", invalid_content)
        self.assertIn("90385;1;no data", invalid_content)
    
    def test_country_sort_key(self):
        processor = OrderProcessor(self.input_file, self.valid_output_file, self.invalid_output_file)
        
        self.assertEqual(processor._country_sort_key("Россия")[0], 0)
        self.assertEqual(processor._country_sort_key("Российская Федерация")[0], 0)
        
        self.assertEqual(processor._country_sort_key("Франция")[0], 1)
        self.assertEqual(processor._country_sort_key("Германия")[0], 1)


if __name__ == "__main__":
    unittest.main() 