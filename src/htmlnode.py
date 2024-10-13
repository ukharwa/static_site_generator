
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_HTML(self):
        return NotImplementedError

    def props_to_HTML(self):
        output = " "
        if self.props:
            for key, value in self.props.items():
                output += key + "=\"" + value + "\"" + " " 
        return output.rstrip()
    
    def __repr__(self):
        return "tag=" + (self.tag if self.tag else "None") +"\nvalue=" + (self.value if self.value else "None") + "\nchildren=" + (str(self.children) if self.children else "[]") + "\nproperties=" + (str(self.props) if self.props else "{}")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_HTML(self):
        if self.value == None:
            return ValueError("No value?!?!?!")
        if self.tag:
            return "<" + self.tag + self.props_to_HTML() +">" + self.value + "</" + self.tag + ">"
        return self.value

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_HTML(self):
        if not self.tag:
            return ValueError("No tag?!?!?!")
        if not self.children:
            return ValueError("No children?!?!?!?")
        output = "<" + self.tag + self.props_to_HTML() + ">"
        for i in self.children:
            output += i.to_HTML()
        output += "</" + self.tag + ">"
        return output