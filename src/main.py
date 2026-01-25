from textnode import TextNode, TextType
from leafnode import LeafNode


def main():
    text_node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )

main()
