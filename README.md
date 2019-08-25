# Taxonomy-Prediction_For-TCS-HumAIn_2019
In this repository, I submit my ideas, learnings and code during my attempt at solving Taxonomy Prediction Problem for TCS HumAIn 2019.

## Problem Statement
Taxonomy Creation -	For the given content, come up with a solution to build the taxonomy.
* For a given Question, we have to predict the tags based on the text in Question *Title* and *Body*.

</br>

### Dataset Description
**Id** - Unique identifier for each question.</br>
**Title** - The question's title.</br>
**Body** - The body of the question.</br>
**Tags** - The tags associated with the question.</br>
</br>

*Title* and *Body* Columns contain text of the question which is the input to the **Taxonomy Prediction** model.</br>
*Tags* Column contain all the tags associated with the *Title* and *Body* of the Question.</br>
</br>

Automatically predicting tags can be very useful for websites and their users, as Tagging of posts and question is time consuming and also very boring.</br>

#### So, this is a multi-class multi-label problem. Training dataset has roughly 60M examples.
##### But, we use only 500,000 examples which are carefully sampled such that they contain only most-frequent 500 tags.
</br>


### Requirements
* Python 3.7
* Numpy
* Pandas
* Matplotlib
* Scikit-Learn
* Scipy
* NLTK
* Pickle

#### Steps to install requirements
1. Download and Install Python 3.7 from [this link](https://www.python.org/downloads/)
2. Open Terminal
3. Run: **pip -r install requirements.txt** on Windows.</br>
   Use **sudo pip -r install requirements.txt** on Linux


### Dataset Link
Dataset is taken from [Facebook Recruiting III - Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) competition on Kaggle.

</br>

#### Steps to download data
1. Download data from: [link](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/download/Train.zip) (2.2 GB)
2. Move the Downloaded file to **data** folder in the cloned Repository.
3. Extract Train.zip to obtain Train.csv
4. Repeat steps 2 and 3 for Test data downloaded from [this link](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/download/Test.zip) (725 MB)



