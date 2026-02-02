from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter
from src.split_nodes_images import split_nodes_images
from src.split_nodes_links import split_nodes_links


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_images(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    return new_nodes
