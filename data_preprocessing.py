###LIBRARIES###
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import missingno as msn

###LOAD EXCEL FILE IN PANDAS###
df = pd.read_excel("FORUN_female_male_compared.xlsx")
###SHOW FIRST 5 ROWS###
df.head()

###DROP ID###
df.drop("mouse_id", axis='columns', inplace=True)

###SET DUMMY VARIABLES FOR SEX AND GENOTYPE###
cat_variables = df[["sex", "genotype"]]

cat_dummies = pd.get_dummies(cat_variables, drop_first=True)
cat_dummies.head()

###REPLACE ROWS###
df=df.drop(["sex", "genotype"], axis=1)
df = pd.concat([df,cat_dummies], axis=1)
df.head()

###SHOW MISSING VALUES###
msno.matrix(df)

###DATA NORMALISATION###
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns = df.columns)
df.head()

###KNN-IMPUTATION###
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

###SAVE NEW EXCEL###
df.to_excel("FORUN-imputed.xlsx")
