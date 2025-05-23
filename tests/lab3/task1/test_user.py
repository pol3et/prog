import unittest
from src.lab3.task1.user import User
from src.lab3.task1.movie import Movie

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(1)
        self.assertEqual(user.get_identifier(), 1)
        self.assertEqual(user.get_movies(), [])

    def test_add_movies(self):
        user = User(1)
        movies = [Movie(1, "Movie 1"), Movie(2, "Movie 2")]
        user.add_movies(movies)
        self.assertEqual(len(user.get_movies()), 2)
        self.assertEqual(user.get_movies(), movies)

    def test_user_edge_cases(self):
        user = User(0)
        self.assertEqual(user.get_identifier(), 0)
        
        with self.assertRaises(ValueError):
            User(-1)
        
        user = User(1)
        user.add_movies([])
        self.assertEqual(user.get_movies(), [])
        
        user = User(1)
        movie = Movie(1, "Movie")
        user.add_movies([movie])
        user.add_movies([movie])
        self.assertEqual(len(user.get_movies()), 2)


if __name__ == '__main__':
    unittest.main() 