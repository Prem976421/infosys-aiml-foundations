import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Load Data
df = pd.read_csv('C:\\Users\\PREM MOTGHARE\\Desktop\\introduction to aiml by infosys\\python\\scikit-learn\\auto_mpg.csv')
df.dropna(inplace=True)

# 2. Split Features (x) and Target (y)
x = df.iloc[:, 1:8]
y = df.iloc[:, 0]

# Convert categorical variables into binary columns (0s and 1s)
x = pd.get_dummies(x) 

# 3. Train/Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) 

# 4. Feature Scaling (FIXED)
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.transform(x_test)

# 5. Train the Model
reg = LinearRegression()
reg.fit(x_train, y_train)

# Print the weights (m) and bias (c)
m = reg.coef_
c = reg.intercept_
print(f"Coefficients (m): {m}")
print(f"Intercept (c): {c}")

# 6. Make Predictions on the unseen test data

#Predicting the target: mpg against the predictors in the training data set
#Predicted data stored in y_pred_train
y_pred_train = reg.predict(x_train)

#Predicting the target: mpg against the predictors in the testing data set
#Predicted data stored in y_pred_test
y_pred_test = reg.predict(x_test)

r2_S = r2_score(y_train, y_pred_train)
print(r2_S)

r2_S = r2_score(y_test, y_pred_test)
print(r2_S)