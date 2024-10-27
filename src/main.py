
from textnode import TextNode
from htmlnode import *
import re, shutil, os

def main():
    copy_to_destination(os.getcwd()  + "/static/",os.getcwd()  +  "/public/")

def copy_to_destination(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)
    else:
        os.mkdir(dest)

    if os.listdir(src) != os.listdir(dest):
        items = os.listdir(src)
        for item in items:
            print(src + item)
            print(os.path.isfile(src + item))
            if os.path.isfile(src + item):
                shutil.copy(src + item, dest)
                print("Copying File: " + item)
            else:
                new_dest = os.mkdir(dest + item)
                print("Copying directory: " + item)
                copy_to_destination(src + item + "/", dest + item + "/")
    else:
        return

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

def text_to_children(text):
    output = []
    for i in text_to_text_nodes(text):
        output.append(textNode_to_HTMLNode(i))
    return output

def line_strip(line):
    return line.strip()

def markdown_to_blocks(markdown):
    output = markdown.split("\n\n")
    output = list(map(line_strip, output))
    return output

def block_to_block_type(block):
    type_indicator = block[0:block.find(" ")]
    if type_indicator == "#":
        return "h1"
    if type_indicator == "##":
        return "h2"
    if type_indicator == "###":
        return "h3"
    if type_indicator == "####":
        return "h4"
    if type_indicator == "#####":
        return "h5"
    if type_indicator == "######":
        return "h6"
    if type_indicator == "*" or type_indicator == "-":
        return "ul"
    if type_indicator == ">":
        return "blockquote"
    if type_indicator[0:3] == "```":
        return "code"    
    if type_indicator == "1.":
        return "ol"
    return "p"

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type[0] == "h":
        return ParentNode(block_type, text_to_children(block[block.find(" ") + 1:]))
    if block_type == "p":
        return ParentNode(block_type, text_to_children(block))
    if block_type == "code":
        return ParentNode(block_type, text_to_children(block[block.find("```") + 3: block.rfind("```")]))
    if block_type == "blockquote":
        return ParentNode(block_type, text_to_children(block[block.find(" ") + 1:]))
    if block_type == "ul":
        return ul_to_HTMLnode(block)
    if block_type == "ol":
        return ol_to_HTMLnode(block)

def ul_to_HTMLnode(block):
    items = block.split("*")
    children = []
    for item in items:
        if item:
            children.append(LeafNode("li", item.strip()))
    return ParentNode("ul", children)

def ol_to_HTMLnode(block):
    items = block.split("\n")
    children = []
    for item in items:
        if item:
            children.append(LeafNode("li", item.strip()[item.find(" ") + 1:]))
    return ParentNode("ol", children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    output_nodes = []
    for block in blocks:
        output_nodes.append(block_to_html_node(block))
    return output_nodes
    

if __name__=="__main__":
    main()