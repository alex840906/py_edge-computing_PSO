import numpy as np
#傳兩個點
def evaluate_distance(x,y):
    distance = (x - y)**2
    
    return distance

def evaluate_distance_from_centroid(centroid,iris,dim):
    distance_from_centroid = np.zeros([len(centroid),len(iris)])
    for i in range(len(centroid)):
        for j in range(len(iris)):
            tmp = 0
            for d in range(dim):
                tmp += evaluate_distance(centroid[i][d],iris[j][d])
            distance_from_centroid[i][j] = tmp**0.5
    
    return distance_from_centroid

def partition(distance_from_centroid,data_size):
    partition = np.empty([data_size])

    for i in range(data_size):
        min = 10000
        for j in range(len(distance_from_centroid)):
            if distance_from_centroid[j][i] < min:
                min = distance_from_centroid[j][i]
                partition[i] = j

    return partition

def calculate_centroid(centroid,partition,k,data_size,dim,iris):
    count = np.zeros(k)
    tmp = np.zeros([k,dim])
    for i in range(data_size):
        for d in range(dim):
            tmp[int(partition[i])][d] += iris[i][d]
        count[int(partition[i])] += 1
    
    print('count',count)
    for i in range(k):
        tmp[i]  /= count[i]
    
    for i in range(k):
        for d in range(dim):
            centroid[i][d] = tmp[i][d]

    return centroid


def evaluate_SSE(partition,centroid_of_particle,data_size,dim,iris):
    SSE = np.zeros([len(centroid_of_particle)])
    for i in range(data_size):
        tmp = 0
        for d in range(dim):
            tmp += evaluate_distance(iris[i][d] , centroid_of_particle[int(partition[i])][d])
        SSE[int(partition[i])] += tmp

    return sum(SSE)
              



            







             



