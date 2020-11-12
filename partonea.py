import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import jaccard_score
from scipy.stats import ttest_1samp
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import mutual_info_score
from prettytable import PrettyTable
from functions import *

#Open CVS files to analyze with pandas
colnames = ['col1', 'col2']
p1a = pd.read_csv('p1a.csv', names=colnames)

#obtain data in list form and ndarray
columnONEconstant = []
columnTWOconstant = []
columnONE = p1a['col1'].to_numpy()
columnTWO = p1a['col2'].to_numpy()
columnONEl = p1a['col1'].tolist()
columnTWOl = p1a['col2'].tolist()

for i in range(len(columnONE)):
    columnONEconstant.append(columnONE[i])

for i in range(len(columnTWO)):
    columnTWOconstant.append(columnTWO[i])

print("Welcome to Homework 4, Part One A")

print("\nEvaluating:")
print("Null Hypothesis: No association between the traits.")
print("Alternative Hypothesis: There is association between the traits.")



#permutation tes##################
print("\n\nMutual Information:")
print(mutual_info_classif(columnONE.reshape(-1,1), columnTWO, discrete_features = True))
print(mutual_info_score(columnONE,columnTWO))

print("\nJaccard Similarity:")
intersection = len(list(set(columnONEconstant).intersection(columnTWOconstant)))
union = (len(columnONEconstant) + len(columnTWOconstant)) - intersection
jaccard = float(intersection) / union
print("Similarity: ")
print(jaccard)
print("Pre permutations score: ")
print(jaccard_score(columnONEconstant, columnTWOconstant))


#print("\nPermutations test") #for Mutual information and Jaccard score
repeats = 100 #we are having 100 permutations
MIperms=[] #saving results for Mutual info
Jacperms=[] #saving info for Jaccard similarity
for i in range(repeats):
    # let's shuffle them!
    random.shuffle(columnONEl)
    #random.shuffle(columnTWOl)
    newMI=mutual_info_score(columnONEl, columnTWOl)
    MIperms.append(newMI)
    newJac = getJacc(columnONE, columnTWO)
    Jacperms.append(newJac)

#sns.set_style('darkgrid')
#sns.displot(Jacperms)
#plt.show()

#permutation test ends ###################

#Calculate P-values for MI
print("\nP-value from permutations for Mutual information:")
pvaluem = getpval(MIperms, mutual_info_score(columnONEconstant,columnTWOconstant))
print(pvaluem)

jackperm = []
for i in range(len(Jacperms)): #this is for the x side of the permutations
    jackperm.append(i)

#show Jaccard plot for permutations
#sns.set_style('darkgrid')
#sns.displot(Jacperms) uncomment this one for histogram
Jacperms.sort()
plt.scatter(Jacperms, jackperm)
#plt.show()



#Calculate P-value for Jaccard
print("\nP-value from permutations for Jaccard:")
pvalue = getpval(Jacperms, jaccard_score(columnONEconstant, columnTWOconstant))
print(pvalue)

#show Jaccard plot for permutations
#sns.set_style('darkgrid')
#sns.displot(Jacperms)
#plt.show()


print("\nChi Square:")
print("Observed Table")
#Get the data into observations ****
#create buckets
YY = 0 #Contain both traits
YN = 0 #contain first trait only
NY = 0 #contain second trait only
NN = 0 #contain no traits
total = 199
i = 0
#Getting the counts for observations table
while (i<total):
    if columnONEconstant[i] == 0:
        if columnONEconstant[i] == columnTWOconstant[i]:
            NN += 1  #No traits on specimen
        else:
            NY += 1 #second trait present
    elif columnONEconstant[i] == 1:
        if columnONEconstant[i] == columnTWOconstant[i]:
            YY += 1 #both traits present
        else:
            YN += 1 #only first trait present
    i += 1
#***

#complete the pretty table
#This is the actual table
observations = PrettyTable()
observations.field_names=["","Trait1 Yes","Trait1 No","Totals"]
observations.add_row(["Trait2 Yes", YY, NY, YY+NY])
observations.add_row(["Trait2 No", YN, NN, YN+NN])
observations.add_row(["Totals", YY+YN, NY+NN, 199])
print(observations)

#caluclate the expected table using:
print("\n\nExpected Table")
# ((total column)*(total row))/totals
totale=199
YYExpect = ((YY+YN)*(YY+NY))/totale
YNExpect = ((YY+YN)*(YN+NN))/totale
NYExpect = ((YY+NY)*(NY+NN))/totale
NNExpect = ((YN+NN)*(NY+NN))/totale

expectations = PrettyTable()
expectations.field_names=["","Trait1 Yes","Trait1 No"]
expectations.add_row(["Trait2 Yes", YYExpect, NYExpect])
expectations.add_row(["Trait2 No", YNExpect, NNExpect])
print(expectations)

#calculate chi square(observed - expected)/expected
x2= (((YY-YYExpect)**2)/YYExpect) + (((YN-YNExpect)**2)/YNExpect) + (((NY-NYExpect)**2)/NYExpect) + (((NN-NNExpect)**2)/NNExpect)
print("Chi Square value is: "+ str(x2))
print("The p-value is: "+ str(1-stats.chi2.cdf(x2, 1)))


