import pandas as pd

# Create a simple dataset
data = {
    'Size (sqft)': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Price (Lacs)': [50, 75, 100, 125, 150]
}

df = pd.DataFrame(data)
print(df)


from sklearn.linear_model import LinearRegression

# Features (X) and Labels (Y)
X = df[['Size (sqft)', 'Bedrooms']]
Y = df['Price (Lacs)']

# Train model
model = LinearRegression()
model.fit(X, Y)

# Predict price for 2200 sqft, 3 bedrooms
predicted = model.predict([[2200, 3]])
print("Predicted Price: ", predicted[0], "Lacs")


