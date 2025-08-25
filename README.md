# FFFA: Food Finding Foxes Algorithm

<p align="center">
  <a href="https://pypi.org/project/fffa/"><img src="https://img.shields.io/pypi/v/fffa.svg" alt="PyPI Version"></a>
  <a href="https://github.com/zeshanalvi/fffa/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/fffa.svg" alt="License"></a>
  <a href="https://pepy.tech/project/fffa/"><img src="https://static.pepy.tech/badge/fffa" alt="Downloads"></a>
  <a href="https://pypi.org/project/fffa/"><img src="https://img.shields.io/pypi/pyversions/fffa.svg" alt="Python Versions"></a>
  <a href="https://github.com/zeshanalvi/fffa/stargazers"><img src="https://img.shields.io/github/stars/zeshanalvi/fffa?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/zeshanalvi/fffa/commits/main"><img src="https://img.shields.io/github/last-commit/zeshanalvi/fffa.svg" alt="Last Commit"></a>
  <a href="https://github.com/zeshanalvi/fffa/issues"><img src="https://img.shields.io/github/issues/zeshanalvi/fffa.svg" alt="Open Issues"></a>
</p>

FFFA is a **nature-inspired single-solution optimization algorithm** that mimics the foraging behavior of foxes.  
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
