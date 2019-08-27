# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Import data

df = pd.read_csv("data/Train.csv")

# Data frame shape and few data points

print(df.shape)
df.head(5)



df.isna().sum()




# Plotting Tag Distribution in questions.

# creating a list of all tags
all_tags = [tag for slist in df["Tags"].dropna().values for tag in slist.split()]

# counting each tag
import collections
counter=collections.Counter(all_tags)

# creating a list of most frequent 100 tags
tags_list = [ y for x, y in sorted(counter.items(), key=lambda x: x[1], reverse=True) ]
top_100_tags = tags_list[:100]

# plotting the frequency
plt.plot(top_100_tags)
plt.title("Tag Distribution in Questions")
plt.grid()
plt.xlabel("Tag index")
plt.ylabel("Frequency in tags")
plt.show()





# Plotting no of tags in questions

# counting the no of tags in each question
df["Tag_Counts"] = df.dropna().Tags.str.split().apply(lambda x: len(x))
tag_counts =  df.dropna()["Tag_Counts"].tolist()

# dropping unnecessary columns
df.drop(columns = ["Tag_Counts"], inplace=True)

# plotting using seaborn
import seaborn as sbn
sbn.countplot(tag_counts, palette='gist_rainbow')
plt.title("Distribution of Number of tags ")
plt.xlabel("No. of Tags")
plt.ylabel("No. of Questions")
plt.show()



# Dropping all NaN tags and corresponding questions

import pandas as pd
# loading data
df = pd.read_csv("data/Train.csv")
print("Shape of dataset Before: ", df.shape)

# dropping nans
df.dropna(inplace=True)

# creating new index
df.reset_index(inplace=True)
df.drop(columns=['index'], inplace=True)

print("Shape of dataset After: ", df.shape)




# dropping Id column

df.drop(columns=["Id"], inplace=True)

# Marking data checkpoint
df.to_csv("data/2_Train_No_NaN.csv", index=False)



# Importing new dataset

import pandas as pd
df = pd.read_csv("data/2_Train_No_NaN.csv")

print(df.shape)
df.head()




# list of all tags in all questions
all_tags = [tag for slist in df["Tags"].values for tag in slist.split()]

print ("Total no of tags in all questions:", len(all_tags))



# Counting tag frequency and selecting top 500 tags

import collections

# counting tag frequency
counter=collections.Counter(all_tags)
counter = { x:y for x, y in sorted(counter.items(), key=lambda x: x[1], reverse=True) }

# selecting top 500 tags
top_tags = set(list(counter.keys())[:500])




# finding indices of questions which have only top 500 tags

req_indices=[]

# question's tag set must be a subset of out top tags list
for i in range(df.shape[0]):
  tags = set(df["Tags"][i].split())
  if tags.issubset(top_tags):
    req_indices.append(i)

# indices of all appropriate questions
print(req_indices[:10])





# sampling 500000 examples with top 500 tags only

# selecting 500,000 indices
import random
req_indices_5L = random.sample(req_indices, k=500000)

# sampling questions from dataset
df = df.iloc[req_indices_5L, :]

# creating new index
df.reset_index(inplace=True)
df.drop(columns=["index"], inplace=True)

# saving new dataset
df.to_csv("data/3_Train_5L.csv", index=True)
# !cp 3_Train_5L.csv drive/My\ Drive/tcs/


# OPTIONAL
# saving indices list
# req_indices_df = pd.DataFrame({"Indices": req_indices_5L})
# req_indices_df.to_csv("data/req_indices.csv", index=False)
# !cp data/req_indices.csv drive/My\ Drive/tcs/


print(df.shape)
df.head()
