from src.lab3.task2.app import App
from src.lab3.task2.schemas import Person, AgeRange
from unittest import TestCase, main

class TestApp(TestCase):
    def setUp(self):
        self.app = App([18, 25, 35, 45, 60, 80, 100])

    def test_add_person(self):
        person = Person("Иванов Иван Иванович", 25)
        self.app.add_person(person)
        self.assertEqual(len(self.app._people), 1)

    def test_get_age_range(self):
        self.assertEqual(self.app._get_age_range(15), AgeRange(0, 18))
        self.assertEqual(self.app._get_age_range(18), AgeRange(0, 18))
        self.assertEqual(self.app._get_age_range(19), AgeRange(19, 25))
        self.assertEqual(self.app._get_age_range(25), AgeRange(19, 25))
        self.assertEqual(self.app._get_age_range(26), AgeRange(26, 35))
        self.assertEqual(self.app._get_age_range(30), AgeRange(26, 35))
        self.assertEqual(self.app._get_age_range(35), AgeRange(26, 35))
        self.assertEqual(self.app._get_age_range(36), AgeRange(36, 45))
        self.assertEqual(self.app._get_age_range(45), AgeRange(36, 45))
        self.assertEqual(self.app._get_age_range(46), AgeRange(46, 60))
        self.assertEqual(self.app._get_age_range(50), AgeRange(46, 60))
        self.assertEqual(self.app._get_age_range(60), AgeRange(46, 60))
        self.assertEqual(self.app._get_age_range(61), AgeRange(61, 80))
        self.assertEqual(self.app._get_age_range(80), AgeRange(61, 80))
        self.assertEqual(self.app._get_age_range(81), AgeRange(81, 100))
        self.assertEqual(self.app._get_age_range(90), AgeRange(81, 100))
        self.assertEqual(self.app._get_age_range(100), AgeRange(81, 100))
        self.assertEqual(self.app._get_age_range(101), AgeRange(101, None))
        self.assertEqual(self.app._get_age_range(110), AgeRange(101, None))

    def test_empty_bins_not_created(self):
        people = [
            Person("Иванов Иван Иванович", 30),
            Person("Петров Петр Петрович", 50)
        ]
        for person in people:
            self.app.add_person(person)
        self.app.create_bins()
        output = self.app.get_output()
        self.assertNotIn("0-18:", output)
        self.assertNotIn("81-100:", output)
        self.assertNotIn("101+:", output)

    def test_bins_order(self):
        people = [
            Person("Иванов Иван Иванович", 110),
            Person("Петров Петр Петрович", 90),
            Person("Сидоров Евгений Евгеньевич", 50),
            Person("Козлов Николай Николаевич", 30),
            Person("Смирнов Семен Семенович", 15)
        ]
        for person in people:
            self.app.add_person(person)
        output = self.app.get_output()
        output_lines = output.split("\n\n")
        try:
            self.assertTrue(output_lines[0].startswith("101+:"))
            self.assertTrue(output_lines[1].startswith("81-100:"))
            self.assertTrue(output_lines[2].startswith("46-60:"))
            self.assertTrue(output_lines[3].startswith("26-35:"))
            self.assertTrue(output_lines[4].startswith("0-18:"))
        except Exception as e:
            self.fail(f"{e}, {output_lines}")

    def test_people_sorting_in_bins(self):
        people = [
            Person("Иванов Иван Иванович", 88),
            Person("Петров Петр Петрович", 88),
            Person("Сидоров Евгений Евгеньевич", 88),
            Person("Козлов Николай Николаевич", 88)
        ]
        for person in people:
            self.app.add_person(person)
        output = self.app.get_output()
        bin_content = output.split(": ")[1]
        people_list = bin_content.split(", ")
        self.assertEqual(people_list[0], "Иванов Иван Иванович (88)")
        self.assertEqual(people_list[1], "Козлов Николай Николаевич (88)")
        self.assertEqual(people_list[2], "Петров Петр Петрович (88)")
        self.assertEqual(people_list[3], "Сидоров Евгений Евгеньевич (88)")

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            Person("Иванов Иван Иванович", -1)
        with self.assertRaises(ValueError):
            Person("Иванов Иван Иванович", 124)
        person = Person("Иванов Иван Иванович", 0)
        self.app.add_person(person)
        self.assertEqual(self.app._get_age_range(0), AgeRange(0, 18))
        
        app_with_one_border = App([50])
        self.assertEqual(app_with_one_border._get_age_range(30), AgeRange(0, 50))
        self.assertEqual(app_with_one_border._get_age_range(50), AgeRange(0, 50))
        self.assertEqual(app_with_one_border._get_age_range(51), AgeRange(51, None))
        
        app_with_ascending_borders = App([10, 20, 30])
        self.assertEqual(app_with_ascending_borders._borders, [30, 20, 10])
        self.assertEqual(app_with_ascending_borders._get_age_range(5), AgeRange(0, 10))
        self.assertEqual(app_with_ascending_borders._get_age_range(15), AgeRange(11, 20))
        self.assertEqual(app_with_ascending_borders._get_age_range(25), AgeRange(21, 30))
        self.assertEqual(app_with_ascending_borders._get_age_range(35), AgeRange(31, None))

if __name__ == "__main__":
    main()
