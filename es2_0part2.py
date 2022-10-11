#Part 2
from sklearn import linear_model
clf = linear_model.LinearRegression()

#To be completed by the student
model = clf.fit(Train_Set[:200, :11], Train_Set[:200, :11])
Train_pred = np.round(model.predict(Train_Set))
Test_pred = np.round(model.predict(Test_Set))
#MSE = ()/

accuracyTestPred = []
accuracyTrainPred = []
for k in range(1,200,3):    #Calculate the correct prediction
  predTest = 0
  predTrain = 0
  for x in range(len(Test_pred)):
    if calculateKNN(Test_pred[x, :11], k) == Test_pred[x, 11]:
      predTest += 1
    if calculateKNN(Train_pred[x, :11], k) == Train_pred[x, 11]:
      predTrain += 1
  accuracyTestPred.append(predictionTest/len(Test_Set))
  accuracyTrainPred.append(predictionTrain/len(Train_Set))

k = range(1,200,3)

plt.figure()
plt.plot(k, accuracyTestPred, label='Test predicted')
plt.plot(k, accuracyTrainPred, label='Train predicted')
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()
plt.show()
