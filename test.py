import networkx as nx
import matplotlib.pyplot as plt
def dot_product(v1, v2):
    # Flatten the vectors
    flat_v1 = [item for sublist in v1 for item in sublist]
    flat_v2 = [item for sublist in v2 for item in sublist]
    
    # Pad vectors to make them of equal length
    while len(flat_v1) < len(flat_v2):
        flat_v1.append(0)
    while len(flat_v2) < len(flat_v1):
        flat_v2.append(0)
    
    return sum(x*y for x, y in zip(flat_v1, flat_v2))

# def dot_product(v1, v2):
#     # Pad vectors to make them of equal length
#     while len(v1) < len(v2):
#         v1.append([0, 0, 0, 0, 0])
#     while len(v2) < len(v1):
#         v2.append([0, 0, 0, 0, 0])
    
#     return sum(x*y for x, y in zip(v1, v2))

languages = ['French', 'German', 'Hindi', 'Russian', 'Arabic', 'Indonesian', 'Tagalog', 'Japanese', 'Korean', 'Swahili', 'Portuguese', 'Urdu']
vectors = {
    'French': [[[0,0,0,0,1], [0,1,0,0,0], [0,0,1,0,0], [1,0,0,0,0]], [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]],
    'German': [[[0,0,0,0,1], [0,1,0,0,0], [0,0,1,0,0], [1,0,0,0,0]], [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]],
    'Hindi': [[[0,0,1,0,0], [1,0,0,0,0], [0,0,0,0,1], [0,1,0,0,0]], [[0,0,1,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0]]],
    'Russian': [[[1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0], [0,0,1,0,0]], [[1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,1,0,0,0]]],
    'Arabic': [[[0,0,1,0,0], [1,0,0,0,0], [0,1,0,0,0], [0,0,0,0,1]], [[1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0], [0,0,1,0,0]]],
    'Indonesian': [[[0,0,0,0,1], [1,0,0,0,0], [0,0,1,0,0]], [[1,0,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]],
    'Tagalog': [[[0,0,0,0,1], [1,0,0,0,0], [0,0,1,0,0]], [[1,0,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,0,0,1,0]]],
    'Japanese': [[[0,0,1,0,0], [1,0,0,0,0], [0,0,0,0,1], [0,1,0,0,0]], [[0,0,1,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0]]],
    'Korean': [[[0,0,1,0,0], [1,0,0,0,0], [0,0,0,0,1], [0,1,0,0,0]], [[0,0,1,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0]]],
    'Swahili': [[[1,0,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,0,0,0,1]], [[1,0,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,0,0,1,0]]],
    'Portuguese': [[[0,0,0,0,1], [0,1,0,0,0], [1,0,0,0,0], [0,0,1,0,0]], [[0,0,1,0,0], [1,0,0,0,0], [0,1,0,0,0], [0,0,0,1,0]]],
    'Urdu': [[[0,0,1,0,0], [1,0,0,0,0], [0,0,0,0,1], [0,1,0,0,0]], [[0,0,1,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,1,0,0,0]]]
}

similarity_matrix = {}
for lang1 in languages:
    similarity_matrix[lang1] = {}
    for lang2 in languages:
        score = (dot_product(vectors[lang1][0], vectors[lang2][0]) + dot_product(vectors[lang1][1], vectors[lang2][1])) / 2
        similarity_matrix[lang1][lang2] = score

# Format as markdown
markdown = "| Language | " + " | ".join(languages) + " |\n"
markdown += "|----------|" + "----|" * len(languages) + "\n"
for lang1 in languages:
    row = "| " + lang1 + " | "
    for lang2 in languages:
        row += str(similarity_matrix[lang1][lang2]) + " | "
    markdown += row + "\n"

print(markdown)


def plot_graph(matrix, threshold=0.5):
    # Create a new graph
    G = nx.Graph()
    
    # Add nodes
    for lang in matrix:
        G.add_node(lang)
    
    # Add weighted edges
    for lang1 in matrix:
        for lang2 in matrix:
            weight = matrix[lang1][lang2]
            if weight >= threshold and lang1 != lang2:  # Add edges only if weight exceeds a certain threshold and not a self-loop
                G.add_edge(lang1, lang2, weight=weight)
    
    # Draw the graph
    pos = nx.spring_layout(G)  # use spring layout
    edges = G.edges(data=True)
    
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, edge_color=[item[2]['weight'] for item in edges],
            width=[item[2]['weight'] for item in edges], edge_cmap=plt.cm.Blues)
    
    plt.show()

# Plot the graph with a weight threshold of, say, 4 (you can adjust this as needed)
plot_graph(similarity_matrix, threshold=4)
