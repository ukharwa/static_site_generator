import unittest

from textnode import TextNode
from main import textNode_to_HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", "italic" ,"url")
        node2 = TextNode("This is a text node", "bold", "url")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is an text node", "bold", "url")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a text node", "bold", "uri")
        self.assertNotEqual(node, node2)

    def test_convert(self):
        node = TextNode("text content", "bold")
        print(textNode_to_HTMLNode(node).to_HTML())

        node = TextNode("text content", "italic")
        print(textNode_to_HTMLNode(node).to_HTML())

        node = TextNode("text content", "image", "lkasdfjh")
        print(textNode_to_HTMLNode(node).to_HTML())

        node = TextNode("text content", "link", "lkasdfjh")
        print(textNode_to_HTMLNode(node).to_HTML())


if __name__ == "__main__":
    unittest.main()