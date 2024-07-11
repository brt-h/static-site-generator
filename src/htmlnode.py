class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # if there are no props, return an empty string
        if self.props is None:
            return ""
        # initialize an accumulator for the formatted string
        formatted_props = ""
        # iterate over the key-value pairs in the props dictionary
        for key, value in self.props.items():
            # format the key-value pair and append it to the accumulator
            formatted_props += f' {key}="{value}"'
        # return the formatted string
        return formatted_props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (self.tag == other.tag 
                and self.value == other.value 
                and self.children == other.children
                and self.props == other.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode to_html method requires a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
       if children is None:
           raise ValueError("ParentNode requires children")
       # ParentNode doesn't take a value argument
       super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            return ValueError("ParentNode to_html method requires a tag")
        if self.children is None:
            return ValueError("ParentNode to_html method requires children")
        # accumulate html output
        html_output = ""
        # iterate through the ParentNode's children
        for child in self.children:
            # call the to_html method on each child, entering recusion when the child is not a LeafNode
            html_output += child.to_html()
        # contatenate the tags from the parent node
        return f"<{self.tag}>" + html_output + f"</{self.tag}>"



    # accumulator

    # if a leaf node, then use the leafnode.to_html method and concatenate the result
    # if its a parent node, call this recursive method and concatenate the result

    # end condition?

    # recursion
        #return f""

    #TODO RECURSIVE iterate over all the children and call `to_html` on each, 
    # concatenating the results and injecting them between the 
    # opening and closing tags of the parent 

### this:
# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# node.to_html()
### should return:
# <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>