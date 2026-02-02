import unittest
from src.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote_block(self):
        md = """
> This is a quote

> This is a **second** quote
>And this is also _valid_
"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote><blockquote>This is a <b>second</b> quote And this is also <i>valid</i></blockquote></div>",
        )

    def test_unordered_list_block(self):
        md = """
- My _single_ item unordered list

- My **double** item
- unordered `list`
"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><ul><li>My <i>single</i> item unordered list</li></ul><ul><li>My <b>double</b> item</li><li>unordered <code>list</code></li></ul></div>",
        )

    def test_ordered_list_block(self):
        md = """
1. My single item _ordered_ list

1. My **double** item
2. `ordered` list
"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><ol><li>My single item <i>ordered</i> list</li></ol><ol><li>My <b>double</b> item</li><li><code>ordered</code> list</li></ol></div>",
        )

    def test_heading_block(self):
        md = """
# Heading _1_

## Heading `2`

### Heading **3**
"""
        node = markdown_to_html_node(md)
        html = node._to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading <i>1</i></h1><h2>Heading <code>2</code></h2><h3>Heading <b>3</b></h3></div>",
        )
