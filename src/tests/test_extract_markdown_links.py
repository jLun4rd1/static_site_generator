import unittest
from src.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_links_with_exclamation_point(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to google](https://www.google.com)"
        )
        self.assertListEqual([("to google", "https://www.google.com")], matches)

    def test_extract_markdown_links_multiple_images(self):
        matches = extract_markdown_links(
            """
            This is text with a link [to google](https://www.google.com)
            and [to youtube](https://www.youtube.com)
            """
        )
        self.assertListEqual(
            [
                ("to google", "https://www.google.com"),
                ("to youtube", "https://www.youtube.com")
            ],
            matches
        )


if __name__ == "__main__":
    unittest.main()
