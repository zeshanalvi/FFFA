# FFFA: Foxes and Fireflies Foraging Algorithm

FFFA is a **nature-inspired single-solution optimization algorithm** that mimics the foraging behavior of foxes and fireflies.  
It is designed for solving **path optimization problems** (e.g., shortest path, graph-based problems) where a weight matrix is provided as input.  

---

## Installation

You can install FFFA directly from PyPI (after publishing):

```bash
pip install fffa
```
## Usage Example

from fffa import fff

# Example weighted adjacency matrix

```python
weight_matrix = [
    [0, 2, 9, 0],
    [1, 0, 6, 4],
    [0, 7, 0, 8],
    [6, 3, 0, 0]
]

best_path, best_cost = fff(weight_matrix)

print("Best Path:", best_path)
print("Best Cost:", best_cost)
```

## Features

Nature-inspired single-solution optimization algorithm

Works with any weighted adjacency matrix

Simple API with minimal dependencies

Lightweight and easy to integrate

## Project Structure

```bash
FFFA/
│── fffa/                 # Main package
│   ├── __init__.py
│   ├── fff.py            # Main algorithm
│   ├── update.py         # Helper functions
│── tests/                # Test cases
│   └── test.py
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── setup.py              # Packaging setup
│── LICENSE

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
