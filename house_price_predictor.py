import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy training data
model = LinearRegression()
X = np.array([[1000, 2], [1500, 3], [2000, 4]])  # [area, bedrooms]
y = np.array([50, 80, 120])  # price in lakhs
model.fit(X, y)

def main():
    st.title("🏠 House Price Predictor")
    st.markdown("Enter the details below to estimate the house price:")

    area = st.number_input("Area (in sq ft)", min_value=300, max_value=10000)
    bedrooms = st.slider("Number of bedrooms", 1, 10)

    if st.button("Predict Price"):
        prediction = model.predict([[area, bedrooms]])
        st.success(f"Estimated Price: ₹ {prediction[0]:,.2f} lakhs")

if __name__ == "__main__":
    main()
