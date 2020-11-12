from functions import *

#Open CVS files to analyze with pandas
columnsnames = ['col1', 'col2']
p2a = pd.read_csv('p2a.csv', names=columnsnames)

column1 = [] #this stays constant
column2 = [] #this stays constant
columnONEb = p2a['col1'].to_numpy()
columnTWOb = p2a['col2'].to_numpy()

for i in range(len(columnONEb)):
    column1.append(columnONEb[i])
    column2.append(columnTWOb[i])

print("Null Hypothesis: No association between the traits.")
print("Alternative Hypothesis: There is association between the traits.")

print('\n\n Pearson\'s Correlation: ')
#https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04    ***Resources
#pearsons = p2a.corr(method='pearson')
#pearsonsfunc(pearsons)
#pearsons_tscore(0.38, 2400)

print('P-value is: ')
#Calculate p-value from correlation results
#print(0.32/2400)

##################################################################### PART 2B ######################################
#Open CVS files to analyze with pandas
columnsnamesb = ['col1', 'col2']
p2b = pd.read_csv('p2b.csv', names=columnsnames)

#pearsonsb = p2b.corr(method='pearson')
#pearsonsfunc(pearsonsb)
#pearsons_tscore(0.93, 110)


#scatter plots
#sns.set_theme(style="darkgrid")
#sns.relplot(x="col1", y="col2", data=p2a)
#plt.title("P2A Dataset")
#plt.xlabel('Column 1')
#plt.ylabel('Column 2')
#plt.show()




################################################# PART 2C ########################################################

columnsnamesc = ['col1', 'col2']
p2c = pd.read_csv('p2c.csv', names=columnsnames)
pearsonsc = p2c.corr(method='pearson')
pearsonsfunc(pearsonsc)
pearsons_tscore(0.041, 2100)
#scatter plots
#sns.set_theme(style="darkgrid")
#sns.relplot(x="col1", y="col2", data=p2c)
#plt.title("P2C Dataset")
#plt.xlabel('Column 1')
#plt.ylabel('Column 2')
#plt.show()

