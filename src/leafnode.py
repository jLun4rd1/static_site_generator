from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def _to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"""
            HTMLNode(\n\ttag: {self.tag}\n\tvalue: {self.value}\n\tprops: {self.props_to_html()}\n)
        """
