from pyvis.network import Network
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

import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

# Create a Dash application
app = dash.Dash(__name__)

# Preprocess data for Cytoscape format
nodes = [{'data': {'id': lang, 'label': lang}} for lang in similarity_matrix]
edges = [{'data': {'source': lang1, 'target': lang2, 'weight': similarity_matrix[lang1][lang2]}} for lang1 in similarity_matrix for lang2 in similarity_matrix if lang1 != lang2]
elements = nodes + edges

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#0074D9',
            'label': 'data(label)',
            'font-size': '12px',
            'text-valign': 'center',
            'color': 'white',
            'text-outline-color': '#0074D9',
            'text-outline-width': '2px'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'width': 'mapData(weight, 0, 100, 1, 5)'
        }
    }
]

app.layout = html.Div([
    cyto.Cytoscape(
        id='language-graph',
        elements=elements,
        stylesheet=default_stylesheet,
        layout={'name': 'circle'},
        style={'height': '600px', 'width': '100%'}
    )
])

@app.callback(
    Output('language-graph', 'stylesheet'),
    Input('language-graph', 'tapNodeData'),
)
def update_styles(tapNodeData):
    if not tapNodeData:
        return default_stylesheet

    new_styles = [
        {
            'selector': f'node[id = "{tapNodeData["id"]}"]',
            'style': {
                'background-color': '#FF4136'
            }
        },
        {
            'selector': f'[source = "{tapNodeData["id"]}"]',
            'style': {
                'line-color': '#FF4136'
            }
        },
        {
            'selector': f'[target = "{tapNodeData["id"]}"]',
            'style': {
                'line-color': '#FF4136'
            }
        }
    ]
    return default_stylesheet + new_styles

if __name__ == '__main__':
    app.run_server(debug=True)

