from graphviz import Digraph

def generate_parse_tree():
    dot = Digraph()

    # Example for: int c = a + b;

    dot.node("assign", "=")
    dot.node("c", "c")
    dot.node("plus", "+")
    dot.node("a", "a")
    dot.node("b", "b")

    dot.edge("assign", "c")
    dot.edge("assign", "plus")
    dot.edge("plus", "a")
    dot.edge("plus", "b")

    return dot