from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split

# Load CSV
df = pd.read_csv("used_cars.csv")

# Features
X = df[[
    "Brand",
    "Year",
    "Engine_CC",
    "Kilometers_Run",
    "Fuel_Type",
    "Transmission"
]]

# Target
y = df["Price_Lakh"]

# Check Features and Target
print("Features:")
print(X.head())

print("\nTarget:")
print(y.head())

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Categorical Encoding
X_train = pd.get_dummies(X_train, dtype=int)
X_test = pd.get_dummies(X_test, dtype=int)

# Match Test Data Columns with Training Data
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

print("Model Training Completed!")

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

print("\nTraining Columns:")
print(X_train.columns.tolist())

print("\nTesting Columns:")
print(X_test.columns.tolist())

# Make Predictions
y_pred = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)