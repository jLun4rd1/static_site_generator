import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_bold_node(self):
        text_node = TextNode("I have some **bold** text in here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertIn(TextNode("I have some ", TextType.TEXT), new_nodes)
        self.assertIn(TextNode("bold", TextType.BOLD), new_nodes)
        self.assertIn(TextNode(" text in here.", TextType.TEXT), new_nodes)

    def test_single_code_node(self):
        text_node = TextNode("I have some `code` text in here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertIn(TextNode("I have some ", TextType.TEXT), new_nodes)
        self.assertIn(TextNode("code", TextType.CODE), new_nodes)
        self.assertIn(TextNode(" text in here.", TextType.TEXT), new_nodes)

    def test_single_italic_node(self):
        text_node = TextNode("I have some _italic_ text in here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertIn(TextNode("I have some ", TextType.TEXT), new_nodes)
        self.assertIn(TextNode("italic", TextType.ITALIC), new_nodes)
        self.assertIn(TextNode(" text in here.", TextType.TEXT), new_nodes)

    def test_multiple_italic_nodes(self):
        text_node1 = TextNode("I have some _italic_ text in here.", TextType.TEXT)
        text_node2 = TextNode("I have some _very italic_ text in here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node1, text_node2], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 6)
        self.assertIn(TextNode("italic", TextType.ITALIC), new_nodes)
        self.assertIn(TextNode("very italic", TextType.ITALIC), new_nodes)

    def test_starting_italic_node(self):
        text_node = TextNode("_I start italic._ Did you like it?", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 2)
        self.assertIn(TextNode("I start italic.", TextType.ITALIC), new_nodes)
        self.assertIn(TextNode(" Did you like it?", TextType.TEXT), new_nodes)

    def test_ending_italic_node(self):
        text_node = TextNode("What do you thing about _ending italic?_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 2)
        self.assertIn(TextNode("ending italic?", TextType.ITALIC), new_nodes)
        self.assertIn(TextNode("What do you thing about ", TextType.TEXT), new_nodes)

    def test_only_italic_node(self):
        text_node = TextNode("_This is me. Completely italic!_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 1)
        self.assertIn(TextNode("This is me. Completely italic!", TextType.ITALIC), new_nodes)

    def test_missing_closing_delimiter_node(self):
        text_node = TextNode("This is me. Completely** bold!", TextType.TEXT)
        with self.assertRaises(SyntaxError) as cm:
            new_nodes = split_nodes_delimiter([text_node], "**", TextType.ITALIC)
        the_exception = cm.exception
        self.assertIn("Some delimiter '**' doesn't", str(the_exception))


if __name__ == "__main__":
    unittest.main()
