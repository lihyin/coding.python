# Input N x L feature matrix, N data, each data feature in L dimensions, classify into K classes.
import math


# a, b is a N X L matrix
def calDistance(a, b):
    return


def findNearestPoint(dist, k):
    return


def adjustNewCenter(cluster):
    return


def isCentersNotChange():
    return


def knn(data, K):
    dist = []
    # 1. calculate the distance
    for i in range(len(data)):
        for j in range(len(data) - 1):
            dist[i][j] = calDistance(data[i], data[j])

    # 2. find the nearest neibours
    kCenters = {}
    # 2.1 randomly assign K centers
    i = 0
    while i < K:
        r = math.rand(len(data))
        if r not in kCenters:
            kCenters[i] = r
            i += 1

    # 2.2
    cluster = []
    while isCentersNotChange():
        for k in range(len(K)):
            for j in range(len(data)):
                # find the len(data) / K nearest data points
                cluster[k] = findNearestPoint(dist[k], len(data) / K)

                # find the new center
                adjustNewCenter(cluster[k])