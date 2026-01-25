from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        if delimiter not in node.text:
            raise SyntaxError(f"Delimiter '{delimiter}' not found in old node text '{node.text}'")
        split_text = node.text.split(delimiter)
        if len(split_text) != 3:
            raise SyntaxError(f"The function still doesn't support multiple separate sentences with the same type")
        new_nodes = [
            TextNode(split_text[0], TextType.TEXT),
            TextNode(split_text[1], text_type),
            TextNode(split_text[2], TextType.TEXT)
        ]
        new_list.extend(new_nodes)
    return new_list
