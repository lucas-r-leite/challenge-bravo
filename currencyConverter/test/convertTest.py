import unittest

import sys
import os

# Add the root directory of your project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


class TestConvertCurrency(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client

    def test_amount_must_be_positive(self):
        response = self.app.get("/convert/?from=USD&to=EUR&amount=-1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, {"error": "Amount must be a positive number"})

    def test_invalid_amount_format(self):
        response = self.app.get("/convert/?from=USD&to=EUR&amount=abc")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Invalid amount format"})

    def test_missing_required_parameters(self):
        response = self.app.get("/convert/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, {"error": "Missing required parameters"})

    def test_successful_conversion(self):
        response = self.app.get("/convert/?from=USD&to=EUR&amount=10")
        self.assertEqual(response.status_code, 200)
        self.assertIn("converted_amount", response.json)


if __name__ == "__main__":
    unittest.main()
