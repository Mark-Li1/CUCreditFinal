from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv as out
ds = pd.read_csv("C:\\Users\\A Name\\CreditColumbiaFinal\\Credit Card Data - train.csv")
# print(ds)


OCCPP = ds["Occupation"]
SSNPP = ds["SSN"]
LTuP = ds["TypeofLoan"]



def cleanup(OCC, SSN, LT):
    freq = []
    SSNnD = []
    OCCnD = []
    LTnD = []
    j = 0
    counter = 0
    for i in range(0, len(SSN) - 1):
        if (SSN[i] not in SSNnD):
            # Add lists and append for each value, if needed
            SSNnD.append(SSN[i])
            OCCnD.append(OCC[i])
            LTnD.append(LT[i])
            j += 1
            counter = 0
            freq.append([0])
        counter += 1
        freq[len(freq) - 1] = counter
    return [freq, SSNnD, OCCnD, LTnD]


Freq, pSSN, pOCC, LTuP = cleanup(OCCPP, SSNPP, LTuP)
aOCC = list(OrderedDict.fromkeys(pOCC))
# print("Freq: ",Freq,"Occupation :", pOCC,"SSN: ", pSSN, "All Occupations: ", aOCC)

# Time complexity of O(NM) is slow, but will suffice.
freqTable = []

for i in aOCC:
    freqTable.append(0)
    for j in pOCC:
        if (j == i):
            freqTable[len(freqTable) - 1] += 1

# Remove Null values from table.
try:
    freqTable.remove(0)
    aOCC.remove(np.nan)
except ValueError:
    print("Val NAN not found")



print("Freq Table: ", freqTable, "  aOCC: ", aOCC)

#Break up LTuP into a 2D array
LTP = []

LoanTypesnD = []

for i in LTuP:
    try:
        LTP.append(str.split(i, ","))
        LTP[-1][-1] = LTP[-1][-1].replace("and", "")
        for i in range(0, len(LTP[len(LTP)-1])):
            LTP[-1][i] = LTP[-1][i].lstrip().rstrip()
            if(LTP[-1][i] not in LoanTypesnD):
                LoanTypesnD.append(LTP[-1][i])
    except TypeError:
        print("Type Error on LTUP Remove And")

print(LTP)

#TODO:
# 1. Convert Loan Types into Mapping using TRUE/FALSE
# 2. Write into Processed Data.xlsx

#out.writer("C:\\Users\\A Name\\CreditColumbiaFinal\\Mapping.csv")

rows = []



try:
    plt.bar(x=aOCC, height=freqTable)
except TypeError:
    print("Type error occured")
finally:
    plt.show()
