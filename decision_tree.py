#-------------------------------------------------------------------------
# AUTHOR: Charles Kypros
# FILENAME: decision_tree.py
# SPECIFICATION: decision trees in python
# FOR: CS 4200- Assignment #2
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

#read the test data and add this data to dbTest    
#reading the test set in a csv file
dbTest = []
with open('contact_lens_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append (row)

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    for row in dbTraining:
        xDataRow = []
        for i, value in enumerate(row[0:4]):
            if i == 0: xDataRow.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
            elif i == 1: xDataRow.append(1 if value == 'Myope' else 2)
            elif i == 2: xDataRow.append(1 if value == 'No' else 2)
            elif i == 3: xDataRow.append(1 if value == 'Reduced' else 2)
        X.append(xDataRow)

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for row in dbTraining:
        Y.append(1 if row[-1] == 'Yes' else 2)

    #loop your training and test tasks 10 times here
    accuracies = []
    correct_classifications = 0
    incorrect_classifications = 0 
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            testValues = []
            for i, value in enumerate(data[0:4]):
                if i == 0: testValues.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
                elif i == 1: testValues.append(1 if value == 'Myope' else 2)
                elif i == 2: testValues.append(1 if value == 'No' else 2)
                elif i == 3: testValues.append(1 if value == 'Reduced' else 2)
            class_actual = 1 if data[-1] == 'Yes' else 2

            class_predicted = clf.predict([testValues])[0]

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            if class_predicted == class_actual: 
                correct_classifications += 1 
            else:
                incorrect_classifications +=1
            accuracies.append(correct_classifications / (correct_classifications + incorrect_classifications))

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    print(f"\tfinal accuracy when training on {ds}: {min(accuracies)}")