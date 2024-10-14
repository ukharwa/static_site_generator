import unittest

from textnode import TextNode
from main import *

class TestTextNode(unittest.TestCase):
    # def test_eq(self):
    #     node = TextNode("This is a text node", "bold")
    #     node2 = TextNode("This is a text node", "bold")
    #     self.assertEqual(node, node2)

    #     node = TextNode("This is a text node", "italic" ,"url")
    #     node2 = TextNode("This is a text node", "bold", "url")
    #     self.assertNotEqual(node, node2)

    #     node = TextNode("This is a text node", "bold", "url")
    #     node2 = TextNode("This is an text node", "bold", "url")
    #     self.assertNotEqual(node, node2)

    #     node = TextNode("This is a text node", "bold", "url")
    #     node2 = TextNode("This is a text node", "bold")
    #     self.assertNotEqual(node, node2)

    #     node = TextNode("This is a text node", "bold", "url")
    #     node2 = TextNode("This is a text node", "bold", "uri")
    #     self.assertNotEqual(node, node2)

    # def test_convert(self):
    #     node = TextNode("text content", "bold")
    #     print(textNode_to_HTMLNode(node).to_HTML())

    #     node = TextNode("text content", "italic")
    #     print(textNode_to_HTMLNode(node).to_HTML())

    #     node = TextNode("text content", "image", "lkasdfjh")
    #     print(textNode_to_HTMLNode(node).to_HTML())

    #     node = TextNode("text content", "link", "lkasdfjh")
    #     print(textNode_to_HTMLNode(node).to_HTML())

    # def test_split(self):
    #     node = TextNode("This is text with a `code block` word", "text")
    #     print(split_nodes_delimiter([node], "`", "code"))

    #     node = TextNode("This is text with **bold text** in it" ,"text")
    #     print(split_nodes_delimiter([node], "**", "bold"))

    #     node = TextNode("This is *text* with *italic text* in it" ,"text")
    #     print(split_nodes_delimiter([node], "*", "italic"))

    #     node = TextNode("Thi*s is text with italic text in it" ,"text")
    #     print(split_nodes_delimiter([node], "*", "italic"))

    # def test_extract(self):
    #     text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #     text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #     print("images text", extract_markdown_images(text))
    #     print("images text1", extract_markdown_images(text1))
    #     print("link text", extract_markdown_links(text))
    #     print("link text1", extract_markdown_links(text1))

    # def test_link_split(self):
    #     node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", "text")
    #     print(split_nodes_image([node]))

    #     node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) Hello", "text")
    #     print(split_nodes_image([node]))

    #     node = TextNode("![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) Hello", "text")
    #     print(split_nodes_image([node]))

    #     node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")
    #     print(split_nodes_link([node]))

    #     node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) Hello", "text")
    #     print(split_nodes_link([node]))

    #     node = TextNode("![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) Hello", "text")
    #     print(split_nodes_link([node]))

    def test_all(self):
        text = "This is **text** with an *italic* word **and** a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and *a* [link](https://boot.dev)"
        print(text_to_text_nodes(text))

if __name__ == "__main__":
    unittest.main()