import unittest
import sys
sys.path.append("..")
from source.person import *


class TestMethods(unittest.TestCase):
    def test_person_creation(self):
        # Arrange
        dan = Person("Dan", 1)

        expected_output_name = "Dan"
        expected_output_id = 1

        # Act
        actual_output_name = dan.get_name()
        actual_output_id = dan.get_id()

        # Assert
        self.assertEqual(actual_output_name, expected_output_name)
        self.assertEqual(actual_output_id, expected_output_id)

    def test_person_rename(self):
        # Arrange
        dan = Person("Dan", 1)

        expected_output = "Ralph"

        # Act
        dan.rename("Ralph")

        # Assert
        self.assertEqual(expected_output, dan.get_name())

    def test_list_creation(self):
        # Arrange
        dan = Person("Dan", 1)
        giles = Person("Giles", 2)
        conner = Person("Conner", 3)
        people_list = [dan, giles, conner]
        instance = PeopleList(False, people_list)

        expected_output = ["Dan", "Giles", "Conner"]

        # Act
        actual_output = instance.get_name_list()

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_append_person(self):
        # Arrange
        dan = Person("Dan", 1)
        giles = Person("Giles", 2)
        conner = Person("Conner", 3)
        people_list = [dan, giles]
        instance = PeopleList(False, people_list)

        expected_output = ["Dan", "Giles", "Conner"]

        # Act
        instance.append_person(conner)

        # Assert
        self.assertEqual(expected_output, instance.get_name_list())


if __name__ == "__main__":
    unittest.main()