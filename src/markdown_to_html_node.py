from src.textnode import TextNode, TextType
from src.parentnode import ParentNode
from src.markdown_to_blocks import markdown_to_blocks
from src.block_to_block_type import block_to_block_type, BlockType
from src.text_to_textnodes import text_to_textnodes
from src.text_node_to_html_node import text_node_to_html_node


def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown)
    list_of_html_blocks = []
    for block in list_of_blocks:
        block_type = block_to_block_type(block)
        block_html_node = _get_block_html_node(block, block_type)
        list_of_html_blocks.append(block_html_node)
    div_node = ParentNode("div", list_of_html_blocks)
    return div_node

def _get_block_html_node(block, block_type):
    if block_type == BlockType.QUOTE:
        return ParentNode(tag="blockquote", children=_get_block_children(block, block_type))
    if block_type == BlockType.PARAGRAPH:
        return ParentNode(tag="p", children=_get_block_children(block, block_type))
    elif block_type == BlockType.UNORDERED_LIST:
        return ParentNode(tag="ul", children=_get_block_children(block, block_type))
    elif block_type == BlockType.ORDERED_LIST:
        return ParentNode(tag="ol", children=_get_block_children(block, block_type))
    elif block_type == BlockType.CODE:
        return ParentNode(tag="pre", children=[ParentNode(tag="code", children=_get_block_children(block, block_type))])
    elif block_type == BlockType.HEADING:
        number_of_hashes, prefix = _get_number_of_hashes_and_prefix(block)
        return ParentNode(tag=f"h{number_of_hashes}", children=_get_block_children(block, block_type, prefix))

def _get_number_of_hashes_and_prefix(block):
    prefix = ""
    count = 0
    for _ in range(6):
        prefix += "#"
        if block.startswith(prefix):
            count += 1
        else:
            break
    prefix = prefix[:-1]
    return count, prefix

def _get_block_children(block, block_type, prefix=None):
    if block_type == BlockType.CODE:
        block = block.split("```")[1].lstrip()
        text_node = TextNode(block, TextType.TEXT)
        return [text_node_to_html_node(text_node)]
    elif block_type == BlockType.HEADING:
        block = block.replace(f"{prefix} ", "")
    children = []
    all_lines = block.split("\n")
    for line in all_lines:
        line = _treat_line(line, all_lines, block_type)
        line_text_nodes = text_to_textnodes(line)
        line_html_nodes = []
        for text_node in line_text_nodes:
            child_html_node = text_node_to_html_node(text_node)
            line_html_nodes.append(child_html_node)

        if block_type in [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]:
            children.extend([ParentNode("li", line_html_nodes)])
        else:
            children.extend(line_html_nodes)

    return children

def _treat_line(line, all_lines, block_type):
    if block_type == BlockType.PARAGRAPH:
        line = _add_extra_space(line, all_lines)
    elif block_type == BlockType.QUOTE:
        line = _add_extra_space(line, all_lines)
        if line.startswith("> "):
            line = line.replace("> ", "")
        else:
            line = line.replace(">", "")
    elif block_type == BlockType.UNORDERED_LIST:
        line = line.replace("- ", "")
    elif block_type == BlockType.ORDERED_LIST:
        line_number = all_lines.index(line) + 1
        line = line.replace(f"{line_number}. ", "")
    return line

def _add_extra_space(line, all_lines):
    """If it's not the last line, add a space to separate from the next line's words"""
    if all_lines.index(line) != len(all_lines) - 1:
        line = line + " "
    return line
