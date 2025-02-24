import unittest
from lib.controller.report_exporter.reporter_exporter_factory import ReporterExporterFactory
from lib.controller.report_exporter.csv_report_exporter import CSVReporterExporter

class TestReporterExporterFactory(unittest.TestCase):

    def test_create_exporter_csv(self):
        exporter = ReporterExporterFactory.create_exporter('csv')
        self.assertIsInstance(exporter, CSVReporterExporter)

    def test_invalid_format(self):
        with self.assertRaises(ValueError) as context:
            ReporterExporterFactory.create_exporter('invalid_format')
        self.assertEqual(str(context.exception), "Unsupported format type")