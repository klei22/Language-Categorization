# Language Similarity Analysis

This Python script calculates the similarity between different languages based on their vector representations. It uses the pyvis library to visualize the similarity matrix in a circular plot.

Language clusters are interesting when looking at LLM training.

One could for example:

1. try to train with all data for a specific language group, which should
   reinforce others and more quickly converge due to similar parts-of-speech
   ordering.
2. One could try to train from and test for different langauge groups to test
   any universality of ones new model.

## Usage

1. Install the required dependencies:
   - pyvis: `pip install pyvis`
   - numpy: `pip install numpy`

2. Run the script:
   ```
   python language_similarity.py
   ```

1. The script will generate a similarity matrix and display it as a circular plot in a web browser.
## Opening on Linux

If the website does not open automatically simply open manually:

```sh
xdg-open temp.html
```

## Example Output

The script will generate a markdown table showing the similarity scores between languages. Here is an example output:

| Language   | French | Spanish | German | Hindi | Russian | Arabic | Indonesian | Tagalog | Japanese | Korean | Swahili | Portuguese | Urdu |
|------------|--------|---------|--------|-------|---------|--------|-------------|---------|----------|--------|----------|-------------|------|
| French     | 1.0    | 0.75    | 1.0    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| Spanish    | 0.75   | 1.0     | 0.75   | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| German     | 1.0    | 0.75    | 1.0    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| Hindi      | 0.5    | 0.5     | 0.5    | 1.0   | 0.75    | 0.75   | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| Russian    | 0.5    | 0.5     | 0.5    | 0.75  | 1.0     | 0.75   | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| Arabic     | 0.5    | 0.5     | 0.5    | 0.75  | 0.75    | 1.0    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.5         | 0.5  |
| Indonesian | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 1.0         | 0.75    | 0.75     | 0.5    | 0.5      | 0.5         | 0.5  |
| Tagalog    | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.75        | 1.0     | 0.75     | 0.5    | 0.5      | 0.5         | 0.5  |
| Japanese   | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.75        | 0.75    | 1.0      | 0.5    | 0.5      | 0.5         | 0.5  |
| Korean     | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 1.0    | 0.75     | 0.5         | 0.5  |
| Swahili    | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.75   | 1.0      | 0.5         | 0.5  |
| Portuguese | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 1.0         | 0.75 |
| Urdu       | 0.5    | 0.5     | 0.5    | 0.5   | 0.5     | 0.5    | 0.5         | 0.5     | 0.5      | 0.5    | 0.5      | 0.75        | 1.0  |

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

