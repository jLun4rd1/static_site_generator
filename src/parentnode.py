from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def _to_html(self):
        if not self.tag:
            raise ValueError("No tag found for ParentNode")
        if not self.children:
            raise ValueError("No children found for ParentNode")
        children_html_string = []
        for child in self.children:
            children_html_string.append(child._to_html())
        return f"<{self.tag}{self.props_to_html()}>{"".join(children_html_string)}</{self.tag}>"

    def __repr__(self):
        return f"""
            HTMLNode(\n\ttag: {self.tag}\n\tchildren: {self.children}\n\tprops: {self.props_to_html()}\n)
        """
