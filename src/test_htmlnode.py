import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
        )

    def test_eq(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        node2 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        node2 = HTMLNode("div", "Goodbye, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://www.google.com"})
        node2 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(
            "HTMLNode(div, Hello, world!, None, {'class': 'greeting', 'href': 'https://boot.dev'})", repr(node)
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_recursion(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()