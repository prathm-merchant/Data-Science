
#imports

import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

#PART 1: LOAD THE DATA INTO PANDAS DATAFRAME
# read the breast cancer data into a pandas DataFrame, including column names

col_names = ['id number', 'Clump_Thickness', 'Uniformity_Cell Size', 'Uniformity_Cell Shape', 'Marginal Adhesion', 'Epithelial_Cell_Size','Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses', 'Class']
bcancer_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', header=None, names=col_names, na_values=["?"])

#display the top 25 rows of data
bcancer_df.head(25)

# gather basic information about the dataset
bcancer_df.shape

#basic statistics of the data
bcancer_df.describe()

#check the missing values in each columns
bcancer_df.isnull().sum()

#check the total number of missing values in a list view
bcancer_df.isnull().sum().sum().tolist()

#since there are not many NaN values, drop the fields having NaN
bcancer_df.dropna()

#once the data set is clean, store it in as a csv file
bcancer_df.to_csv('C:/Users/ADMIN/Desktop/My Docs/research/bcancer_df-clean1.csv', header=False)