
from textnode import TextNode
from htmlnode import *

def main():
    tNode = TextNode("text node", "text type", "u/r/l")
    print(tNode)

def textNode_to_HTMLNode(tNode):
    if tNode.text_type == "text":
        return LeafNode(None, tNode.text)
    if tNode.text_type == "bold":
        return LeafNode("b", tNode.text)
    if tNode.text_type == "italic":
        return LeafNode("i", tNode.text)
    if tNode.text_type == "code":
        return LeafNode("code", tNode.text)
    if tNode.text_type == "link":
        return LeafNode("a", tNode.text, {"href":tNode.url})
    if tNode.text_type == "image":
        return LeafNode("img", "", {"src":tNode.url, "alt":tNode.text})
    return Exception


if __name__=="__main__":
    main()