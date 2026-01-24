class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        final_string = []
        for key, value in self.props.items():
            final_string.append(f'{key}="{value}"')
        return " ".join(final_string)

    def __repr__(self):
        return f"""
            HTMLNode(\n\ttag: {self.tag}\n\tvalue: {self.value}\n\tchildren: {self.children}\n\tprops: {self.props_to_html}\n)
        """
