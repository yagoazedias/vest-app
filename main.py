import sys

from lib.constants.events import EXPORTER_TYPE
from lib.controller.file_reader.file_reader_factory import FileReaderFactory
from lib.controller.report_exporter.reporter_exporter_factory import ReporterExporterFactory


def main():
    file_path = sys.argv[1]
    target_date = sys.argv[2]
    FileReaderFactory.create_interface(file_path).read(file_path, target_date)
    ReporterExporterFactory.create_exporter(EXPORTER_TYPE).export()

if __name__ == '__main__':
    main()
