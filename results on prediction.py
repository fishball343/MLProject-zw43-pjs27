
# coding: utf-8

# In[40]:

import csv
import pandas as pd
import numpy as np
data1=pd.read_csv('epl/useful/fulltrainingset.csv', header=0)
data2=pd.read_csv('epl/useful/fulltestset.csv', header=0)


DF = data1.drop('Season', 1)
DF = DF.drop('Date', 1)
DF = DF.drop('HomeTeam', 1)
DF = DF.drop('AwayTeam', 1)
DF = DF.drop('HR', 1)
DF=DF.drop('HG', 1)
DF=DF.drop('AG', 1)
X_train=np.asarray(DF)

y_train=[]
for i in range(0, len(data1)):
    if data1['HR'][i]=="H":
        y_train.append(1)
    if data1['HR'][i]=="D":
        y_train.append(0)
    if data1['HR'][i]=="A":
        y_train.append(-1)
        
DF = data2.drop('Season', 1)
DF = DF.drop('Date', 1)
DF = DF.drop('HomeTeam', 1)
DF = DF.drop('AwayTeam', 1)
DF = DF.drop('HR', 1)
DF=DF.drop('HG', 1)
DF=DF.drop('AG', 1)
X_test=np.asarray(DF)

y_test=[]
for i in range(0, len(data2)):
    if data2['HR'][i]=="H":
        y_test.append(1)
    if data2['HR'][i]=="D":
        y_test.append(0)
    if data2['HR'][i]=="A":
        y_test.append(-1)
        


# In[20]:

from sklearn.naive_bayes import MultinomialNB
from sklearn import cross_validation
gnb = MultinomialNB()
gnb.fit(X_train, y_train)

1-gnb.score(X_test, y_test)



# In[30]:

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier

clf1 = RandomForestClassifier(n_estimators=15)
clf1 = clf1.fit(X_train, y_train)
1-clf1.score(X_test, y_test)



# In[33]:

from sklearn import svm
lin_clf = svm.LinearSVC(C=0.1, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
     verbose=0)
lin_clf.fit(X_train, y_train) 
1-lin_clf.score(X_test, y_test)


# In[29]:

from sklearn.lda import LDA 

clf3 =LDA()
clf3.fit(X_train, y_train)
1-clf3.score(X_test, y_test)


# In[27]:

clfrbf = svm.SVC(kernel='rbf')
clfrbf.fit(X_train, y_train) 

1-clfrbf.score(X_test, y_test)


# In[18]:

from sklearn.naive_bayes import GaussianNB

clf5 = GaussianNB()
clf5.fit(X_train, y_train)

1-clf5.score(X_test, y_test)
#clf.predict(X_test)


# In[34]:

from sklearn.metrics import confusion_matrix


# In[41]:

#SVM
y_pred1=lin_clf1.predict(X_test)
y_true=y_test
confusion_matrix(y_true, y_pred1)


# In[ ]:




# In[42]:

#Random Forest
#SVM
y_pred1=clf1.predict(X_test)
y_true=y_test
confusion_matrix(y_true, y_pred1)


# In[39]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



