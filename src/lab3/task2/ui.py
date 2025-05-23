from .app import App
from .schemas import Person

class UI:
    """User interface for interacting with the age binning application."""
    def __init__(self):
        """Initialize the UI, prompt for borders, and create the App instance."""
        borders = input("Enter borders: ").split(" ")
        if len(borders) == 0:
            raise ValueError("Borders cannot be empty")
        self._app = App(list(map(int, borders)))

    def run(self):
        """Run the main input loop for adding people and displaying the output."""
        while True:
            person_str = input("Enter name and age: ")
            if person_str == "END":
                break
            try:
                name, age = person_str.split(",")
                self._app.add_person(Person(name, int(age)))
            except ValueError as e:
                print(e)

        output = self._app.get_output()
        print(output)

if __name__ == "__main__":
    ui = UI()
    ui.run()