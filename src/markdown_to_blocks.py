def markdown_to_blocks(markdown):
    list_of_blocks = []
    raw_list = markdown.split("\n\n")
    for block in raw_list:
        stripped_block = block.strip()
        if stripped_block:
            list_of_blocks.append(stripped_block)
    return list_of_blocks
