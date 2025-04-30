import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("imdb_top_1000.csv")  # Change filename as needed
print("Data Loaded")

# Select relevant features and drop missing
df = df[['Series_Title', 'Genre', 'Director', 'Star1', 'IMDB_Rating', 'Runtime']]
df.dropna(inplace=True)

# Convert runtime to numeric (e.g., "142 min" → 142)
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

# Select features and target
X = df[['Genre', 'Director', 'Star1', 'Runtime']]
y = df['IMDB_Rating']

# One-hot encoding for categorical variables
X_encoded = pd.get_dummies(X, columns=['Genre', 'Director', 'Star1'], drop_first=True)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R^2 Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Rating")
plt.ylabel("Predicted Rating")
plt.title("Actual vs Predicted Movie Ratings")
plt.grid(True)
plt.show()
