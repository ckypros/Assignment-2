from math import sqrt
from statistics import mode

knn = 9
dataset = [[0,5,'no'], [0,3,'no'], [1,4,'no'], [2,4,'yes'], [2,1,'no'], [3,3,'yes'], [3,2,'yes'], [4,4,'yes'], [4,3,'yes'], [4,1,'no']]
correct = 0
incorrect = 0
# For each data, calculate the euclidean distances to other datas
for i in range(len(dataset)):
    distances = []

    for j in range(len(dataset)):
        # Label coordinates of data being evaluated
        x1 = dataset[i][0]
        y1 = dataset[i][1]
        
        # Don't perform calcation against itself
        if dataset[j] != dataset[i]:
            # Label coordinates of other data to being measured against
            x2 = dataset[j][0]
            y2 = dataset[j][1]

            # Calculate euclidean distance to other data and append to list 
            distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
            distances.append([j, distance])  # j is the index of the data in dataset[]

    # Sort the distances lowest to highest distance
    sorted_distances = sorted(distances, key=lambda x: (x[1], -x[1]))
    
    # Get closest neighbor for evaluation
    nearest = []
    knn_results = []
    for n in range(knn):
        nearest.append(sorted_distances[n])
        knn_results.append(dataset[sorted_distances[n][0]][2]) 

    knn_result = mode(knn_results)
    result = dataset[i][2] == knn_result
    print(f"data {i} neighbor{'s' if knn != 1 else ''} [data #, distance]: {nearest}")
    print(f"data {i}: {dataset[i][2]} \tmode of {knn}nn: {knn_result} \tisCorrect?: {result}\n")
    # Tabulate correct and incorrect predictions using KNN
    if result:
        correct += 1
    else: 
        incorrect += 1
error_rate = incorrect / (correct + incorrect)
print(f"correct: {correct}, incorrect: {incorrect}")
print(f"{incorrect}/({correct} + {incorrect}) = {error_rate}")