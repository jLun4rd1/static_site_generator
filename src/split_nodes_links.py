from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links


def split_nodes_links(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_list.append(node)
            continue

        tmp_text = node.text
        for match in matches:
            new_nodes = []
            formatted_link = f"[{match[0]}]({match[1]})"
            sections = tmp_text.split(formatted_link, 1)
            text = sections[0]
            text2 = sections[1]

            if text.strip():
                new_nodes.append(TextNode(text, TextType.TEXT))

            new_nodes.append(TextNode(match[0], TextType.LINK, url=match[1]))

            if matches.index(match) == len(matches) - 1 and text2.strip():
                new_nodes.append(TextNode(text2, TextType.TEXT))

            new_list.extend(new_nodes)
            tmp_text = text2

    return new_list