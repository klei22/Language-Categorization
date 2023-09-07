from pyvis.network import Network
import numpy as np

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

languages = ['French', 'Spanish', 'German', 'Hindi', 'Russian', 'Arabic', 'Indonesian', 'Tagalog', 'Japanese', 'Korean', 'Swahili', 'Portuguese', 'Urdu']
vectors = {
    'French': [[[0,0,0,0,1], [0,1,0,0,0], [0,0,1,0,0], [1,0,0,0,0]], [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]],
    'Spanish': [[[0,0,0,0,1], [0,1,0,0,0], [0,0,1,0,0], [1,0,0,0,0]], [[0,0,1,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]],
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


def _circular_positions(labels, radius=1000):
    """
    Generate circular positions for given labels.

    Parameters:
    - labels: List of labels
    - radius: Radius of the circle

    Returns:
    - Dictionary with labels as keys and positions as values
    """
    theta = 2 * 3.141592653589793 / len(labels)
    positions = {}
    for i, label in enumerate(labels):
        x = radius * np.cos(i * theta)
        y = radius * np.sin(i * theta)
        positions[label] = (x, y)
    return positions

def circular_plot(matrix):
    nt = Network(notebook=True, width="100%", height="750px", bgcolor="#222222", font_color="green", heading="")

    # Use remote resources
    nt.use_CDN = True

    # Add nodes
    for lang in matrix:
        nt.add_node(lang)

    # Get max and min similarities for normalization
    all_weights = [matrix[lang1][lang2] for lang1 in matrix for lang2 in matrix if lang1 != lang2]
    max_weight = max(all_weights)
    min_weight = min(all_weights)

    threshold = 1  # Only show edges with similarity above 70, for example.

    # Add edges with normalized transparency based on similarity
    for lang1 in matrix:

        for lang2 in matrix:
            weight = matrix[lang1][lang2]
            normalized_weight = (weight - min_weight) / (max_weight - min_weight)
            alpha = (0.95 * normalized_weight + 0.05)  # This will normalize between 5% to 100%
            color = f"rgba(255, 120, 120, {alpha})"
            if lang1 != lang2 and weight > threshold:
                nt.add_edge(lang1, lang2, value=weight, color=color)

    # Use the circular layout for nodes
    positions = _circular_positions(list(matrix.keys()))

    # Update node positions
    for node in nt.nodes:
        label = node['label']
        position = positions.get(label, (0, 0))
        node['x'] = position[0]
        node['y'] = position[1]

    # Display the plot
    nt.show("temp.html")



# Create the circular plot
circular_plot(similarity_matrix)

def dynamic_plot(matrix):
    nt = Network(notebook=True, width="100%", height="1500px", bgcolor="#222222", font_color="blue", heading="")

    # Use remote resources
    nt.use_CDN = True

    # Add nodes
    for lang in matrix:
        nt.add_node(lang)

    # Add edges
    for lang1 in matrix:
        for lang2 in matrix:
            weight = matrix[lang1][lang2]
            if lang1 != lang2:
                nt.add_edge(lang1, lang2, value=weight)

    # Display the dynamic plot
    nt.show("temp.html")

# Create the dynamic plot
# dynamic_plot(similarity_matrix)

