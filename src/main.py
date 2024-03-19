from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
  text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(text_node)

  html_node = HTMLNode("a", "This is a text node", "bold", {"href": "https://www.boot.dev", "target": "_balnk"})
  print(html_node)

  leaf_node = LeafNode("a", "boot.dev", {"href": "https://www.boot.dev", "target": "_balnk"})
  print(leaf_node)

  parent_node = ParentNode("div", [LeafNode("p", "boot.dev", {"href": "https://www.boot.dev", "target": "_balnk"})], {"class": "container"})
  print(parent_node)

main()