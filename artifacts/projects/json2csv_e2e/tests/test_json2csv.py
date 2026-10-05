import unittest
from json2csv import to_csv

class TestJson2Csv(unittest.TestCase):
    def test_dict_to_csv(self):
        json_obj = {"name": "Alice", "age": 30}
        expected_csv = "name:Alice,age:30"
        self.assertEqual(to_csv(json_obj), expected_csv)

    def test_list_to_csv(self):
        json_obj = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        expected_csv = "name:Alice,age:30\nname:Bob,age:25"
        self.assertEqual(to_csv(json_obj), expected_csv)

    def test_string_to_csv(self):
        json_obj = "Hello, World!"
        expected_csv = "Hello, World!"
        self.assertEqual(to_csv(json_obj), expected_csv)

if __name__ == '__main__':
    unittest.main()
