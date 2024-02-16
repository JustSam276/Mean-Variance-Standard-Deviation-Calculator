import numpy as np


def calculate(list):

    #reshaping the list into a matrix
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3,3)

    #mean
    mean = [(np.mean(matrix, axis=0)).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]

    #variance
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]

    #standard deviation
    std = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]

    #max
    highest = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]

    #min
    lowest = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]

    #sum
    total = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]

    calculations = {
        "mean" : mean,
        "variance" : variance,
        "standard deviation" : std,
        "max" : highest,
        "min" : lowest,
        "sum" : total
    }
    

    return calculations


