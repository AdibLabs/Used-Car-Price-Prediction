
# Used Car Price Prediction 🚗

## Project Overview

This project uses Machine Learning to predict the selling price of used cars based on different car features.

A Linear Regression model is trained using car information such as brand, manufacturing year, engine capacity, kilometers driven, fuel type, and transmission type.

The main goal is to understand how Machine Learning can be used to estimate used car prices.

## Project Objective

- Predict the selling price of used cars.
- Understand the relationship between car features and selling prices.
- Practice data preprocessing and categorical encoding.
- Build and train a Linear Regression model.
- Evaluate the model's prediction performance.

## Dataset Information

The project uses a small sample dataset containing 15 used car records.

### Dataset Features

| Feature | Description |
|---|---|
| Car_ID | Unique car identifier |
| Brand | Car manufacturer |
| Year | Manufacturing year |
| Engine_CC | Engine capacity |
| Kilometers_Run | Total kilometers driven |
| Fuel_Type | Type of fuel |
| Transmission | Manual or Automatic |

### Target Variable

`Price_Lakh` — The selling price of the car in lakh.

## Technologies & Libraries

- Python
- Pandas
- Scikit-learn
- Linear Regression
- Jupyter Notebook / VS Code

## Project Workflow

1. Import required Python libraries.
2. Load the dataset using Pandas.
3. Select input features (X).
4. Select the target variable (y).
5. Split the dataset into training and testing sets.
6. Convert categorical variables into numerical values using One-Hot Encoding (`pd.get_dummies()`).
7. Match training and testing columns.
8. Create a Linear Regression model.
9. Train the model using training data.
10. Predict used car prices using testing data.

## Model Information

**Algorithm:** Linear Regression

**Training Data:** 12 records

**Testing Data:** 3 records

**Input Features:** 12 encoded features

## Initial Prediction Results

The model generated the following predictions:

| Actual Price (Lakh) | Predicted Price (Lakh) |
|---:|---:|
| 15 | 19.22 |
| 6 | 5.78 |
| 18 | 21.85 |

These are initial prediction results. Model evaluation and error analysis will be added after completing the project.

## Project Structure

```text
Used_Car_Project/
│
├── used_cars.csv
├── used_car_analysis.py
└── README.md
```

## How to Run This Project

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Install Required Libraries

```bash
pip install pandas scikit-learn
```

### 3. Run the Python Script

```bash
python used_car_analysis.py
```

## Learning Outcomes

Through this project, I practiced:

- Loading and exploring datasets with Pandas.
- Selecting features and target variables.
- Training and testing data splitting.
- Handling categorical variables.
- One-Hot Encoding.
- Building a Linear Regression model.
- Making predictions using Scikit-learn.

## Project Status

In Progress 🚧

Model evaluation, error analysis, and further improvements are planned.

## Author

**Asif Iqubal Adib**

GitHub: [AdibLabs](https://github.com/AdibLabs)
