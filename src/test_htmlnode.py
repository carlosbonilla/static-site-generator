import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "target": "_balnk"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.boot.dev\" target=\"_balnk\"")

    def test_props_to_html_empty(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "boot.dev", None)
        self.assertEqual(node.to_html(), "<p>boot.dev</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "boot.dev", None)
        self.assertEqual(node.to_html(), "boot.dev")

    def test_to_html_no_value(self):
        node = LeafNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_props(self):
        node = LeafNode("a", "boot.dev", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.boot.dev\">boot.dev</a>")

        
class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "boot.dev")], None)
        self.assertEqual(node.to_html(), "<div><p>boot.dev</p></div>")
        
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "boot.dev")], None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_children(self):
        node = ParentNode("div", [], None)
        self.assertEqual(node.to_html(), "<div></div>") 

    def test_to_html_nested(self):
        node = ParentNode("div", [ParentNode("p", [LeafNode("a", "boot.dev", {"href": "https://www.boot.dev"})])], None)
        self.assertEqual(node.to_html(), "<div><p><a href=\"https://www.boot.dev\">boot.dev</a></p></div>")

    def test_to_html_with_grandchildren(self):
        node = ParentNode("div", [ParentNode("p", [LeafNode("a", "boot.dev", {"href": "https://www.boot.dev"})]), ParentNode("p", [LeafNode("a", "boot.dev", {"href": "https://www.boot.dev"})])], None)
        self.assertEqual(node.to_html(), "<div><p><a href=\"https://www.boot.dev\">boot.dev</a></p><p><a href=\"https://www.boot.dev\">boot.dev</a></p></div>")