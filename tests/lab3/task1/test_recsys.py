import unittest
from src.lab3.task1.db import Database
from src.lab3.task1.recsys import RecSys

class TestRecSys(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.movie1 = self.db.create_movie("Movie 1")
        self.movie2 = self.db.create_movie("Movie 2")
        self.movie3 = self.db.create_movie("Movie 3")
        self.recsys = RecSys(self.db)

    def test_empty_recommendations(self):
        user = self.db.create_user([])
        recommendations = self.recsys.generate_recommendations(user)
        self.assertEqual(recommendations, [])

    def test_recommendations_with_similar_users(self):
        user1 = self.db.create_user([self.movie1.get_identifier(), self.movie2.get_identifier()])
        user2 = self.db.create_user([self.movie1.get_identifier(), self.movie2.get_identifier(), self.movie3.get_identifier()])
        recommendations = self.recsys.generate_recommendations(user1)
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations[0][0], self.movie3)

    def test_no_recommendations_for_dissimilar_users(self):
        user1 = self.db.create_user([self.movie1.get_identifier()])
        user2 = self.db.create_user([self.movie2.get_identifier(), self.movie3.get_identifier()])
        recommendations = self.recsys.generate_recommendations(user1)
        self.assertEqual(recommendations, [])

    def test_recsys_edge_cases(self):
        user = self.db.create_user([self.movie1.get_identifier()])
        recommendation = self.recsys.get_recommendation(user)
        self.assertEqual(recommendation, None)
        
        user1 = self.db.create_user([self.movie1.get_identifier()])
        user2 = self.db.create_user([self.movie1.get_identifier(), self.movie2.get_identifier()])
        user3 = self.db.create_user([self.movie1.get_identifier(), self.movie3.get_identifier()])
        recommendations = self.recsys.generate_recommendations(user1)
        self.assertEqual(len(recommendations), 2)
        
        user = self.db.create_user([self.movie1.get_identifier(), self.movie2.get_identifier()])
        user2 = self.db.create_user([self.movie1.get_identifier(), self.movie2.get_identifier(), self.movie3.get_identifier()])
        recommendations = self.recsys.generate_recommendations(user)
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations[0][0], self.movie3)


if __name__ == '__main__':
    unittest.main() 