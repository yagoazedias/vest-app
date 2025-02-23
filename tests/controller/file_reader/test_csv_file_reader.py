import unittest

from unittest.mock import patch, mock_open, MagicMock
from lib.controller.file_reader.csv_file_reader import CSVFileReader
from lib.constants.events import EVENT_DATE_FORMAT
from datetime import datetime

class TestCSVFileReader(unittest.TestCase):

    @patch('lib.controller.file_reader.csv_file_reader.open', new_callable=mock_open, read_data="event1,2020-04-01\n")
    @patch('lib.controller.file_reader.csv_file_reader.csv.reader')
    @patch('lib.controller.file_reader.csv_file_reader.EventFactory.create')
    @patch('lib.controller.file_reader.csv_file_reader.EventUsecaseFactory.create_usecase')
    def test_read(self, mock_create_usecase, mock_create_event, mock_csv_reader, mock_open):
        # Given
        mock_csv_reader.return_value = [["event1", "2020-04-01"]]
        mock_event = MagicMock()
        mock_create_event.return_value = mock_event
        mock_usecase = MagicMock()
        mock_create_usecase.return_value = mock_usecase
        target_date = "2020-04-01"
        file_path = "dummy_path.csv"
        reader = CSVFileReader()

        # When
        reader.read(file_path, target_date)

        # Then
        mock_open.assert_called_once_with(file_path, mode='r', newline='')
        mock_csv_reader.assert_called_once()
        mock_create_event.assert_called_once_with("event1", "2020-04-01")
        mock_create_usecase.assert_called_once_with(mock_event)
        mock_usecase.process.assert_called_once_with(mock_event, datetime.strptime(target_date, EVENT_DATE_FORMAT))

if __name__ == '__main__':
    unittest.main()