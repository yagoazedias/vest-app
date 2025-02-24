import unittest

from lib.controller.file_reader.file_reader_factory import FileReaderFactory
from lib.controller.file_reader.csv_file_reader import CSVFileReader

class TestFileReaderFactory(unittest.TestCase):

    def test_create_interface_csv(self):
        file_path = 'test.csv'
        reader = FileReaderFactory.create_interface(file_path)
        self.assertIsInstance(reader, CSVFileReader)

    def test_create_interface_unsupported_file_type(self):
        file_path = 'test.txt'
        with self.assertRaises(ValueError) as context:
            FileReaderFactory.create_interface(file_path)
        self.assertEqual(str(context.exception), "Unsupported file type")
