import unittest

from htmlnode import HTMLNode, LeafNode

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
        