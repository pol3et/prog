from typing import NamedTuple

class AgeRange(NamedTuple):
    """Represents an age range with a start and optional end value.

    Args:
        start (int): The start of the age range.
        end (int | None): The end of the age range, or None for open-ended.
    """
    start: int
    end: int | None

    def __str__(self) -> str:
        """Return a string representation of the age range.

        Returns:
            str: The formatted age range as 'start-end' or 'start+'.
        """
        return f"{self.start}-{self.end}" if self.end else f"{self.start}+"

    @property
    def sort_key(self) -> int:
        """Return the start value for sorting age ranges.

        Returns:
            int: The start of the age range.
        """
        return self.start
    
class Person:
    """Represents a person with a name and age.

    Args:
        name (str): The person's name.
        age (int): The person's age.
    """
    def __init__(self, name, age):
        """Initialize a Person with a name and age.

        Args:
            name (str): The person's name.
            age (int): The person's age.

        Raises:
            ValueError: If age is negative or greater than 123.
        """
        self._name = name
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 123:
            raise ValueError("Age cannot be greater than 123")
        self._age = age

    @property
    def name(self) -> str:
        """Return the person's name.

        Returns:
            str: The name of the person.
        """
        return self._name

    @property
    def age(self) -> int:
        """Return the person's age.

        Returns:
            int: The age of the person.
        """
        return self._age

    def __str__(self) -> str:
        """Return a string representation of the person.

        Returns:
            str: The formatted string as 'name (age)'.
        """
        return f"{self.name} ({self.age})"