import unittest
from textnode import TextNode, TextType
from split_nodes_links import split_nodes_links


class TestSplitNodesLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to google](https://www.google.com) and another [to youtube](https://www.youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com"),
            ],
            new_nodes,
        )

    def test_split_starting_link(self):
        node = TextNode(
            "[To google](https://www.google.com). What about now that I started with a link?",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("To google", TextType.LINK, "https://www.google.com"),
                TextNode(". What about now that I started with a link?", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_ending_link(self):
        node = TextNode(
            "What about now that I ended with a link [to google](https://www.google.com)?",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("What about now that I ended with a link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode("?", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_with_leading_and_trailing_space(self):
        node = TextNode(
            " [Google](https://www.google.com) ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("Google", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_spilt_two_links_with_starting_second(self):
        node = TextNode(
            "This is text with a link [to google](https://www.google.com), [to youtube](https://www.youtube.com) and it ends",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(", ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com"),
                TextNode(" and it ends", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_two_starting_links(self):
        node = TextNode(
            "[Google](https://www.google.com) this is text with a link [to youtube](https://www.youtube.com) and it ends",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" this is text with a link ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com"),
                TextNode(" and it ends", TextType.TEXT),
            ],
            new_nodes,
        )
