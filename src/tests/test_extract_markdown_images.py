import unittest
from src.extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_missing_exclamation_point(self):
        matches = extract_markdown_images(
            "This is text with a link [to google](https://www.google.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple_images(self):
        matches = extract_markdown_images(
            """
            This is text with image A ![image A](https://i.imgur.com/zjjcJKZ.png)
            and image B ![image B](https://imgur.com/gallery/wild-regex-bug-appeared-Alk0gcf#/t/regex)
            """
        )
        self.assertListEqual(
            [
                ("image A", "https://i.imgur.com/zjjcJKZ.png"),
                ("image B", "https://imgur.com/gallery/wild-regex-bug-appeared-Alk0gcf#/t/regex")
            ],
            matches
        )


if __name__ == "__main__":
    unittest.main()
