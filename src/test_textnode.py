import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Text with no URL", "normal", None)
        node2 = TextNode("Text with no URL", "normal")
        self.assertEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("Text with URL", "normal", "http://example.com")
        node2 = TextNode("Text with URL", "normal")
        self.assertNotEqual(node, node2)

    def test_text_type_diff(self):
        node = TextNode("Text with different style", "bold")
        node2 = TextNode("Text with different style", "italic")
        self.assertNotEqual(node, node2)

    def test_text_content_diff(self):
        node = TextNode("First text", "normal")
        node2 = TextNode("Second text", "normal")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
