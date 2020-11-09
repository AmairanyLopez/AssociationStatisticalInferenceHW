import pandas as pd
import numpy as np
import scipy.stats as stats
import random
from sklearn.metrics import jaccard_score


def getJacc(columnONEx, columnTWOx):
    random.shuffle(columnONEx)
    jaccard = jaccard_score(columnONEx, columnTWOx)
    return jaccard

def getpval(arrayish, basenumber):
    count=0
    for i in range(len(arrayish)):
        if arrayish[i] > basenumber:
            count += 1

    return ((count + 1 ) / (len(arrayish) + 1 ))


