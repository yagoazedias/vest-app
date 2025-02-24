import unittest

from tests.integration import TestIntegration

from tests.controller.file_reader.test_file_reader_factory import TestFileReaderFactory
from tests.controller.file_reader.test_csv_file_reader import TestCSVFileReader
from tests.controller.report_exporter.test_reporter_exporter_factory import TestReporterExporterFactory
from tests.controller.report_exporter.test_csv_reporter_exporter import TestCSVReporterExporter

if __name__ == '__main__':
    unittest.main()
