#-------------------------------------------------------------------------
# AUTHOR: Charles Kypros
# FILENAME: knn.py
# SPECIFICATION: knn error rate calculation in python
# FOR: CS 4200- Assignment #2
# TIME SPENT: 20 minutes
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
num_correct = 0
num_incorect = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    X = []
    Y = []
    
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    for j in range(len(db)):
        if i != j:
            training_feature = [int(db[j][0]), int(db[j][1])]
            X.append(training_feature)            

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]  
    for j in range(len(db)):
        if i != j:
            training_class = 1 if db[j][2] == '+' else 2
            Y.append(training_class)

    #store the test sample of this iteration in the vector testSample
    testSample = [int(instance[0]), int(instance[1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    class_actual = 1 if instance[2] == '+' else 2

    if class_predicted == class_actual:
        num_correct += 1
    else:
        num_incorect += 1

#print the error rate
error_rate = num_incorect / (num_correct + num_incorect)
print(error_rate)