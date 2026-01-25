import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType
from main import text_node_to_html_node


class TestMainFunctions(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "public/my_image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "public/my_image.png", "alt": "This is an image text node"})

    def test_text_node_to_html_node_link(self):
        node = TextNode("Click to go to Google!", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click to go to Google!")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})


if __name__ == "__main__":
    unittest.main()
