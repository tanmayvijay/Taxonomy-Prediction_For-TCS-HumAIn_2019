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
###### Instead of installing these requirements, it's recommended to use [Google Colab](https://colab.research.google.com/) to run the notebook. </br>To use python scripts, the requirements are as following:
* Python 3.7
* Numpy
* Pandas
* Matplotlib
* Scikit-Learn
* Scipy
* NLTK
* Pickle

</br>

#### Steps to install requirements
1. Download and Install Python 3.7 from [this link](https://www.python.org/downloads/)
2. Open Terminal
3. Run: **pip -r install requirements.txt** on Windows.</br>
   Use **sudo pip -r install requirements.txt** on Linux

</br>

### Dataset Link
Dataset is taken from [Facebook Recruiting III - Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) competition on Kaggle.

</br>

#### Steps to download data
1. Download data from: [link](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/download/Train.zip) (2.2 GB)
2. Move the Downloaded file to **data** folder in the cloned Repository.
3. Extract Train.zip to obtain Train.csv
4. Repeat steps 2 and 3 for Test data downloaded from [this link](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/download/Test.zip) (725 MB)

</br>

### How to run the Code
> The code is available as both Notebook and Python Scripts. Anyone of these can be used.

#### To use the Notebook
1. Clone the Repository to your local machine or on Google Colab.
2. Download data using steps specified above and **make sure that *Train.csv* is in *data/* directory**
3. In case you use local machine, create a new *Virtual Environment* and install all the requirements specified in *requirements.txt* using steps specified above.
4. Open Notebook in JupyterLab or in Google Colab.
5. Read through it directly or Execute all cells.

#### To use Scripts
1. Clone the repository to your machine.
2. Download data using steps specified above and **make sure that *Train.csv* is in *data/* directory**
3. Create a new *Virtual Environment* and install all the requirements specified in *requirements.txt* using steps specified above.
4. Run each script in following order:
   1. *1_data_sampling.py*
   2. *2_data_cleaning.py*
   3. *3_bag_of_words.py*
   4. *4_data_vectorize.py*
   5. *5_train_model.py*
   6. *6_test_model.py*

</br>

### How to Test
To test the model, we can use *Test_new.npz* that we created during the **data sampling and cleaning steps**.
* First we have to train the model (either by running the notebook or by running scripts 1 to 5.)
* Once the model is trained, we can test it using last cell of the notebook or using script *6_test_model.py* (recommended).
###### NOTE: Make sure that *Test_new.npz is in *data/* directory.* 

</br>
</br>
</br>

## Algorithm {Pseudo Code}
###### I have created this project for Idea Submission round at TCS HumAIn 2019. The dataset and Problem description is provided by TCS team. So, a big Thanks to everyone at TCS.

### This Project includes basically 6 big steps:
1. Data Exploration 
2. Data Cleaning and Data Engineering Part-1
3. Data Engineering Part-2
4. Tokenize + Remove Stop words + Stemming + Vectorizing 
5. Training
6. Testing

</br>

#### Data Exploration
* Check for all NaN values in data.
* Plot tags frequency.
* Check how tags are distributed among question.
* Obtain Conclusion and Strategize next steps. 


#### Data Cleaning and Data Engineering Part-1
* Remove unnecessary features from data [Id].
* Drop all rows where Tags column is NaN. 
* Select Most Frequent 500 tags.
   * Create a list of top 500 tags.
   * Find indices of examples containing all tags as a subset of top 500 tags.
* Sample 500,000 indices from list of indices obtained from previous step.
* Sample the training set using those indices and save.


#### Data Engineering Part-2
* Using Regular Expression, clean all the Titles in the Title column.
* Separate Code part from the Body and put into Code column.
* Clean Body column using Regular Expression.
* Similarly, clean Code Column.
* Create new Data Frame by adding Title, Body and Code columns, separated by space into a single column.


#### Tokenize + Remove Stop words + Stemming + Vectorizing
* Loop through all the 500,000 examples:
   * Tokenize the text
   * Remove Stop words from it
   * Stem the remaining words
   * Join the words again to form a string
   * Save the new modified dataset. 
* Apply binary Count Vectorizer on Tags
* Apply Count Vectorizer on Text    


#### Training
* Train Stochastic Gradient Descent model.
* Train Support Vector Classifier.
* Train Logistic Regression Classifier.


#### Testing
* Test different models on data.
* Select the best performance model
