import unittest

from unittest.mock import patch
from lib.controller.report_exporter.csv_report_exporter import CSVReporterExporter


class TestCSVReporterExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = CSVReporterExporter()

    @patch('lib.controller.report_exporter.csv_report_exporter.EmployeeUsecaseFactory.create_usecase')
    @patch('builtins.print')
    def test_export_with_valid_employee_data(self, mocked_print, create_usecase_mock):
        usecase_mock = unittest.mock.Mock()
        usecase_mock.get_all.return_value = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {"102": {"amount": 2000}}}
        }
        create_usecase_mock.return_value = usecase_mock
        exporter = CSVReporterExporter()
        exporter.export()
        mocked_print.assert_called_once_with("1,John Doe,101,1000\n2,Jane Smith,102,2000")

    @patch('lib.controller.report_exporter.csv_report_exporter.EmployeeUsecaseFactory.create_usecase')
    @patch('builtins.print')
    def test_export_with_empty_employee_data(self, mocked_print, create_usecase_mock):
        usecase_mock = unittest.mock.Mock()
        usecase_mock.get_all.return_value = {}
        create_usecase_mock.return_value = usecase_mock
        exporter = CSVReporterExporter()
        exporter.export()
        mocked_print.assert_called_once_with("")

    @patch('lib.controller.report_exporter.csv_report_exporter.EmployeeUsecaseFactory.create_usecase')
    @patch('builtins.print')
    def test_export_with_missing_fields(self, mocked_print, create_usecase_mock):
        usecase_mock = unittest.mock.Mock()
        usecase_mock.get_all.return_value = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {}}
        }
        create_usecase_mock.return_value = usecase_mock
        exporter = CSVReporterExporter()
        exporter.export()
        mocked_print.assert_called_once_with("1,John Doe,101,1000")

    @patch('lib.controller.report_exporter.csv_report_exporter.EmployeeUsecaseFactory.create_usecase')
    @patch('builtins.print')
    def test_export_with_special_characters(self, mocked_print, create_usecase_mock):
        usecase_mock = unittest.mock.Mock()
        usecase_mock.get_all.return_value = {
            "1": {"name": "John, Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {"102": {"amount": 2000}}}
        }
        create_usecase_mock.return_value = usecase_mock
        exporter = CSVReporterExporter()
        exporter.export()
        mocked_print.assert_called_once_with("1,John, Doe,101,1000\n2,Jane Smith,102,2000")

    @patch('lib.controller.report_exporter.csv_report_exporter.EmployeeUsecaseFactory.create_usecase')
    @patch('builtins.print')
    def test_export_with_multiple_equities(self, mocked_print, create_usecase_mock):
        usecase_mock = unittest.mock.Mock()
        usecase_mock.get_all.return_value = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}, "102": {"amount": 1500}}},
            "2": {"name": "Jane Smith", "equities": {"103": {"amount": 2000}}}
        }
        create_usecase_mock.return_value = usecase_mock
        exporter = CSVReporterExporter()
        exporter.export()
        mocked_print.assert_called_once_with("1,John Doe,101,1000\n1,John Doe,102,1500\n2,Jane Smith,103,2000")

    def test_convert_json_to_csv_with_valid_employee_data(self):
        employees = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {"102": {"amount": 2000}}}
        }
        expected_csv = "1,John Doe,101,1000\n2,Jane Smith,102,2000"
        self.assertEqual(self.exporter._convert_json_to_csv(employees), expected_csv)

    def test_convert_json_to_csv_with_empty_employee_data(self):
        employees = {}
        expected_csv = ""
        self.assertEqual(self.exporter._convert_json_to_csv(employees), expected_csv)

    def test_convert_json_to_csv_with_missing_fields(self):
        employees = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {}}
        }
        expected_csv = "1,John Doe,101,1000"
        self.assertEqual(self.exporter._convert_json_to_csv(employees), expected_csv)

    def test_convert_json_to_csv_with_special_characters(self):
        employees = {
            "1": {"name": "John, Doe", "equities": {"101": {"amount": 1000}}},
            "2": {"name": "Jane Smith", "equities": {"102": {"amount": 2000}}}
        }
        expected_csv = "1,John, Doe,101,1000\n2,Jane Smith,102,2000"
        self.assertEqual(self.exporter._convert_json_to_csv(employees), expected_csv)

    def test_convert_json_to_csv_with_multiple_equities(self):
        employees = {
            "1": {"name": "John Doe", "equities": {"101": {"amount": 1000}, "102": {"amount": 1500}}},
            "2": {"name": "Jane Smith", "equities": {"103": {"amount": 2000}}}
        }
        expected_csv = "1,John Doe,101,1000\n1,John Doe,102,1500\n2,Jane Smith,103,2000"
        self.assertEqual(self.exporter._convert_json_to_csv(employees), expected_csv)
