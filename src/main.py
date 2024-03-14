from textnode import TextNode
from htmlnode import HTMLNode

def main():
  text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(text_node)

  html_node = HTMLNode("a", "This is a text node", "bold", {"href": "https://www.boot.dev", "target": "_balnk"})
  print(html_node)

main()