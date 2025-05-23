from typing import List, Tuple
from collections import defaultdict
from .user import User
from .movie import Movie
from .db import Database

class RecSys:
    """Recommendation system for suggesting movies to users based on their viewing history and similarity to other users."""
    def __init__(self, db: Database):
        """Initialize the recommendation system with a database instance.

        Args:
            db (Database): The database containing users and movies.
        """
        self.db = db

    def generate_recommendations(self, user: User) -> List[Tuple[Movie, float]]:
        """Generate a list of recommended movies for a user, ranked by similarity and weight.
        
        Iterates over all other users, computes similarity based on common movies, and aggregates scores for movies not yet seen by the user.
        Only users with at least 50% overlap are considered.
        Recommendations are sorted by score and movie identifier.

        Args:
            user (User): The user to generate recommendations for.

        Returns:
            List[Tuple[Movie, float]]: List of (Movie, weight) tuples sorted by weight and movie identifier.
        """
        user_movies = set(user.get_movies())
        if not user_movies:
            return []

        recommendations = defaultdict(float)
        user_movie_count = len(user_movies)

        for other_user in self.db.get_users():
            if user.get_identifier() == other_user.get_identifier():
                continue

            other_user_movies = set(other_user.get_movies())
            if not other_user_movies:
                continue

            common_movies = user_movies & other_user_movies
            if not common_movies:
                continue

            similarity = len(common_movies) / user_movie_count
            if similarity < 0.5:
                continue

            new_movies = other_user_movies - user_movies
            if not new_movies:
                continue

            for movie in new_movies:
                recommendations[movie] += similarity

        return sorted(recommendations.items(), key=lambda x: (-x[1], x[0].get_identifier()))

    def get_recommendation(self, user: User) -> Movie:
        """Return the best movie recommendation for a user, or None if no recommendation is available.
        
        Selects the top-weighted recommended movies, and if there are ties, chooses the most popular one among them.
        Returns None if no recommendations are available.

        Args:
            user (User): The user to recommend a movie to.

        Returns:
            Movie or None: The recommended movie, or None if no recommendation is available.
        """
        recommendations = self.generate_recommendations(user)
        
        if not recommendations:
            return None
            
        rec_pool = []
        max_weight = recommendations[0][1]
        
        for movie, weight in recommendations:
            if weight == max_weight:
                rec_pool.append(movie)
            else:
                break
                
        if len(rec_pool) == 1:
            return rec_pool[0]
            
        popularity = self.db.get_popularity()
        return max(rec_pool, key=lambda x: popularity.get(x, 0))
