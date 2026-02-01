from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    prefix = ""
    for _ in range(6):
        prefix += "#"
        if block.startswith(prefix):
            return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    all_lines = block.split("\n")
    quote_lines = []
    ordered_list_lines = []
    unordered_list_lines = []
    for i, line in enumerate(all_lines):
        if line.strip().startswith(">"):
            quote_lines.append(line)
        elif line.strip().startswith("- "):
            unordered_list_lines.append(line)
        elif line.strip().startswith(f"{i + 1}. "):
            ordered_list_lines.append(line)

    if len(quote_lines) == len(all_lines):
        return BlockType.QUOTE
    if len(ordered_list_lines) == len(all_lines):
        return BlockType.ORDERED_LIST
    if len(unordered_list_lines) == len(all_lines):
        return BlockType.UNORDERED_LIST
    else:
        return BlockType.PARAGRAPH
