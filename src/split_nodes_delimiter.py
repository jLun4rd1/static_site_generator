from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)

        delimiter_count = 0
        comparison_parameter = 2 if delimiter != "**" else 4
        tmp_delimiter = delimiter if delimiter != "**" else "*"
        for char in node.text:
            if tmp_delimiter == char:
                delimiter_count += 1
        if delimiter_count % comparison_parameter != 0:
            raise SyntaxError(f"Some delimiter '{delimiter}' doesn't have its closing match in '{node.text}'")

        split_text = node.text.split(delimiter)
        new_nodes = []
        for i, text in enumerate(split_text):
            if i % 2 == 1:
                new_nodes.append(TextNode(text, text_type))
            elif text.strip():
                new_nodes.append(TextNode(text, TextType.TEXT))

        new_list.extend(new_nodes)
    return new_list
