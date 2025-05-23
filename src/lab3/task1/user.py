from typing import List
from .movie import Movie

class User:
    """Represents a user with a unique identifier and a list of movies associated with the user."""
    def __init__(self, identifier: int):
        """Initialize a User with a unique identifier.

        Args:
            identifier (int): The unique identifier for the user.

        Raises:
            ValueError: If the identifier is negative.
        """
        if identifier < 0:
            raise ValueError("User identifier cannot be negative")
        self._identifier = identifier
        self._movies = []

    def add_movies(self, movies: List[Movie]):
        """Add a list of movies to the user's movie list.

        Args:
            movies (List[Movie]): List of Movie objects to add.
        """
        self._movies.extend(movies)

    def get_movies(self) -> List[Movie]:
        """Return the list of movies associated with the user.

        Returns:
            List[Movie]: The user's movies.
        """
        return self._movies

    def get_identifier(self) -> int:
        """Return the user's unique identifier.

        Returns:
            int: The user's identifier.
        """
        return self._identifier
    
    def __str__(self):
        """Return a string representation of the user."""
        return f"User(identifier={self._identifier}, movies={self._movies})"
