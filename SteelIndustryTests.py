import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

# Load the data into a Pandas dataframe
industry = pd.read_csv(r'C:\Users\Sana R\Downloads\SteelIndustry.csv')

# Separate the independent variables and the dependent variable
industry.head()


#Categorizing variables
industry['WeekStatus'].replace(['Weekday', 'Weekend'],
                        [0, 1], inplace=True)

industry['Day_of_week'].replace(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                        [0,1,2,3,4,5,6], inplace=True)

industry['Load_Type'].replace(['Light_Load', 'Medium_Load', 'Maximum_Load'],
                        [0,1,2], inplace=True)

industry = industry.drop(columns=['date'])
from numpy import float64
industry = industry.astype(float64)

#Splitting data into test and train
X = industry.iloc[:, 2:]
y = industry['Usage_kWh']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the linear regression model
regressor = LinearRegression()

# Train the model using the training data
regressor.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

# Calculate the mean squared error and the coefficient of determination
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('R-squared:', r2)

# Decision tree regressor
from sklearn.tree import DecisionTreeRegressor

# create a regressor object
industry_model = DecisionTreeRegressor(random_state = 42)

# fit the regressor with X and Y data
industry_model.fit(X, y)

prediction = regressor.predict(X_test)

# print the predicted price
print("Prediction:")
print(prediction)

# scatter plot for original data
plt.scatter(X.Leading_Current_Reactive_Power_kVarh, y, color = 'red')

# plot predicted data
plt.plot(X.Leading_Current_Reactive_Power_kVarh, regressor.predict(X), color = 'blue')

# specify title
plt.title('Profit to Production Cost (Decision Tree Regression)')

# specify X axis label
plt.xlabel('Production Cost')

# specify Y axis label
plt.ylabel('Profit')

# show the plot
plt.show()

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import sklearn.metrics as metrics

print(np.sqrt(mean_squared_error(y_test, prediction)))
r2 = metrics.r2_score(y_test,prediction)
print(r2)

#Correlation chart
import seaborn as sns
industry

industry_corr=industry.corr() 

f,ax=plt.subplots(figsize=(12,7)) 

sns.heatmap(industry_corr,cmap='viridis',annot=True) 

plt.title("Correlation between features",weight='bold',fontsize=18) 

plt.show() 

