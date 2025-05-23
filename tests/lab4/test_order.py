import unittest
from src.lab4.validator import Order, ErrorType

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        order_line = "87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX"
        order = Order(order_line)
        
        self.assertTrue(order.is_valid())
        self.assertEqual(len(order.errors), 0)
        self.assertEqual(order.order_number, "87459")
        self.assertEqual(order.priority_str, "MAX")
    
    def test_invalid_phone(self):
        order_line = "56342;Хлеб, Молоко, Хлеб, Молоко;Смирнова Мария Леонидовна;Германия. Бавария. Мюнхен. Мариенплац;+4-989-234-56;LOW"
        order = Order(order_line)
        
        self.assertFalse(order.is_valid())
        self.assertEqual(len(order.errors), 1)
        self.assertEqual(order.errors[0][0], ErrorType.PHONE)
        self.assertEqual(order.errors[0][1], "+4-989-234-56")
    
    def test_invalid_address(self):
        order_line = "90385;Макароны, Сыр, Макароны, Сыр;Николаев Николай;;+1-416-123-45-67;LOW"
        order = Order(order_line)
        
        self.assertFalse(order.is_valid())
        self.assertEqual(len(order.errors), 1)
        self.assertEqual(order.errors[0][0], ErrorType.ADDRESS)
        self.assertEqual(order.errors[0][1], "no data")
    
    def test_multiple_errors(self):
        order_line = "84756;Печенье, Сыр, Печенье, Сыр;Васильева Анна Владимировна;Япония. Шибуя. Шибуя-кроссинг;+8-131-234-5678;MAX"
        order = Order(order_line)
        
        self.assertFalse(order.is_valid())
        self.assertEqual(len(order.errors), 2)
        
        error_types = [error[0] for error in order.errors]
        self.assertIn(ErrorType.ADDRESS, error_types)
        self.assertIn(ErrorType.PHONE, error_types)
    
    def test_formatted_products(self):
        order_line = "87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX"
        order = Order(order_line)
        
        self.assertEqual(order.get_formatted_products(), "Молоко x2, Яблоки x2, Хлеб")
    
    def test_formatted_address(self):
        order_line = "87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX"
        order = Order(order_line)
        
        self.assertEqual(order.get_formatted_address(), "Московская область. Москва. улица Пушкина")
    
    def test_get_country(self):
        order_line = "87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX"
        order = Order(order_line)
        
        self.assertEqual(order.get_country(), "Россия")


if __name__ == "__main__":
    unittest.main() 