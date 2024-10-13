import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_HTMLnode(self):
        node1 = HTMLNode()
        print(node1)

        node = HTMLNode("p", "hello")
        print(node)

        node = HTMLNode("p", "hello", [node1], {"href":"url"})
        print(node)

    def test_LeafNode(self):
        node = LeafNode("p", "hello")
        print(node.to_HTML())
        
        node = LeafNode("a", "This is a link", {"href":"url.com"})
        print(node.to_HTML())

        node = LeafNode(None, "Should be raw text")
        print(node.to_HTML())

        node = LeafNode("p", None)
        print(node.to_HTML())

    def test_ParentNode(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text", {"font_size":"2rem"}),
        LeafNode(None, "Normal text"),],)
        print(node.to_HTML())

        node1 = ParentNode("div", [node], {"href":"url", "src":"src"})
        print(node1.to_HTML())

if __name__ == "__main__":
    unittest.main()