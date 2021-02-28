#-------------------------------------------------------------------------
# AUTHOR: Charles Kypros
# FILENAME: naive_bayes.py
# SPECIFICATION: Calculates naive bayes confidence prediction in python
# FOR: CS 4200- Assignment #2
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv


#reading the training data
db = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
features = {
    'Sunny': 1,
    'Overcast': 2,
    'Rain': 3,
    'Hot': 1,
    'Mild': 2,
    'Cool': 3,
    'High': 1,
    'Normal': 2,
    'Strong': 1,
    'Weak': 2
}

classes = {
    'Yes': 1,
    'No': 2
}

X = []
Y = []
for row in db:
    instance = []
    for value in row[1:-1]:
        instance.append(features[value])
    X.append(instance)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
for row in db:
    Y.append(classes[row[-1]])


#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append(row)

test_X = []

for row in dbTest:
    test_instance = []
    for value in row[1:-1]:
        test_instance.append(features[value])
    test_X.append(test_instance)

#printing the header of the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
for row in dbTest:
    test = []
    for value in row[1:-1]:
        test.append(features[value])
    predicted = clf.predict_proba([test])[0]
    if max(predicted) >= 0.75:
        output = ""
        for i in range(5):
            output += row[i].ljust(15)
        play_tennis = "Yes" if predicted[0] > predicted[1] else "No"
        output += play_tennis.ljust(15)
        output += str(max(predicted)).ljust(15)
        print(output)