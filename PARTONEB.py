from functions import *

#Open CVS files to analyze with pandas
columnsnames = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12', 'col13', 'col14', 'col15']
p1b = pd.read_csv('p1b.csv', names=columnsnames)


#obtain data in list form and ndarray
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column8 = []
column9 = []
column10 = []
column11 = []
column12 = []
column13 = []
column14 = []
column15 = []

columnONEb = p1b['col1'].to_numpy()
columnTWOb = p1b['col2'].to_numpy()
columnTHREE = p1b['col3'].to_numpy()
columnFOUR = p1b['col4'].to_numpy()
columnFIVE = p1b['col5'].to_numpy()
columnSIX = p1b['col6'].to_numpy()
columnSEVEN = p1b['col7'].to_numpy()
columnEIGHT = p1b['col8'].to_numpy()
columnNINE = p1b['col9'].to_numpy()
columnTEN = p1b['col10'].to_numpy()
columnELEVEN = p1b['col11'].to_numpy()
columnTWELVE = p1b['col12'].to_numpy()
columnTHIRTEEN = p1b['col13'].to_numpy()
columnFOURTEEN = p1b['col14'].to_numpy()
columnFIFTEEN = p1b['col15'].to_numpy()


for i in range(len(columnONEb)):
    column1.append(columnONEb[i])
    column2.append(columnTWOb[i])
    column3.append(columnTHREE[i])
    column4.append(columnFOUR[i])
    column5.append(columnFIVE[i])
    column6.append(columnSIX[i])
    column7.append(columnSEVEN[i])
    column8.append(columnEIGHT[i])
    column9.append(columnNINE[i])
    column10.append(columnTEN[i])
    column11.append(columnELEVEN[i])
    column12.append(columnTWELVE[i])
    column13.append(columnTHIRTEEN[i])
    column14.append(columnFOURTEEN[i])
    column15.append(columnFIFTEEN[i])



print("Null Hypothesis: No association between the traits.")
print("Alternative Hypothesis: There is association between the traits.")

print("\n\nMutual Information:")

#Array to hold all possible combinations scores
allcombos = []
combosJacc = []
getchissquare = []

#Array to obtain p values
Chis_pvalues = []
Jacc_pvalues = []
Mi_pvalues = []


#Obtain all possible combiantion's mutual information and Jaccard in array should be 105
for i in range(1, 16):
    columnA = 'col' + str(i)
    for g in range(1, 16):
        if i == g:
            continue
        if i == '15':
            continue
        columnB = 'col' + str(g)
        if i != 1:
            if i > g:
                continue
            else:
                columnalpha = p1b[columnA].to_numpy()
                columnbravo = p1b[columnB].to_numpy()
                allcombos.append(mutual_info_score(columnalpha, columnbravo))
                combosJacc.append(getJacc(columnalpha, columnbravo))
                getchissquare.append(chis(columnalpha, columnbravo))
        else:
            if i == g:
                continue
            else:
                columnalph = p1b[columnA].to_numpy()
                columnbrav = p1b[columnB].to_numpy()
                allcombos.append(mutual_info_score(columnalph, columnbrav))
                combosJacc.append(getJacc(columnalph, columnbrav))
                getchissquare.append(chis(columnalph, columnbrav))




combosJacc.sort() #Uncomment this to see the graph unsorted
#allcombos.sort()
#getchissquare.sort()
#print(len(getchissquare)) #making sure to have all 105 combinations

#plot change this to display Mutual info, Chi square, and Jaccard
makeprettyplots(combosJacc, "Jaccard")
