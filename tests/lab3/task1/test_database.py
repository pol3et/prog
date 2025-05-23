import unittest
from src.lab3.task1.db import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_create_movie(self):
        movie = self.db.create_movie("Test Movie")
        self.assertEqual(movie.get_title(), "Test Movie")
        self.assertEqual(movie.get_identifier(), 0)

    def test_create_user(self):
        movie = self.db.create_movie("Test Movie")
        user = self.db.create_user([movie.get_identifier()])
        self.assertEqual(user.get_identifier(), 0)
        self.assertEqual(len(user.get_movies()), 1)

    def test_get_user_movies(self):
        movie = self.db.create_movie("Test Movie")
        user = self.db.create_user([movie.get_identifier()])
        user_movies = self.db.get_user_movies(user.get_identifier())
        self.assertEqual(len(user_movies), 1)
        self.assertIn(movie, user_movies)

    def test_database_edge_cases(self):
        self.assertEqual(self.db.get_user(999), None)
        self.assertEqual(self.db.get_movie(999), None)
        self.assertEqual(self.db.get_user_movies(999), set())
        
        user = self.db.create_user([])
        self.assertEqual(len(user.get_movies()), 0)
        
        movie = self.db.create_movie("")
        self.assertEqual(movie.get_title(), "")
        
        self.assertEqual(len(self.db.get_users()), 1)
        self.assertEqual(len(self.db.get_movies()), 1)


if __name__ == '__main__':
    unittest.main() 