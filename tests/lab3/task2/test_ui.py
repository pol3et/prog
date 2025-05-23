from src.lab3.task2.ui import UI
from unittest import TestCase, main
from io import StringIO
import sys

class TestUI(TestCase):
    def setUp(self):
        self.original_stdin = sys.stdin
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout

    def test_ui_output(self):
        test_input = StringIO("18 25 35 45 60 80 100\n"
                            "Кошельков Захар Брониславович,105\n"
                            "Дьячков Нисон Иринеевич,88\n"
                            "Иванов Варлам Якунович,88\n"
                            "Старостин Ростислав Ермолаевич,50\n"
                            "Ярилова Розалия Трофимовна,29\n"
                            "Соколов Андрей Сергеевич,15\n"
                            "Егоров Алан Петрович,7\n"
                            "END")
        sys.stdin = test_input
        ui = UI()
        ui.run()
        output = sys.stdout.getvalue()
        
        actual_output_start = output.find("101+:")
        if actual_output_start != -1:
            actual_output = output[actual_output_start:].strip()
        else:
            actual_output = output.strip()
        
        expected_output = """101+: Кошельков Захар Брониславович (105)

81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)

46-60: Старостин Ростислав Ермолаевич (50)

26-35: Ярилова Розалия Трофимовна (29)

0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)"""
        
        self.assertEqual(actual_output, expected_output)

    def test_invalid_input(self):
        test_input = StringIO("18 35 60 100\ninvalid\nEND")
        sys.stdin = test_input
        ui = UI()
        ui.run()
        output = sys.stdout.getvalue()
        self.assertIn("not enough values to unpack", output)

    def test_empty_borders(self):
        test_input = StringIO("\n")
        sys.stdin = test_input
        with self.assertRaises(ValueError):
            UI()

if __name__ == "__main__":
    main()
