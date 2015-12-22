######################################################################
#  CC0 1.0 Universal
#  $Author: celsa diaz tejada
#  $Date: 10/11/15
#  $Name: eQuiz Test your german vocabulary knowledge ;)
######################################################################

import numpy as np
import csv, sys, re
import pandas as pd
from pandas import DataFrame
import datetime as dt


class namen():
     def __init__(self, df):
         df1 = df[df.columns[0:2]].copy()
         df2 = df[df.columns[2:4]].copy()
         df3 = df[df.columns[4:6]].copy()
         df1.columns = ['a', 'b']
         df2.columns = ['a', 'b']
         df3.columns = ['a', 'b']
         df1.loc[slice(None),'location'] = 'eKuche'
         df2.loc[slice(None),'location'] = 'rBalkon'
         df3.loc[slice(None),'location'] = 'sZimmer'
         df4 = pd.concat([df1, df2, df3], axis=0)
         df4 = df4[pd.notnull(df4['b'])]
         df4.loc[slice(None),'match'] = 0
         df = df4.reset_index()
         df = df[df.columns[1:5]]
         self.dafa = df
	 self.index = self.dafa.index

     def randomindex(self, index):
         self.items = np.random.choice(range(len(index)), len(index), replace=False)

class verben():
     def __init__(self, df):
	 df1 = df[df.columns[0:2]].copy()
         df2 = df[df.columns[2:4]].copy()
         df1.columns = ['a', 'b']
         df2.columns = ['a', 'b']
         df1.loc[slice(None),'objtype'] = 0 # 0 for akk
         df2.loc[slice(None),'objtype'] = 1 # 1 for dat
         df3 = pd.concat([df1, df2], axis=0)
         df3 = df3[pd.notnull(df3['b'])]
         df3['match'] = 0
         df = df3.reset_index()
         df = df[df.columns[1:6]]
	 self.dafa = df
	 self.german = self.dafa.a 
         self.index = self.dafa.index

     def randomindex(self):
         self.items = np.random.choice(range(len(self.index)), len(self.index), replace=False)    

class adjandadv():       
     def __init__(self, df):
         df.columns = ['a', 'b']
         df['match'] = 0
         self.dafa = df
         self.index = self.dafa.index

     def randomindex(self):
         self.items = np.random.choice(range(len(self.index)), len(self.index), replace=False)

class dfresults():
     def __init__(self, df):
	 print df
         self.dafa = df
         self.num = len(self.dafa.index)
         self.match = df['match']
         
     def calculate(self):
         self.right = self.match.tolist()
         self.positive = self.right.count(1)
         self.fraction = self.positive/self.num
         self.percentage = (self.positive*100)/self.num


#######################################################################################################


# Get the input dataframe
df = pd.read_csv(sys.argv[1], sep = ',')

# Clasify questions by type of data
if len(df.columns) == 2:
    obje = "Adjektiv und adverbien"
    print obje
    # Get words randomly order
    mylist = adjandadv(df)
    mylist.randomindex()
    finaldata = mylist.dafa
    ran = mylist.items
    for i in ran:
        print "How would you say - %s - in german?"%finaldata.b[i]
        mya = raw_input("Please enter the answer: ")
        if mya == finaldata.a[i]:
             print "Well done!"
	     finaldata.loc[i,'match'] = 1
	else:
             print "Wrong! The answer was - %s -"%finaldata.a[i] 


elif len(df.columns) == 4:
    obje = "Verben"
    print obje
    # Get words randomly order
    mylist = verben(df)
    mylist.randomindex()
    ran = mylist.items
    finaldata = mylist.dafa
    for i in ran:
        print "How would you say - %s - in german?"%finaldata.b[i]
        mya = raw_input("Please enter the answer: ")
        if mya == mylist.dafa.a[i]:
             print "Well done! You know the translation but... is it akkusative?"
	     obj = raw_input("Please enter the answer (y/n): ")
	     if obj == 'y' and finaldata.objtype[i] == 0:
                 print "Well done! You are getting better ;)"  
                 finaldata.loc[i,'match'] = 1
             elif obj == 'n' and finaldata.objtype[i] == 1:
                 print "Well done! You are getting better ;)"                           
                 finaldata.loc[i,'match'] = 1
             else:
                 print "Wrong!"
        else:
             print "Wrong! The answer was - %s -"%finaldata.a[i]

    
elif len(df.columns) == 6:
    obje = "Namen"
    print obje
    # Get words randomly order
    mylist = namen(df)
    mylist.randomindex()
    ran = mylist.items
    finaldata = mylist.dafa
    print ran
    for i in ran:
        print "How would you say - %s - in german?"%finaldata.b[i]
        mya = raw_input("Please enter the answer: ")
        if mya == finaldata.a[i]:
             print "Well done! You know the translation but what is its gender or location?"
             loc = raw_input("Please enter the answer (eKuche/rBalkon/sZimmer): ")
             if loc == finaldata.location[i]:
                 print "Well done! You know the translation and the gender!"
                 finaldata.loc[i,'match'] = 1
             else:
                     print "Wrong! Sorry, you have to learn also the gender of the Namen..."
        else:
             print "Wrong! The answer was - %s -"%finaldata.a[i]
    
# Get results
myres = dfresults(finaldata)
myres.calculate()
words = str(myres.num)
fract = str(myres.fraction)
perce = str(myres.percentage)
date = str(dt.datetime.now().date())

# Save the results of each quiz in results.csv
fd = open('../results.csv','a')
newrow = date+","+obje+","+words+","+fract+","+perce+"\n"
fd.write(newrow)
fd.close()




