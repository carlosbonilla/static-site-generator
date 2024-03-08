import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "target": "_balnk"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.boot.dev\" target=\"_balnk\"")

    def test_props_to_html_empty(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), "")