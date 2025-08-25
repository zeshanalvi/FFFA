import numpy as np
import numpy as np
from .update import update_Foxes   # ✅ relative import
from .utils import weight, Generate

def fff(graph, num_foxes=150, G=500, w=0.5, c1=1, c2=1):
    """
    fff algorithm (Food Finding Foxes) for TSP-like optimization problems.

    Parameters:
    - Graph: 2D numpy array (distance matrix)
    - num_foxes: population size
    - G: number of generations
    - w, c1, c2: velocity parameters

    Returns:
    - best_cost: cost of the best found path
    - best_path: sequence of nodes (permutation)
    """
    N = len(graph)
    
    # Random initial population and velocity
    data = Generate(num_foxes, N)
    V = np.zeros((num_foxes, N))
    
    # For memory of each generation
    history = np.zeros((G, num_foxes, N), dtype=int)
    history_acc = np.zeros((G, num_foxes), dtype=float)
    
    h_best = 0
    leader_num = 0
    best_path = data[leader_num]
    best_cost = weight(graph, best_path)
    
    for g in range(G):
        Ws = [weight(graph, data[i]) for i in range(num_foxes)]
        history[g] = data
        history_acc[g] = Ws
        
        for i in range(num_foxes):
            if Ws[i] < best_cost:
                best_path = data[i]
                best_cost = Ws[i]
                leader_num = i
            if Ws[i] < history_acc[h_best, i]:
                h_best = g
        
        data = update_Foxes(
            data, num_foxes, N, V, g, G, best_path, leader_num,
            history, h_best, w, c1, c2
        )
    
    return float(best_cost), best_path
