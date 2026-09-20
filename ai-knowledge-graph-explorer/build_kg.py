import matplotlib.pyplot as plt
import networkx as nx


def create_knowledge_graph():
    # Initialize a directed graph
    kg = nx.DiGraph()

    # Define semantic triples: (Subject, Object, Attribute dict for relationship)
    triples = [
        ("Artificial Intelligence", "Machine Learning", "subfield_of"),
        ("Artificial Intelligence", "Natural Language Processing", "subfield_of"),
        ("Machine Learning", "Deep Learning", "subfield_of"),
        ("Deep Learning", "Neural Networks", "utilizes"),
        ("Machine Learning", "Python", "commonly_implemented_in"),
        ("Deep Learning", "PyTorch", "supported_by"),
        ("PyTorch", "Python", "is_library_of"),
        ("Natural Language Processing", "Large Language Models", "includes"),
        ("Large Language Models", "Transformers", "based_on"),
    ]

    # Add edges with relationship attributes
    for subject, obj, relation in triples:
        kg.add_edge(subject, obj, relationship=relation)

    return kg


def visualize_knowledge_graph(kg):
    plt.figure(figsize=(12, 8))

    # Calculate layout positioning for nodes
    pos = nx.spring_layout(kg, k=1.5, seed=42)

    # Draw nodes and labels
    nx.draw_networkx_nodes(kg, pos, node_size=2500, node_color="skyblue")
    nx.draw_networkx_labels(kg, pos, font_size=9, font_weight="bold")

    # Draw edges with arrows
    nx.draw_networkx_edges(
        kg,
        pos,
        edgelist=kg.edges(),
        edge_color="gray",
        arrowsize=20,
        connectionstyle="arc3,rad=0.1",
    )

    # Draw edge relationship labels
    edge_labels = nx.get_edge_attributes(kg, "relationship")
    nx.draw_networkx_edge_labels(kg, pos, edge_labels=edge_labels, font_size=8)

    plt.title("AI Concepts Assignment Knowledge Graph", fontsize=14)
    plt.axis("off")
    plt.tight_layout()

    # Save the file locally so it can be committed to GitHub
    output_image = "knowledge_graph.png"
    plt.savefig(output_image, format="PNG", dpi=300)
    plt.show()
    print(f"[Success] Knowledge Graph generated and saved as '{output_image}'")


if __name__ == "__main__":
    graph = create_knowledge_graph()
    visualize_knowledge_graph(graph)