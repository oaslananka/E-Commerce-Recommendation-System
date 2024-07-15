import unittest
import os
from src.utils.helpers import setup_logging, log_info, log_error


class TestHelpers(unittest.TestCase):
    """
    A test case class for testing helper functions.
    """

    def setUp(self):
        self.log_file = 'logs/test_app.log'
        setup_logging(self.log_file)

    def test_setup_logging(self):
        self.assertTrue(os.path.exists(self.log_file))

    def test_log_info(self):
        log_info('Test information message')
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn('Test information message', logs)

    def test_log_error(self):
        log_error('Test error message')
        with open(self.log_file, 'r') as file:
            logs = file.read()
            self.assertIn('Test error message', logs)


if __name__ == '__main__':
    unittest.main()
