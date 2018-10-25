# import external libs
import numpy np
import pandas as pd
import sklearn as sk
from sklearn import datasets as ds
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#laod dataset
df = ds.load_breast_cancer()

# write data
def accuracy(predict):
    count = 0
    for i in range(len(predict)):
        if not predict[i] == test_labels[i]:
            count = count + 1
    return 1 - count/len(predict)

print(accuracy(predict5))X,y = df["data"],df["target"]
train,test,train_labels,test_labels = train_test_split(X,y,test_size=0.3,random_state=123)
gaus = GaussianNB()
model = gaus.fit(train, train_labels)
predict = model.predict(test)

def accuracy(predict):
    count = 0
    for i in range(len(predict)):
        if not predict[i] == test_labels[i]:
            count = count + 1
    return 1 - count/len(predict)

print(accuracy(predict))
