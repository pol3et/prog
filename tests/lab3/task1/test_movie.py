import unittest
from src.lab3.task1.movie import Movie

class TestMovie(unittest.TestCase):
    def test_movie_creation(self):
        movie = Movie(1, "Test Movie")
        self.assertEqual(movie.get_identifier(), 1)
        self.assertEqual(movie.get_title(), "Test Movie")

    def test_movie_equality(self):
        movie1 = Movie(1, "Test Movie")
        movie2 = Movie(1, "Different Title")
        movie3 = Movie(2, "Test Movie")
        self.assertEqual(movie1, movie2)
        self.assertNotEqual(movie1, movie3)

    def test_movie_hash(self):
        movie1 = Movie(1, "Test Movie")
        movie2 = Movie(1, "Different Title")
        self.assertEqual(hash(movie1), hash(movie2))

    def test_movie_edge_cases(self):
        movie = Movie(0, "")
        self.assertEqual(movie.get_identifier(), 0)
        self.assertEqual(movie.get_title(), "")
        
        with self.assertRaises(ValueError):
            Movie(-1, "Negative ID")
        
        movie = Movie(999999, "Large ID")
        self.assertEqual(movie.get_identifier(), 999999)


if __name__ == '__main__':
    unittest.main() 