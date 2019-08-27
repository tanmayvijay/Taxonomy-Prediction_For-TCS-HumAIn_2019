##############################
# Testing
from sklearn.feature_extraction.text import CountVectorizer
import scipy.sparse as sparse

# loading the test data
# feel free to replace ngram 1,1 with ngram 1,4
X_test_1_1 = sparse.load_npz("data/8_X_test_1_1.npz")
y_test = sparse.load_npz("data/8_y_test.npz")



# loading the model
model = pickle.load(open("models/1_log_reg_clf.pickle", "rb"))

# predicting the tags on test set
pred = model.predict(test)




# Using Micro average F1 score for Evaluation

from sklearn.metrics import precision_score, recall_score, f1_score

precis = precision_score(y_test, pred, average='micro')
rec = recall_score(y_test, pred, average='micro')
f1 = f1_score(y_test, pred, average='micro')

print("Micro Average F1 Score Metrics:")
print("Precision: {.6f}", precis)
print("Recall: {.6f}", rec)
print("F1 Score: {.6f}", f1)




# loading vectorizer for testing
tags_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("vectorizers/tags_vectorizer.pickle", "rb")))
tags_vec._validate_vocabulary()

ques_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("vectorizers/ngram_1_1_vectorizer.pickle", "rb")))
ques_vec._validate_vocabulary()


print("Predicted tags for Questions")

import pandas as pd

Results = pd.DataFrame({"Questions": ques_vec.inverse_transform(X_test_1_1),
                        "Tags": tags_vec.inverse_transform(pred)})

Results.head(100)
