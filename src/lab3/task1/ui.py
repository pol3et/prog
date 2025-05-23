from .db import Database
from .recsys import RecSys
import os

def main():
    """Main entry point for the application. Loads movies and user histories, initializes the recommendation system, and prints a recommendation for a new user based on input."""
    db = Database()

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    with open(os.path.join(data_dir, "movies.txt"), "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "":
                continue
            movie_id, title = line.strip().split(",")
            try:
                movie_id = int(movie_id)
                db.create_movie(title, movie_id)
            except ValueError:
                db.create_movie(title)

    with open(os.path.join(data_dir, "user_history.txt"), "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "":
                continue
            movie_ids = list(map(int, line.strip().split(",")))
            db.create_user(movie_ids)

    recsys = RecSys(db)

    user_movies = input("Enter new user's movies: ")
    user_movies = list(map(int, user_movies.split(",")))
    
    user = db.create_user(user_movies)

    recommendation = recsys.get_recommendation(user)
    if recommendation:
        print(recommendation.get_title())
    else:
        print("No recommendations available")

if __name__ == "__main__":
    main()