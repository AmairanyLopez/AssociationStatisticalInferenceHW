import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_1samp
import seaborn as sns
from sklearn.feature_selection import mutual_info_classif
import random
from sklearn.metrics import jaccard_score
import matplotlib.pyplot as plt
from sklearn.metrics import mutual_info_score
from prettytable import PrettyTable
import math

def getJacc(columnONEx, columnTWOx):
    #random.shuffle(columnONEx)
    jaccard = jaccard_score(columnONEx, columnTWOx)
    return jaccard


def getpval(arrayish, basenumber):
    count=0
    for i in range(len(arrayish)):
        if arrayish[i] > basenumber:
            count += 1

    return ((count + 1 ) / (len(arrayish) + 1 ))


def chis(column1, column2):
    # create buckets
    YY = 0  # Contain both traits
    YN = 0  # contain first trait only
    NY = 0  # contain second trait only
    NN = 0  # contain no traits
    total = 199
    i = 0
    # Getting the counts for observations table
    while (i < total):
        if column1[i] == 0:
            if column1[i] == column2[i]:
                NN += 1  # No traits on specimen
            else:
                NY += 1  # second trait present
        elif column1[i] == 1:
            if column1[i] == column2[i]:
                YY += 1  # both traits present
            else:
                YN += 1  # only first trait present
        i += 1
    totale = 199
    YYExpect = ((YY + YN) * (YY + NY)) / totale
    YNExpect = ((YY + YN) * (YN + NN)) / totale
    NYExpect = ((YY + NY) * (NY + NN)) / totale
    NNExpect = ((YN + NN) * (NY + NN)) / totale
    # calculate chi square(observed - expected)/expected
    x2 = (((YY - YYExpect) ** 2) / YYExpect) + (((YN - YNExpect) ** 2) / YNExpect) + (
                ((NY - NYExpect) ** 2) / NYExpect) + (((NN - NNExpect) ** 2) / NNExpect)
    return x2

def makeprettyplots(arraytodisplay, Name):
    x = []
    for i in range(len(arraytodisplay)):
        x.append(i)
    area = (30 * np.random.rand(len(arraytodisplay))) ** 2
    colors = np.random.rand(len(arraytodisplay))
    plt.scatter(arraytodisplay, x, s=area, c=colors, alpha=0.5)
    plt.title(Name + ' Scores')
    plt.ylabel('Columns combinations 105')
    plt.xlabel(Name + ' Scores from all combinations')
    plt.show()


def pearsonsfunc(pearsons):
    sns.heatmap(pearsons,
                xticklabels=pearsons.columns,
                yticklabels=pearsons.columns,
                cmap='Spectral_r',
                annot=True,
                linewidth=0.5)
    plt.show()

def pearsons_tscore(rcorr, nvars):  #rcorr = pearsons correlation  nvars = how many items/rows
    result = (rcorr*(math.sqrt(nvars-2)))/math.sqrt(1-((rcorr)**2))
    print(result)