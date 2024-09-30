import unittest
import os
from dotenv import load_dotenv
from main import greeting

class TestGreeting(unittest.TestCase):
    def setUp(self):
        load_dotenv()

    def test_greeting(self):
        expected_prefix = os.getenv('GREETING_PREFIX', 'Hello')
        self.assertEqual(greeting("Alice"), f"{expected_prefix}, Alice!")
        self.assertEqual(greeting("Bob"), f"{expected_prefix}, Bob!")

if __name__ == "__main__":
    unittest.main()