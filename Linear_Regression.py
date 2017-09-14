''''
 ML URL           :https://archive.ics.uci.edu/ml/datasets/Automobile
 Data Description : https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names
 Data Link        :https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data

 @Author          : Hari om Singh

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split




columns= ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels",
          "engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders",
          "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg",
          "highway-mpg","price"]

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data', header=None,names=columns)



### Consolidating the columns which are categorical

categorical_columns=["make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","engine-type",
                     "num-of-cylinders","fuel-system"]


numeric_columns=["symboling","normalized-losses",
          "wheel-base","length","width","height","curb-weight",
          "engine-size","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg",
          "highway-mpg","price"]





## Replacing the columns which are not provided "?" .

for variable in df.columns:
    df[variable] = df[variable].replace('?', np.nan)


## Aggregating the columns which nulls count .
print(np.sum(df.isnull()))

## Listing the columns which has missing values
impute_columns=["normalized-losses","num-of-doors","bore","stroke","horsepower","peak-rpm","price"]

## Dropping the rows - Price columns which are not present , as price is needed for prediction.
df = df[pd.notnull(df['price'])]

## Aggregating the columns which nulls count .
print(np.sum(df.isnull()))

impute_columns_new=["normalized-losses","num-of-doors","bore","stroke","horsepower","peak-rpm"]
impute_columns_new_numeric=["normalized-losses","bore","stroke","horsepower","peak-rpm"]
impute_columns_new_categorical=["num-of-doors"]




## Getting the different values count for the impute columns .

for variable in impute_columns:
  print ("-------------------------------")
  print ("Histogram for " + variable)
  print ("-------------------------------")
  print (df[variable].value_counts())
  print ("")

### Type conversion for the columns

df["normalized-losses"] = df["normalized-losses"].astype(np.float)
df["bore"] = df["bore"].astype(np.float)
df["stroke"] = df["stroke"].astype(np.float)
df["horsepower"] = df["horsepower"].astype(np.float)
df["peak-rpm"] = df["peak-rpm"].astype(np.float)

#### Replacing the nulls with mean or mode based on nature of data ####


df["normalized-losses"].fillna(df["normalized-losses"].mean(), inplace=True)
df["bore"].fillna(df["bore"].mean(), inplace=True)
df["stroke"].fillna(df["stroke"].mean(), inplace=True)
df["horsepower"].fillna(df["horsepower"].mean(), inplace=True)
df["peak-rpm"].fillna(df["peak-rpm"].mean(), inplace=True)


imputed_values_categorical=df[impute_columns_new_categorical].mode()
for variable in impute_columns_new_categorical:
    df[variable].fillna(value=imputed_values_categorical[variable][0], inplace=True)


print(np.sum(df.isnull()))

################################### Encoding  ###############################################


df['num-of-doors'] = df['num-of-doors'].map(lambda x :4 if x == 'four' else 2)

num_of_cylinders_replace={'eight':8,'five':5,'four':4,'six':6,'three':3,'twelve':12,'two':2}

df['num-of-cylinders']=df['num-of-cylinders'].map(num_of_cylinders_replace)

# Converting the categorical data into the equivalent code


make_replace={"alfa-romero":1,"audi":2,"bmw":3,"chevrolet":4,"dodge":5,"honda":6,"isuzu":7,"jaguar":8,"mazda":9,"mercedes-benz":10,"mercury":11,"mitsubishi":12,"nissan":13,"peugot":14,"plymouth":15,"porsche":16,"renault":17,"saab":18,"subaru":19,"toyota":20,"volkswagen":21,"volvo":22}
fuel_type_replace={"diesel":1,"gas":0}
aspiration_replace={"std":0,"turbo":1}
engine_location_replace={"front":0,"rear":1}

df['make']=df['make'].map(make_replace)
#df['fuel-type']=df['fuel-type'].map(fuel_type_replace)
#df['aspiration']=df['aspiration'].map(aspiration_replace)
df['engine-location']=df['engine-location'].map(engine_location_replace)


df = pd.get_dummies(df, columns=['body-style'])
df=  pd.get_dummies(df, columns=['engine-type'])
df=  pd.get_dummies(df, columns=['fuel-system'])
df=  pd.get_dummies(df, columns=['drive-wheels'])
df=  pd.get_dummies(df, columns=['fuel-type'])
df=  pd.get_dummies(df, columns=['aspiration'])

#print(df["engine-location"])

################################### Data Visualizations #####################################

data1=df.ix[:,["aspiration","engine-location","fuel-type","make","normalized-losses","stroke","wheel-base"]]

data1.hist()
plt.show()




#################################### Spliting the Data into Training and Test Data set ######

print(df.columns)


Xin=df[['symboling', 'normalized-losses', 'make', 'num-of-doors',
       'engine-location', 'length', 'width', 'height',
       'curb-weight', 'num-of-cylinders', 'engine-size', 'bore', 'stroke',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg', 'price', 'body-style_convertible', 'body-style_hardtop',
       'body-style_hatchback', 'body-style_sedan', 'body-style_wagon',
       'engine-type_dohc', 'engine-type_l', 'engine-type_ohc',
       'engine-type_ohcf', 'engine-type_ohcv', 'engine-type_rotor',
       'fuel-system_1bbl', 'fuel-system_2bbl', 'fuel-system_4bbl',
       'fuel-system_idi', 'fuel-system_mfi', 'fuel-system_mpfi',
       'fuel-system_spdi', 'fuel-system_spfi', 'drive-wheels_4wd',
       'drive-wheels_fwd', 'drive-wheels_rwd', 'fuel-type_diesel',
       'fuel-type_gas', 'aspiration_std', 'aspiration_turbo']].as_matrix()

Yin=df[['price']].as_matrix()

X_train, X_test, Y_train, Y_test = train_test_split(Xin, Yin, test_size=0.2, random_state=42)

print('X_train --- length -->',len(X_train))
print('Y_train --- length -->',len(Y_train))
print('X_test --- length -->',len(X_test))
print('Y_test --- length -->',len(Y_test))

#################################### Model Prediction ########################################

model = linear_model.LinearRegression()

model.fit(X_train, Y_train)


price_y_pred = model.predict(X_test)
print('Predicted Value ---->')
print(price_y_pred)
print('Actual Value ---->')

print(Y_test)

# The mean squared error

## 1 model =11562345
## 2 model =11469410 -- after dropping wheel base
## 3 model =0  -- after putting get_dummies  fuel-type and aspiration
print("Mean squared error: %.2f"% mean_squared_error(Y_test, price_y_pred))

