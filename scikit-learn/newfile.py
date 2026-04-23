import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('C:\\Users\\PREM MOTGHARE\\Desktop\\introduction to aiml by infosys\\python\scikit-learn\\auto_mpg.csv')
print(df.info())

df.dropna(inplace = True)

# creating an predictor variable here all variables are used as predictors except the target(mpg), and name
x = df.iloc[:,1:8]

#creating the target 
y = df.iloc[:,0]

x = pd.get_dummies(x)

x_train ,x_test ,y_train ,y_test = train_test_split(x ,y ,test_size = 0.2 ,random_state = 0) 

