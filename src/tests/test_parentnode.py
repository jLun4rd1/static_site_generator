import unittest
from src.leafnode import LeafNode
from src.parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node._to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_and_attribute(self):
        child_node = LeafNode("span", "child", {"c_attr1": "c_value1"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node._to_html(), '<div><span c_attr1="c_value1">child</span></div>')

    def test_to_html_with_children_and_attr_for_both_children_and_parent(self):
        child_node = LeafNode("span", "child", {"c_attr1": "c_value1"})
        parent_node = ParentNode("div", [child_node], {"has_bold": True})
        self.assertEqual(parent_node._to_html(), '<div has_bold="True"><span c_attr1="c_value1">child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node._to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grand_grandchildren(self):
        grand_grandchild_node = LeafNode("b", "grand_grandchild")
        grandchild_node = ParentNode("p", [grand_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node._to_html(),
            "<div><span><p><b>grand_grandchild</b></p></span></div>",
        )

    def test_to_html_with_grand_grandchildren_and_attributes(self):
        grand_grandchild_node = LeafNode("b", "grand_grandchild", {"bold": True})
        grandchild_node = ParentNode("p", [grand_grandchild_node])
        child_node = ParentNode("span", [grandchild_node], {"span": True})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node._to_html(),
            '<div><span span="True"><p><b bold="True">grand_grandchild</b></p></span></div>',
        )

    def test_to_html_with_children_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        try:
            self.assertEqual(parent_node._to_html(), "<div><span>child</span></div>")
        except Exception as e:
            self.assertIn("No tag", str(e))

    def test_to_html_with_children_no_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [])
        try:
            self.assertEqual(parent_node._to_html(), "<div><span>child</span></div>")
        except Exception as e:
            self.assertIn("No children", str(e))


if __name__ == "__main__":
    unittest.main()
