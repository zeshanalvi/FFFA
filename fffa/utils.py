import numpy as np
import math


def weight(WM, A):
    """Calculate total cost of path A using weight matrix WM."""
    w = WM[A[0]][A[-1]]
    for i in range(1, len(A)):
        w += WM[A[i - 1]][A[i]]
    return w

def Generate(M, N):
    """Generate a random population of M paths with N nodes."""
    data = np.zeros((M, N), int)
    for i in range(M):
        data[i] = np.random.permutation(N)
    return data


def read_tsp(file):
    # Open input file
    infile = open(file, 'r')
    # Read instance header
    
    #print(infile.readline().strip().split())
    
    Name = infile.readline().strip().split()[-1] # NAME
    FileType = infile.readline().strip().split()[-1] # TYPE
    Comment = infile.readline().strip().split()[-1] # COMMENT
    Dimension = infile.readline().strip().split()[-1] # DIMENSION
    
    if(Dimension=='EXPLICIT'):
        EdgeWeightType=Dimension
        Dimension=Comment
    elif(not Dimension.isdigit()):        
        EdgeWeightType=Dimension
        Dimension=Comment
    else:
        EdgeWeightType = infile.readline().strip().split()[-1] # EDGE_WEIGHT_TYPE,EXPLICIT
    EdgeWeightFormat = infile.readline().strip().split()[-1]#EDGE_WEIGHT_FORMAT: LOWER_DIAG_ROW
    if(EdgeWeightFormat=='NO_DISPLAY'):
        EdgeWeightFormat=EdgeWeightType
        EdgeWeightType=Dimension
        Dimension=Comment
    infile.readline()
    #print(Name,FileType,Comment,Dimension,EdgeWeightType,EdgeWeightFormat)
    # Read node list
    if("COORD" in EdgeWeightFormat):
        cities=read_cities(infile,int(Dimension))
        WM=calculate_distance_matrix(cities)
        return WM
    nodelist = []
    N = int(Dimension)
    while(True):
        line=infile.readline()
        if(len(line)==0):
            break
        ary=line.split()
        numeric=True
        for i in ary:
            if (not i.isnumeric()):
                numeric=False
                break
        if(numeric):
            ary=[int(i) for i in ary]
            nodelist.extend(ary)
    # Close input file
    infile.close()
    #print(len(nodelist),N)
    #print(EdgeWeightFormat)
    #print(nodelist[:30],len(nodelist[:30]))
    if(EdgeWeightFormat=="FULL_MATRIX"):
        WM=np.zeros((N,N),int)
        k=0
        for i in range(0,N):
            for j in range(0,N):
                #print('i,j,k',i,j,k)
                WM[i][j]=nodelist[k]
                k+=1
    elif("UPPER" in EdgeWeightFormat):#LOWER_DIAG_ROW
        WM=np.zeros((N,N),int)
        k=0
        for i in range(0,N):
            for j in range(i+1,N):
                #print('i,j,k',i,j,k,len(nodelist),N)
                WM[i][j]=nodelist[k]
                WM[j][i]=nodelist[k]
                k+=1
    elif("LOWER" in EdgeWeightFormat):#LOWER_DIAG_ROW
        WM=np.zeros((N,N),int)
        k=0
        for i in range(0,N):
            for j in range(0,i+1):
                #print('i,j,k',i,j,k,len(nodelist),N)
                WM[i][j]=nodelist[k]
                WM[j][i]=nodelist[k]
                k+=1
    
    return WM

def read_cities(infile,Dimension):
    cities = {}
    for i in range(Dimension):
    #while(True):
        line=infile.readline()
        #print(line)
        if(len(line)==0 or line=='EOF'):
            break
        line=line.strip().split()
        if len(line) != 3:
            break
            raise ValueError(f"Invalid line format in file: {line}")
        city_name, x, y = line
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            break
            raise ValueError(f"Invalid coordinates for city '{city_name}': {line}")
        cities[city_name] = (x, y)
    return cities

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = [[0 for _ in range(num_cities)] for _ in range(num_cities)]  # Initialize with zeros

    for i, city_i in enumerate(cities):
        x_i, y_i = cities[city_i]
        for j, city_j in enumerate(cities):
            if i != j:  # Avoid calculating distance to itself
                x_j, y_j = cities[city_j]
                distance_matrix[i][j] = distance_matrix[j][i] = math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2)  # Euclidean distance

    return distance_matrix
