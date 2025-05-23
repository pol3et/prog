import unittest
from src.lab3.task1.db import Database
from src.lab3.task1.recsys import RecSys

class TestUI(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.movie1 = self.db.create_movie("Мстители: Финал", 1)
        self.movie2 = self.db.create_movie("Хатико", 2)
        self.movie3 = self.db.create_movie("Дюна", 3)
        self.movie4 = self.db.create_movie("Унесенные призраками", 4)
        
        self.db.create_user([2, 1, 3])
        self.db.create_user([1, 4, 3])
        self.db.create_user([2, 2, 2, 2, 2, 3])
        
        self.recsys = RecSys(self.db)

    def test_ui_recommendation(self):
        user = self.db.create_user([2, 4])
        recommendation = self.recsys.get_recommendation(user)
        self.assertEqual(recommendation.get_title(), "Дюна")


if __name__ == '__main__':
    unittest.main() 