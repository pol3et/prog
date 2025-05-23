from typing import List
from collections import defaultdict
from .schemas import Person, AgeRange

class App:
    """Application for binning people into age ranges based on provided borders."""
    def __init__(self, borders: List[int]):
        """Initialize the application with age borders.

        Args:
            borders (List[int]): List of age borders for binning.
        """
        self._people = []
        self._borders = sorted(borders, reverse=True)
        self._bins = defaultdict(list)

    def add_person(self, person: Person):
        """Add a person to the application.

        Args:
            person (Person): The person to add.
        """
        self._people.append(person)

    def _get_age_range(self, age: int) -> AgeRange:
        """Determine the age range for a given age based on borders.

        Args:
            age (int): The age to classify.

        Returns:
            AgeRange: The corresponding age range.

        Raises:
            ValueError: If the age does not fit any range.
        """
        if age > self._borders[0]:
            return AgeRange(self._borders[0] + 1, None)
        
        if age <= self._borders[-1]:
            return AgeRange(0, self._borders[-1])
            
        for i in range(len(self._borders) - 1):
            upper_border = self._borders[i]
            lower_border = self._borders[i + 1]
            if lower_border < age <= upper_border:
                return AgeRange(lower_border + 1, upper_border)
                
        raise ValueError(f"Could not determine age range for age: {age}")

    def create_bins(self):
        """Assign all people to their respective age bins."""
        for person in self._people:
            age_range = self._get_age_range(person.age)
            if person not in self._bins[age_range]:
                self._bins[age_range].append(person)

    def get_output(self) -> str:
        """Return a formatted string of all people grouped by age range, sorted by age range and person details.

        Returns:
            str: The formatted output string.
        """
        self.create_bins()
        output = []
        
        for age_range, people in sorted(
            self._bins.items(),
            key=lambda x: -x[0].sort_key
        ):
            if len(people) == 0:
                continue
            sorted_people = sorted(people, key=lambda x: (-x.age, x.name))
            people_str = ", ".join(f"{person}" for person in sorted_people)
            output.append(f"{age_range}: {people_str}")
        
        return "\n\n".join(output)
