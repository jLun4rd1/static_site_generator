import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        result = node._to_html()
        self.assertEqual(expected, result)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click here", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">click here</a>'
        result = node._to_html()
        self.assertEqual(expected, result)

    def test_leaf_to_html_a_multiple_attributes(self):
        node = LeafNode("a", "click here", {"href": "https://www.google.com", "target": "_blank"})
        expected = '<a href="https://www.google.com" target="_blank">click here</a>'
        result = node._to_html()
        self.assertEqual(expected, result)

    def test_leaf_to_html_a_no_attributes(self):
        node = LeafNode("a", "click here", {})
        expected = '<a>click here</a>'
        result = node._to_html()
        self.assertEqual(expected, result)

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "I am a raw text")
        expected = 'I am a raw text'
        result = node._to_html()
        self.assertEqual(expected, result)

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        try:
            result = node._to_html()
        except Exception as e:
            self.assertIsInstance(e, ValueError)


if __name__ == "__main__":
    unittest.main()
