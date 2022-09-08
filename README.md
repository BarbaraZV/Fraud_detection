# Credit Card Transactions Fraud Detection

The purpose of this project is to detect the fraudulent transactions with some classification models and create an application prototype to detect a fraudulent transaction. 

# Authors
- *Barbara Vargas*
  - Contact : barbvargasz@gmail.com
- *Mauricio Bock*
  - Contact : mauricio.bock@gmx.de
  
 *July 2022, Berlin*

## Content
- [Project Description](#Project_Description)  
- [Questions & Hypotheses](#Questions_&_Hypotheses)  
- [Datasets](#datasets)
- [Resources](#resources) 
- [Organization](#organization)
- [Links](#links)
 
## Project_Description

A typical organization loses an estimated 5% of its yearly revenue to fraud, not just the banks but most of the business with a digital platform to pay. Of course, the customers want to be ensured that they won’t be charged for the items they did not purchase.

To decrease this issue we will use various predictive models to see how accurate they are. We will use supervised learning algorithms (Classification) to detect fraudulent behavior similar to past ones. Moreover, in fraud analytics we have to deal with highly imbalanced datasets when classifying fraud versus non-fraud.

## Questions & Hypotheses

1. Do fraudulent trnsactions occur more often during certain time frame?
2. What is the spending pattern on Credit Card Fraud Detection?
3. How much money is used in fraud transactions?

After the Exploratory Data Analysis we discovered that the fraudulent transactions are happening mainly at night, when the victims are sleeping or are less likely to notice the fraud.
Regarding the spending patter we determine that fraudulent over Non-Fraudulent transaction in Online Shopping and Offline Grocery Shopping categories increased over 10% to 15% in comparison to other category spendings.
The data base in this project are a simulation from real data, considering this we can say that while normal transactions tend to be around 200 Dollars or less, we see fraudulent transactions peak around 300 Dollars and then at the 800-1000 Dollars range.

If you are a victim, the first thing that you want to do  is block quickly your account, right?. That's why we use 
Decision Trees, a clasification model that must be able to detect fraudulent transactions.
Recall assures we don't predict fraudulent transactions as valid transactions.
And of course this is our priority.

Note: The recall measures the model's ability to detect Positive samples (Fraudulent transactions). The higher the recall, the more positive samples detected.

## Datasets

For this project we use two simulated credit card transaction datasets. These timeframe include Transactions from 1st Jan 2019 to 31st Dec 2020

1. 'Credit Card Fraud Analysis and Modeling'
The Dataset is a merge form the following data.
fraudTest.csv
fraudTrain.csv
Link: https://www.kaggle.com/code/nathanxiang/credit-card-fraud-analysis-and-modeling/data

## Resources

To understand better the process to simulate fraud transaction data you can go to [this Github repo](https://github.com/namebrandon/Sparkov_Data_Generation)
To understand better how the fraud detection works you can go to [this link] (https://towardsdatascience.com/credit-card-fraud-detection-using-machine-learning-python-5b098d4a8edc)
The principal resources are from this kaggle project to understand the topic and all differents methods to explore and predict a fraud detection are: 
https://www.kaggle.com/code/nathanxiang/credit-card-fraud-analysis-and-modeling/data
https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/notebook#Test-Data-with-Logistic-Regression:
https://bookdown.org/max/FES/

## Organization

This repository cintains the folowwing files :
- Presentation
- Notebooks (EDA Notebook, Modeling Notebook with different scenarios)
- csv files 

# Links
We report here relevant references:
- https://www.kaggle.com/code/nathanxiang/credit-card-fraud-analysis-and-modeling/notebook
- https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/notebook#Test-Data-with-Logistic-Regression:
- https://www.kaggle.com/code/ohseokkim/creditcard-fraud-balance-is-key-feat-pycaret
