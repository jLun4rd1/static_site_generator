import unittest
from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_one_block(self):
        block = "# Heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_three_block(self):
        block = "### Heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_six_block(self):
        block = "####### Heading 6"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = """```
def my_function_code():
    print("Hello World")
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        block = """> This is okay for quotes
>This is okay, too"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = """- Do the dishes
- Clean up the bedroom
- Feed the dog"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = """1. Sign into boot.dev
2. Code a bunch of projects
3. Become a master coder"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph_list_block(self):
        block = "Just a good old paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
