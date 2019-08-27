# loading the data into ram

import pandas as pd

df_tbc = pd.read_csv("data/5_TBC_tok_stop_stem.csv", usecols=["TBC"])


# Ngrams = (1,1)
# using count vectorizer on TBC column
# we drop all the words with frequency leass than 0.0001
# also to control the no of columns, we limit max_features to 25000

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(ngram_range=(1,1), tokenizer=lambda x: x.split(), min_df=0.00009, max_features=25000)
X_data_1_1 = vectorizer.fit_transform(df_tbc["TBC"])


# Saving the new data as a sparse matrix in npz format
# Also saving vectorizer vocabulary for testing

from scipy import sparse
sparse.save_npz("data/6_X_data_1_1.npz", X_data_1_1)

# !cp 6_X_data_1_1.npz drive/My\ Drive/tcs/

# we can only save the vocabulaty dictionary
import pickle
pickle.dump(vectorizer.vocabulary_, open("vectorizers/ngram_1_1_vectorizer.pickle", "wb"))

# !cp ngram_1_1_vectorizer.pickle drive/My\ Drive/tcs/



# Ngrams = (1,4)
# using count vectorizer on TBC column
# we drop all the words with frequency leass than 0.0001
# also to control the no of columns, we limit max_features to 25000

vectorizer = CountVectorizer( ngram_range=(1,4), tokenizer=lambda x: x.split(), min_df=0.00009, max_features=25000)
X_data_1_4 = vectorizer.fit_transform(df_tbc["TBC"])



# saving the 1-4 vocabulary and spase matrix data

# saving new vectorizer for testing
pickle.dump(vectorizer.vocabulary_, open("vectorizers/ngram_1_4_vectorizer.pickle", "wb"))

# saving sparse matrix into npz
sparse.save_npz("data/7_X_data_1_4.npz", X_data_1_4)

# !cp 7_X_data_1_4.npz drive/My\ Drive/tcs/
# !cp ngram_1_4_vectorizer.pickle drive/My\ Drive/tcs





print("N-gram=(1,1)")
print(X_data_1_1.shape)
pd.DataFrame(X_data_1_1[:10].toarray()).head()	



print("N-gram=(1,4)")
print(X_data_1_4.shape)
pd.DataFrame(X_data_1_4[:10].toarray()).head()



# loading the tags into ram and discarding TBC column to free up RAM

import pandas as pd

df_tbc = pd.read_csv("data/5_TBC_tok_stop_stem.csv", usecols=["Tags"])



# vectorizing the tags and saving vectorizer to future purposes

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(tokenizer = lambda x: x.split(), binary='true')
tags = vectorizer.fit_transform(df_tbc['Tags'])


import pickle
pickle.dump(vectorizer.vocabulary_, open("vectorizers/tags_vectorizer.pickle", "wb"))

# !cp tags_vectorizer.pickle drive/My\ Drive/tcs/


# to load
# loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))




# saving tags vectorized sparse matrix as npz

from scipy import sparse
sparse.save_npz("data/Tags_vectorized.npz", tags)

# !cp data/Tags_vectorized.npz drive/My\ Drive/tcs/



print(tags.shape)

pd.DataFrame(tags[:10].toarray()).head()
