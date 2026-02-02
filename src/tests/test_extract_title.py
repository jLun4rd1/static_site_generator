import unittest
from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is the title
"""
        title = extract_title(md)
        self.assertEqual(title, "This is the title")

    def test_extract_title_in_second_line(self):
        md = """
## This is not the title
# This is the title
"""
        title = extract_title(md)
        self.assertEqual(title, "This is the title")

    def test_extract_title_with_no_title(self):
        md = """
There is no title
## This is not the title
"""
        try:
            title = extract_title(md)
        except Exception as e:
            self.assertEqual(str(e), "No title found in markdown")
