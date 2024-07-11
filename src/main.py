from textnode import TextNode
from htmlnode import LeafNode

def main():
    print("hello world")
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node) # This will automatically call node.__repr__()

if __name__ == "__main__":
    main()