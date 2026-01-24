import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com"})
        expected = 'href="https://www.google.com"'
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_props_to_html_multiple_attributes(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = 'href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_props_to_html_no_attributes(self):
        node = HTMLNode("a", "click here", None, {})
        expected = ''
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_props_to_html_with_props_as_none(self):
        node = HTMLNode("a", "click here")
        expected = ''
        result = node.props_to_html()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
