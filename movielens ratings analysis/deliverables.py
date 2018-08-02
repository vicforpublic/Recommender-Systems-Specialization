import pandas as pd

df = pd.read_csv('HW1-data.csv')
avaragesDict={}
for col in df:
    avaragesDict[col] = df[col].mean()
sortedList = sorted(avaragesDict.items(), key=lambda x: x[1])
sortedList.reverse()
sortedList=sortedList[1:-1]
sortedList[0:3]

countDict={}
for col in df:
    countDict[col] = df[col].count()
sortedCountList= sorted(countDict.items(), key = lambda x: x[1])
sortedCountList.reverse()
sortedCountList=sortedCountList[2:]
sortedCountList[0:3]

likedDict={}
for col in df:
    likedDict[col] = df[col][df[col]>3].count()
sortedLikedList = sorted(likedDict.items(), key = lambda x: x[1])
sortedLikedList = sortedLikedList[1:-1]
sortedLikedList.reverse()
sortedLikedList[0:3]

coOcurrenceDict1={}
coOcurrenceDict2={}
matematicallyCorrectCoOcurrenceDict={}
for col in df:
    coOcurrenceDict1[col] = df[col][pd.notnull(df['1: Toy Story (1995)'])].count()/df[col].count()
    coOcurrenceDict2[col] = df[col][pd.notnull(df['1: Toy Story (1995)'])].count()/df['1: Toy Story (1995)'].count()
    matematicallyCorrectCoOcurrenceDict[col] = df[col][pd.notnull(df['1: Toy Story (1995)'])].count()/(df['1: Toy Story (1995)'].count() + df[col][~pd.notnull(df['1: Toy Story (1995)'])].count())
sortedSimpleCorrelList1 = sorted(coOcurrenceDict1.items(), key= lambda x: x[1])
sortedSimpleCorrelList1 = sortedSimpleCorrelList1[0:-3]
sortedSimpleCorrelList1.reverse()
sortedSimpleCorrelList2 = sorted(coOcurrenceDict2.items(), key= lambda x: x[1])
sortedSimpleCorrelList2 = sortedSimpleCorrelList2[0:-3]
sortedSimpleCorrelList2.reverse()
sortedSimpleCorrelList3 = sorted(matematicallyCorrectCoOcurrenceDict.items(), key= lambda x: x[1])
sortedSimpleCorrelList3 = sortedSimpleCorrelList3[0:-3]
sortedSimpleCorrelList3.reverse()
sortedSimpleCorrelList3[0:3]

from scipy.stats.stats import pearsonr
df2 = df.iloc[: , 2:]
correlDict = {}
for col in df2:
    correlDict[col] = pearsonr(df2[col][pd.notnull(df['1: Toy Story (1995)']) & pd.notnull(df[col])], df2['1: Toy Story (1995)'][pd.notnull(df['1: Toy Story (1995)']) & pd.notnull(df[col])])[0]
sortedCorrelList = sorted(correlDict.items(), key = lambda x : x[1])
sortedCorrelList.reverse()
sortedCorrelList[1:4]

dfMale = df.iloc[: , 2:][df.iloc[: , 1] == 0]
dfFemale = df.iloc[: , 2:][df.iloc[: , 1] == 1]
meanMaleDict={}
meanFemaleDict={}
summationMale = 0
countMale = 0
summationFemale = 0
countFemale = 0
for col in dfMale:
    meanMaleDict[col] = dfMale[col].mean()
    meanFemaleDict[col] = dfFemale[col].mean()
    countMale = countMale + dfMale[col].count()
    summationMale = summationMale + dfMale[col].sum()
    countFemale = countFemale + dfFemale[col].count()
    summationFemale = summationFemale + dfFemale[col].sum()
maleList = list(meanMaleDict.items())
femaleList = list(meanFemaleDict.items())
sortedDifMaleLike = []
sortedDifFemaleLike = []
for maleAvgTuple, femaleAvgTuple in zip(maleList, femaleList):
    sortedDifMaleLike.append((maleAvgTuple[0],maleAvgTuple[1]-femaleAvgTuple[1]))
    sortedDifFemaleLike.append((maleAvgTuple[0],femaleAvgTuple[1]-maleAvgTuple[1]))
sortedDifMaleLike = sorted(sortedDifMaleLike, key = lambda x: x[1])
sortedDifFemaleLike = sorted(sortedDifFemaleLike, key = lambda x: x[1])
sortedDifMaleLike.reverse()
sortedDifFemaleLike.reverse()

maleAvg = summationMale/countMale
femaleAvg = summationFemale/countFemale
print("The female avarage is", femaleAvg, "and the male avarage is", maleAvg)
print("men love women hate:", sortedDifMaleLike[0], "women love men hate:", sortedDifFemaleLike[0])
