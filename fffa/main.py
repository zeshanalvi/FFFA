from fff import FFF
from utils import read_tsp
import numpy as np

if __name__ == "__main__":
    graph = np.array([
        [0, 2, 9, 10, 7],
        [1, 0, 6, 4, 3],
        [15, 7, 0, 8, 3],
        [6, 3, 12, 0, 9],
        [8, 5, 9, 6, 0]
    ])
    files=["gr48","gr666","gr96","hk48","bayg29"]
    for f in files:
        tsp_file="data/"+f+".tsp"
        graph=read_tsp(tsp_file)
        best_cost, best_path = FFF(M=100, G=300, Graph=graph)
        print("Best Cost:", best_cost)
        print("Best Path:", best_path)

