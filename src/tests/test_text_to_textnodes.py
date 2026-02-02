import unittest
from src.textnode import TextNode, TextType
from src.text_to_textnodes import text_to_textnodes


class TestTextToTextNode(unittest.TestCase):
    def test_bold_and_italic_text(self):
        text = "I am **bold** and I am _italic_"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("I am ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and I am ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            nodes_list
        )

    def test_bold_and_code_text(self):
        text = "I am **bold** and I am `code`"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("I am ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and I am ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            nodes_list
        )

    def test_starting_bold_and_code_text(self):
        text = "**Bold** am I, and I am `code`"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Bold", TextType.BOLD),
                TextNode(" am I, and I am ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            nodes_list
        )

    def test_link_and_image_text(self):
        text = "I am a link [to google](https://www.google.com) and I am an ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("I am a link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and I am an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            nodes_list
        )

    def test_all_kinds_of_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes_list
        )
