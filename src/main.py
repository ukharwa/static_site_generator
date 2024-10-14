
from textnode import TextNode
from htmlnode import *
import re

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    escaped_delimiter = re.escape(delimiter)
    pattern = rf'(?:{escaped_delimiter})(.*?)(?:{escaped_delimiter})'
    
    output = []
    for node in old_nodes:
        if node.text_type == "text":
            parts = re.split(pattern, node.text)
            
            for i, text in enumerate(parts):
                if i % 2 == 0:
                    output.append(TextNode(text, "text"))
                else:
                    output.append(TextNode(text, text_type))
        else:
            output.append(node)
    
    return output

def extract_markdown_images(text):
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r'[^!]\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    pattern = rf'!\[.*?\]\(.*?\)'

    output = []
    for node in old_nodes:
        if node.text_type == "text":
            text = node.text
            matches = re.finditer(pattern, text)
            
            last_end = 0
            for match in matches:
                start, end = match.span() 
                
                if last_end < start:
                    output.append(TextNode(text[last_end:start], "text"))

                image = extract_markdown_images(match.group())
                output.append(TextNode(image[0][0], "image", image[0][1]))

                last_end = end
            
            if last_end < len(text):
                output.append(TextNode(text[last_end:], "text"))
        else:
            output.append(node)

    return output       

def split_nodes_link(old_nodes):
    pattern = rf'[^!]\[.*?\]\(.*?\)'

    output = []
    for node in old_nodes:
        if node.text_type == "text":
            text = node.text
            matches = re.finditer(pattern, text)
            last_end = 0
        
            for match in matches:
                start, end = match.span() 
                
                if last_end < start:
                    output.append(TextNode(text[last_end:start], "text"))

                image = extract_markdown_links(match.group())
                output.append(TextNode(image[0][0], "link", image[0][1]))

                last_end = end

            if last_end < len(text):
                output.append(TextNode(text[last_end:], "text"))
        else:
            output.append(node)

    return output

def text_to_text_nodes(text):
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([TextNode(text, "text")])), "**", "bold"), "*", "italic"), "`", "code")

if __name__=="__main__":
    main()