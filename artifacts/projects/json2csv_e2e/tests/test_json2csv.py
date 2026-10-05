import unittest
from json2csv import to_csv

class TestJson2Csv(unittest.TestCase):
    def test_dict_to_csv(self):
        json_obj = {"name": "John", "age": 30, "city": "New York"}
        expected_csv = '"name": "John", "age": "30", "city": "New York"'
        self.assertEqual(to_csv(json_obj), expected_csv)

    def test_list_to_csv(self):
        json_obj = [{"name": "John", "age": 30}, {"name": "Anna", "age": 22}]
        expected_csv = '"name": "John", "age": "30"\n"name": "Anna", "age": "22"'
        self.assertEqual(to_csv(json_obj), expected_csv)

    def test_string_to_csv(self):
        json_obj = "Hello, World!"
        expected_csv = '"Hello, World!"'
        self.assertEqual(to_csv(json_obj), expected_csv)

if __name__ == '__main__':
    unittest.main()
