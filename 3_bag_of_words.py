
# importing the libraries and downloading packages

# Natural Language Toolkit
import nltk
# Stopwords lsist
from nltk.corpus import stopwords
# tokenizer
from nltk.tokenize import word_tokenize
# Stemmer
from nltk.stem.snowball import SnowballStemmer

# downloading necessary packages
nltk.download('punkt')
nltk.download('stopwords')

# Creating Stop words and Stemmer objects
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")




words = word_tokenize(df_tbc.iloc[0,0])

t = " ".join(str(stemmer.stem(word)) for word in words if word not in stop_words )

print(t)




#  Tokenize + Stopword removal + Stem

tok_stop_stem_list=[]

for i in range(df_tbc.shape[0]):
  # tokenize
  words = word_tokenize(df_tbc.iloc[i,0])
  # stopword removal and stemming
  t = " ".join(str(stemmer.stem(word)) for word in words if word not in stop_words  )
  tok_stop_stem_list.append(t)

  # to see progress
  if not i%100000:
    print(i)



# Saving Data

# replacing in df
df_tbc["TBC"] = tok_stop_stem_list

# Also adding tags
df_tbc["Tags"] = df["Tags"]


# saving to csv
df_tbc.to_csv("data/5_TBC_tok_stop_stem.csv", index=True)

# !cp data/5_TBC_tok_stop_stem.csv drive/My\ Drive/tcs/



print(df_tbc.shape)

df_tbc.head()


# Total no of words
# Average words/ example


len_tbc_new = 0

for i in range(df_tbc.shape[0]):
  l = len(df_tbc["TBC"][i].split())

  len_tbc_new += l

print("OLD:")
print("Total:", len_tbc)
print("Words/row:", len_tbc/df_tbc.shape[0])

print("NEW:")
print("Total:", len_tbc_new)
print("Words/row:", len_tbc_new/df_tbc.shape[0])
