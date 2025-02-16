import subprocess
import unittest


class TestIntegration(unittest.TestCase):

    def setUp(self):
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    def read_expected_output(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def run_authorize_script(self, input_file):
        with open(input_file, "r") as file:
            result = subprocess.run(
                ["python3", "main.py"],
                stdin=file,
                stdout=subprocess.PIPE,
                text=True,
                check=True
            )
        return result.stdout

    def test_account_creation_success(self):
        expected_output = self.read_expected_output("tests/integration/expected/output_file_main_case.csv")
        output = self.run_authorize_script("tests/integration/samples/input_file_main_case.csv")
        self.assertEqual(expected_output, output)
