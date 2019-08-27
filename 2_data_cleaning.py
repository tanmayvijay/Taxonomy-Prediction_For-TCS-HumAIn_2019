import pandas as pd

df = pd.read_csv("data/3_Train_5L.csv", usecols=["Title", "Body", "Tags"])


# Cleaning Titles using Regular Expressions

import re

titles_list=[]
for i in range(df.shape[0]):
  # taking out html tags if any
  x = re.sub(r"</{0,1}[\w]+>", " ", df["Title"][i] )
  # replacing c++ and c#
  x= re.sub(r"C\+\+", "CPP", x)
  x = re.sub(r"C#", "CSHARP", x)
  # removing non alpahbets
  x = re.sub(r"[^a-zA-Z]+", " ", x)
  # removing extra spaces
  x = re.sub(r"[\s]+", " ", x)
  # removing all single letters
  x = re.sub(r"(?:^| )+[a-bd-qs-zA-BD-QS-Z](?=$| )+", "", x)

  # adding to list
  titles_list.append(x.lower())

# replacing in dataset
df["Title"] = titles_list




# cleaning the body


import re
code_list=[]
bodies_list=[]
for i in range(df.shape[0]):
  # separating the code
  code = str( re.findall(r"<code>(.*?)</code>", df["Body"][i], flags=re.DOTALL) ) or "No_code"
  # removing code from body
  x = re.sub(r"<code>(.*?)</code>", " ", df["Body"][i], flags=re.MULTILINE|re.DOTALL)
  # removing html tags
  x = re.sub(r"</{0,1}[\w]+>", " ", x )
  # replacing c+ and c#
  x = re.sub(r"C\+\+", "CPP", x)
  x = re.sub(r"C#", "CSHARP", x)
  # removing non alphabets
  x = re.sub(r"[^a-zA-Z]+", " ", x)
  # removing extra spaces
  x = re.sub(r"[\s]+", " ", x)
  # removing single characters
  x = re.sub(r"(?:^| )+[a-bd-qs-zA-BD-QS-Z]{1,2}(?=$| )+", "", x)

  # adding to list
  bodies_list.append(x.lower())
  code_list.append(code.lower())


# replacing in dataset
df["Body"] = bodies_list
df["Code"] = code_list





# cleaning the code

import re
clean_code_list = []
for i in range(df.shape[0]):
  # removing non alphabets 
  x = re.sub(r"[^a-zA-Z]+", " ", df["Code"][i])
  # removing all less than 3 letter words
  x = re.sub(r"\b\w{1,3}\b", " ", x)
  # removing all extra spaces
  x = re.sub(r"[\s]+", " ", x)
  # removing left and right spaces
  x = x.strip()

  # adding to list
  clean_code_list.append(x)


# replacing in dataset
df["Code"] = clean_code_list



# looking at new dataset

df.head()



# Saving to new csv to mark checkpoint

df.to_csv("data/4_Cleaned_Train.csv", index=True)

# !cp data/4_Cleaned_Train.csv drive/My\ Drive/tcs/


# Creating Title + Body + Code Dataframe

df_tbc = pd.DataFrame()

# adding T B and C separated by space
df_tbc["TBC"] = df["Title"] + " " + df["Body"] + " " + df["Code"]



# Looking at new DF

print(df_tbc.shape)

df_tbc.head()




# Total no of words
# Average words/ example


len_tbc = 0

for i in range(df_tbc.shape[0]):
  l = len(df_tbc["TBC"][i].split())

  len_tbc += l

# Total no of words
print("Total Words:",len_tbc)

# Average words/ example
print("Average words per example:", len_tbc/df_tbc.shape[0])
