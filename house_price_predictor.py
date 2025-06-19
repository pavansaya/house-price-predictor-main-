import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# ⬛ Optional: Set background image
def set_bg():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/ok4x0aS.jpg");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# 🟦 Dummy training data for demo
model = LinearRegression()
X = np.array([[1000, 2], [1500, 3], [2000, 4]])
y = np.array([50, 80, 120])
model.fit(X, y)

# 🟨 Main UI
def main():
    set_bg()

    st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")

    st.markdown("<h1 style='text-align: center; color: #2e86de;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
    st.markdown("### 💬 Enter the details below to estimate house price:")

    # Sidebar inputs
    st.sidebar.header("📋 Input Parameters")
    area = st.sidebar.number_input("📏 Area (sq ft)", min_value=300, max_value=10000, step=100)
    bedrooms = st.sidebar.slider("🛏️ Bedrooms", 1, 10)

    # Predict button
    if st.sidebar.button("🔮 Predict"):
        prediction = model.predict([[area, bedrooms]])
        st.markdown("---")
        st.success(f"💰 **Estimated Price:** ₹ {prediction[0]:,.2f} lakhs")

    st.markdown("---")
    st.markdown("<small>Made with ❤️ using Streamlit | Powered by Linear Regression</small>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
