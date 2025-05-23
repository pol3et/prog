from typing import List, Union, Dict
from collections import Counter
from .user import User
from .movie import Movie

class Database:
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._movies: Dict[int, Movie] = {}
        self._popularity: Counter[Movie] = Counter()
        self._user_movies: Dict[int, set[Movie]] = {}

    def create_user(self, movies: List[int]) -> User:
        """Create a new user with a list of movie identifiers and add the user to the database.

        Args:
            movies (List[int]): List of movie identifiers.

        Returns:
            User: The created user instance.
        """
        user = User(len(self._users))
        user.add_movies([self._movies[movie_id] for movie_id in movies if movie_id in self._movies])
        self.add_user(user)
        return user
    
    def create_movie(self, title: str, identifier: int | None = None) -> Movie:
        """Create a new movie with a title and optional identifier, and add it to the database.

        Args:
            title (str): The title of the movie.
            identifier (int, optional): The unique identifier for the movie. Defaults to None.

        Returns:
            Movie: The created movie instance.
        """
        if identifier is None:
            identifier = len(self._movies)
        movie = Movie(identifier, title)
        self.add_movie(movie)
        return movie

    def add_user(self, user: User) -> None:
        """Add a user to the database.

        Args:
            user (User): The user to add.

        Raises:
            ValueError: If a user with the same identifier already exists.
        """
        if user.get_identifier() in self._users:
            raise ValueError(f"User with ID {user.get_identifier()} already exists")
        self._users[user.get_identifier()] = user
        self._user_movies[user.get_identifier()] = set(user.get_movies())
        self.calculate_popularity()

    def add_movie(self, movie: Movie) -> None:
        """Add a movie to the database.

        Args:
            movie (Movie): The movie to add.

        Raises:
            ValueError: If a movie with the same identifier already exists.
        """
        if movie.get_identifier() in self._movies:
            raise ValueError(f"Movie with ID {movie.get_identifier()} already exists")
        self._movies[movie.get_identifier()] = movie

    def get_user(self, identifier: int) -> Union[User, None]:
        """Retrieve a user by their identifier.

        Args:
            identifier (int): The user's identifier.

        Returns:
            User or None: The user if found, otherwise None.
        """
        return self._users.get(identifier)

    def get_movie(self, identifier: int) -> Union[Movie, None]:
        """Retrieve a movie by its identifier.

        Args:
            identifier (int): The movie's identifier.

        Returns:
            Movie or None: The movie if found, otherwise None.
        """
        return self._movies.get(identifier)

    def get_users(self) -> List[User]:
        """Return a list of all users in the database.

        Returns:
            List[User]: List of users.
        """
        return list(self._users.values())

    def get_movies(self) -> List[Movie]:
        """Return a list of all movies in the database.

        Returns:
            List[Movie]: List of movies.
        """
        return list(self._movies.values())
    
    def get_user_movies(self, user_id: int) -> set[Movie]:
        """Return the set of movies associated with a user.

        Args:
            user_id (int): The user's identifier.

        Returns:
            set[Movie]: Set of movies for the user.
        """
        return self._user_movies.get(user_id, set())
    
    def calculate_popularity(self) -> None:
        """Recalculate the popularity of all movies based on user data."""
        self._popularity.clear()
        for user in self._users.values():
            for movie in user.get_movies():
                self._popularity[movie] += 1

    def get_popularity(self) -> Dict[Movie, int]:
        """Return a dictionary mapping movies to their popularity counts.

        Returns:
            Dict[Movie, int]: Popularity counts for each movie.
        """
        if not self._popularity:
            self.calculate_popularity()
        return dict(self._popularity)