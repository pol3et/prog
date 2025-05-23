class Movie:
    """Represents a movie with a unique identifier and title."""
    def __init__(self, identifier: int, title: str):
        """Initialize a Movie with a unique identifier and title.

        Args:
            identifier (int): The unique identifier for the movie.
            title (str): The title of the movie.

        Raises:
            ValueError: If the identifier is negative.
        """
        if identifier < 0:
            raise ValueError("Movie identifier cannot be negative")
        self._identifier = identifier
        self._title = title

    def get_title(self) -> str:
        """Return the title of the movie.

        Returns:
            str: The movie's title.
        """
        return self._title
    
    def get_identifier(self) -> int:
        """Return the unique identifier of the movie.

        Returns:
            int: The movie's identifier.
        """
        return self._identifier
    
    def __eq__(self, other):
        """Check if two Movie instances are equal based on their identifier.

        Args:
            other (Movie): The other Movie instance to compare.

        Returns:
            bool: True if identifiers are equal, False otherwise.
        """
        return self._identifier == other._identifier
    
    def __hash__(self):
        """Return the hash of the movie based on its identifier.

        Returns:
            int: The hash value.
        """
        return hash(self._identifier)
    
    def __str__(self):
        """Return a string representation of the movie."""
        return f"Movie(identifier={self._identifier}, title={self._title})"
