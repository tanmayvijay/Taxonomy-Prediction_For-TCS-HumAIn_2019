# loading n-gram 1,1 data
# feel free to use ngram 1,4

X_data = sparse.load_npz("data/6_X_data_1_1.npz")
y_data = sparse.load_npz("data/Tags_vectorized.npz")



# splitting Train:Test :: 98:2

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.02, random_state=42)





print("Training Data:", X_train.shape)
print("Test Data:", X_test.shape)




# saving train and test files separately

sparse.save_npz("data/8_X_train_1_1.npz", X_train)
sparse.save_npz("data/8_X_test_1_1.npz", X_test)


sparse.save_npz("data/8_y_train.npz", y_train)
sparse.save_npz("data/8_y_test.npz", y_test)




# Imports for all Classifiers

from scipy import sparse

# !pip install scikit-multilearn
from sklearn.multiclass import OneVsRestClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB



############################################

# Logistic Regression - (1,1)

############################################

from scipy import sparse

# feel free to replace data with ngram 1-4 if you saved it
X_train_1_1 = sparse.load_npz("data/8_X_train_1_1.npz")
y_train = sparse.load_npz("data/8_y_train.npz")

# fitting the model
clf_log_reg_1 = OneVsRestClassifier(LogisticRegression(C=0.1, penalty='l2', verbose=1))
clf_log_reg_1.fit(X_train_1_1, y_train)

# saving model to disk
import pickle
pickle.dump(clf_log_reg_1, open("models/1_log_reg_clf.pickle", "wb"))

# !cp models/1_log_reg_clf.pickle drive/My\ Drive/tcs/